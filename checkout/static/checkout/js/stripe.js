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
const card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle errors
card.addEventListener('change',function(e){
    const errorMessage = document.getElementById('card-errors');
    if(e.error){
        const content =`<p>${e.error.message}</p>`;
        $(errorMessage).html(content);
    }else{
        errorMessage.textContent= '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            const errorMessage = document.getElementById('card-errors');
            const content =`<p>${result.error.message}</p>`;
            $(errorMessage).html(content);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});