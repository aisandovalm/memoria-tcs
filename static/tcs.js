$(document).ready(function() {
    $('form').submit(function(e) {
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
});