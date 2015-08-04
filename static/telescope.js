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
        //alert($(this).serialize());
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
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotoradec',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotopreciseradec').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotopreciseradec',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotoradechdms').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotoradechdms',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotoazmalt').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotoazmalt',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotopreciseazmalt').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotopreciseazmalt',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gotoazmaltdms').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/gotoazmaltdms',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_syncradec').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/syncradec',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_syncpreciseradec').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/syncpreciseradec',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_syncradechdms').submit(function(e) {
        //alert($(this).serialize());
        $.ajax({
            type: 'POST',
            url: '/syncradechdms',
            data: $(this).serialize(),
            success: function(response) {
                $('#response').html(response);
            }
        });
        e.preventDefault();
    });

    $('#gettrackingmodeButton').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gettrackingmode',
            success: function(response) {
                $('#trackingmode').html(response);
            }
        });
        e.preventDefault();
    });
});