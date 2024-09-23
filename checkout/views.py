from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shopping_bag.contexts import shopping_bag_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .models import OrderItem, Order



import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shopping_bag': json.dumps(request.session.get('shopping_bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)



def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method =='POST':
       shopping_bag = request.session.get('shopping_bag',{})
        
       form_data ={
            'full_name':request.POST['full_name'],
            'email':request.POST['email'],
            'phone':request.POST['phone'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'town_city': request.POST['town_city'],
            'county_region': request.POST['county_region'],
            'country':request.POST['country'],
            'eircode':request.POST['eircode'],
        }
       order_form = OrderForm(form_data)
       if order_form.is_valid():
           order = order_form.save(commit=False)
           pid = request.POST.get('client_secret').split('_secret')[0] 
           order.stripe_pid = pid
           order.original_bag = json.dumps(shopping_bag)
           order.save() 
                     
           for item_id, item_data in shopping_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request,(
                        "Issue on our database. Please reach out our member staff"
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))

           request.session['save_info'] = 'save-info' in request.POST
           return redirect(reverse('checkout_success', args=[order.order_number]))
       else:
          messages.error(request, 'There was an error with your form. \
              Please double check your information.')   
         
    else:
        shopping_bag = request.session.get('shopping_bag',{})
        if not shopping_bag:
            messages.error(request, "No items in your shopping bag")
            return redirect(reverse('Products'))

        current_bag = shopping_bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name':profile.user.get_full_name(),
                    'email':profile.user.email,
                    'phone':profile.default_phone,
                    'address1':profile.default_address1,
                    'address2': profile.default_address2,
                    'town_city': profile.default_town_city,
                    'county_region': profile.default_county_region,
                    'country':profile.default_country,
                    'eircode':profile.default_eircode,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:              
            order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile= UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data ={
            'default_phone': order.phone,
            'default_address1': order.address1,
            'default_address2': order.address2,
            'default_town_city': order.town_city,
            'default_county_region': order.county_region,
            'default_eircode': order.eircode,
            }
            user_profile_form = UserProfileForm(profile_data,instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()


    messages.success(request, f'The order has been successfully completed !!  Order Number: {order_number}. We will shortly send a confirmation email to {order.email}. Thank you !! ')
    
    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'checkout/checkout_success.html'
    context ={
        'order':order,
    }

    return render(request, template, context)
