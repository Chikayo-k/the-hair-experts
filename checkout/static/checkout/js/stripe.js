/*globals $:false */
const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle errors
card.addEventListener('change', function(e) {
    const errorMessage = document.getElementById('card-errors');
    if (e.error) {
        const content = `<p>${e.error.message}</p>`;
        $(errorMessage).html(content);
    } else {
        errorMessage.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {

    console.log('FORM: ', form);
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    const saveInfo = Boolean($('#id-save-info').attr('checked'));
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.address1.value),
                        line2: $.trim(form.address2.value),
                        city: $.trim(form.town_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county_region.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone.value),
                address: {
                    line1: $.trim(form.address1.value),
                    line2: $.trim(form.address2.value),
                    city: $.trim(form.town_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.eircode.value),
                    state: $.trim(form.county_region.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                const errorMessage = document.getElementById('card-errors');
                const content = `<p>${result.error.message}</p>`;
                $(errorMessage).html(content);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    });
});