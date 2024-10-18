/*globals $:false */
// Sorting
$('#sort').change(function(){
    let selector = $(this);
    let url = new URL(window.location);

    let selectedValue = selector.val();
    if(selectedValue != 'reset'){
        let sort = selectedValue.split('_')[0];
        let direction = selectedValue.split('_')[1];

        url.searchParams.set('sort',sort);
        url.searchParams.set('direction',direction);

        window.location.replace(url);
    }else{
        url.searchParams.delete('sort');
        url.searchParams.delete('direction');
    }
});


// Scroll top
$('.scroll-top').click(function(e){
    window.scroll(0,0);
});


//Increment Decrement quantity button
    function enableDisable(itemId){
        const valueNow = parseInt($(`#id_qty_${itemId}`).val());
        const minimum = valueNow < 2;
        const maximum = valueNow > 98;
        $(`#decrement${itemId}`).prop('disabled',minimum);
        $(`#increment${itemId}`).prop('disabled',maximum);
    }
    
    const quantity = $('.quantity_input');
    for(let i = 0; i < quantity.length; i++){
        const itemId = $(quantity[i]).data('item_id');
        enableDisable(itemId);
    }

    $('.quantity_input').change(function(){
        const itemId = $(this).data('item_id');
        enableDisable(itemId);
    });

    // Increment quantity
    $('.increment').click(function(e) {
        e.preventDefault();
        const closestInput = $(this).closest('.input-group').find('.quantity_input')[0];
        const currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        const itemId = $(this).data('item_id');
        enableDisable(itemId);
     });
 
     // Decrement quantity
     $('.decrement').click(function(e) {
        e.preventDefault();
        const closestInput = $(this).closest('.input-group').find('.quantity_input')[0];
        const currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        const itemId = $(this).data('item_id');
        enableDisable(itemId);
     });