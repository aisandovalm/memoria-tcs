$(document).ready(function() {
    $('#form_test').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/ajax',
            data: $(this).serialize(),
            success: function(response) {
                $('#ajaxP').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_getposition').submit(function(e) {
        //var coord = $('#coordinates').val();
        alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/getposition',
            data: $(this).serialize(),
            success: function(response) {
                $('#position').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotoradec').submit(function(e) {
        alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotoradec',
            data: $(this).serialize(),
            success: function(response) {
                $('#estado').html(response);
            }
        });
        e.preventDefault();
    });
});