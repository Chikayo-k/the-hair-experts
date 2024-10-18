/*globals $:false */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'gray');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'gray');
    } else {
        $(this).css('color', 'black');
    }
});