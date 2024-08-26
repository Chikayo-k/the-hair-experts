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