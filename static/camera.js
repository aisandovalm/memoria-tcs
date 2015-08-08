$(document).ready(function() {
    $('#form_generalsettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/generalsettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_generalsettings').html(response);
            }
        });
        e.preventDefault();
    });
    
    $('#form_actualgeneralsettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/actualgeneralsettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_actualgeneralsettings').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_imagesettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/imagesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_imagesettings').html(response);
            }
        });
        e.preventDefault();
    });
    
    $('#form_actualimagesettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/actualimagesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_actualimagesettings').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_capturesettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/capturesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_capturesettings').html(response);
            }
        });
        e.preventDefault();
    });
    
    $('#form_actualcapturesettings').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/actualcapturesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_actualcapturesettings').html(response);
            }
        });
        e.preventDefault();
    });
});