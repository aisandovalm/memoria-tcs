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
                $('#response_gotoradec').html(response);
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
                $('#response_gotopreciseradec').html(response);
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
                $('#response_gotoradechdms').html(response);
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
                $('#response_gotoazmalt').html(response);
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
                $('#response_gotopreciseazmalt').html(response);
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
                $('#response_gotoazmaltdms').html(response);
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
                $('#response_syncradec').html(response);
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
                $('#response_syncpreciseradec').html(response);
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
                $('#response_syncradechdms').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gettrackingmode').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gettrackingmode',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gettrackingmode').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_settrackingmode').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/settrackingmode',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_settrackingmode').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_slewing').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/slewing',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_slewing').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_getlocation').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/getlocation',
            data: $(this).serialize(),
            success: function(response) {
                $('#location').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_setlocation').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/setlocation',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_setlocation').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gettime').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gettime',
            data: $(this).serialize(),
            success: function(response) {
                $('#time').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_settime').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: 'settime',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_settime').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gpscheck').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gpscheck',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gpscheck').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gpsgetlatitude').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gpsgetlatitude',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gpsgetlatitude').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gpsgetlongitude').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gpsgetlongitude',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gpsgetlongitude').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gpsgetdate').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gpsgetdate',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gpsgetdate').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_gpsgettime').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/gpsgettime',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_gpsgettime').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_rtcgetdate').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/rtcgetdate',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_rtcgetdate').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_rtcgettime').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/rtcgettime',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_rtcgettime').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_rtcsetdate').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/rtcsetdate',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_rtcsetdate').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_rtcsettime').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/rtcsettime',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_rtcsettime').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_version').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/version',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_version').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_deviceversion').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/deviceversion',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_deviceversion').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_model').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: '/model',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_model').html(response);
            }
        });
        e.preventDefault();
    });
});