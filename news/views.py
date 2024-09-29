from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from news.forms import NewsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def news(request):
    """
    Display news
    """
    news = News.objects.all()
    
    # Add news
    if request.method == 'POST':
        
        form = NewsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'News was added succssfuly')
            return redirect('news')
        else:
            messages.error(request, 'News was not added. Please try again')

    else:
        form = NewsForm()
            

    return render(request, 'news/news.html',{'news': news, 'form':form})



@login_required 
def news_edit(request,news_id):
    """
    Edit news
    """
    if not request.user.is_superuser:
        messages.error(request, 'limited to store owners')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form= NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated news successfully!')
            return redirect('news')
        else:
            messages.error(request,'Failed to update news. Please try again.')
            return render(request, 'news/news.html',{'news': news, 'form':form})
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are editing {news.title}')

    template ='news/news_edit.html'
    context ={
        'form':form,
        'news':news,
    }

    return render(request,template,context)




