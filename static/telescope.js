$(document).ready(function() 
{
    var prgrs_msg = 'Operation in progress, please wait.';

    $('#form_getposition').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#position').html(prgrs_msg);
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

    $('#form_gotoradec').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotoradec').html(prgrs_msg);
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

    $('#form_gotopreciseradec').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotopreciseradec').html(prgrs_msg);
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

    $('#form_gotoradechdms').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotoradechdms').html(prgrs_msg);
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

    $('#form_gotoazmalt').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotoazmalt').html(prgrs_msg);
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

    $('#form_gotopreciseazmalt').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotopreciseazmalt').html(prgrs_msg);
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

    $('#form_gotoazmaltdms').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_gotoazmaltdms').html(prgrs_msg);
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

    $('#form_syncradec').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_syncradec').html(prgrs_msg);
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

    $('#form_syncpreciseradec').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_syncpreciseradec').html(prgrs_msg);
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

    $('#form_syncradechdms').submit(function(e) 
    {
        //alert($(this).serialize());
        $('#response_syncradechdms').html(prgrs_msg);
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

    
    $('#gettrackingmodeButton').click(function()
    {
        //stopPropagation();
        $('#response_gettrackingmode').html(prgrs_msg);
        $.get('/gettrackingmode', function(response)
        {
            $('#response_gettrackingmode').html(response);
        });
    });

    $('#form_settrackingmode').submit(function(e) 
    {
        $('#response_settrackingmode').html(prgrs_msg);
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

    $('#form_slewing').submit(function(e) 
    {
        $('#response_slewing').html(prgrs_msg);
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

    $('#stopslewingButton').click(function () 
    {
        $('#response_stopslewing').html(prgrs_msg);
        $.get('/stopslewing', function(response)
        {   
            $('#response_stopslewing').html(response);
        });
    });

    $('#getlocationButton').click(function() 
    {
        $('#location').html(prgrs_msg);
        $.get('/getlocation', function(response)
        {
            $('#location').html(response);
        });
    });

    $('#form_setlocation').submit(function(e) 
    {
        $('#response_setlocation').html(prgrs_msg);
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

    $('#gettimeButton').click(function() 
    {
        $('#time').html(prgrs_msg);
        $.get('/gettime', function(response)
        {
            $('#time').html(response);
        });
    });

    $('#form_settime').submit(function(e) 
    {
        $('#response_settime').html(prgrs_msg);
        $.ajax({
            type: 'POST',
            url: '/settime',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_settime').html(response);
            }
        });
        e.preventDefault();
    });

    $('#gpscheckButton').click(function() 
    {
        $('#response_gpscheck').html(prgrs_msg);
        $.get('/gpscheck', function(response)
        {
            $('#response_gpscheck').html(response);
        });
    });

    $('#form_gpsgetlatitude').submit(function(e) 
    {
        $('#response_gpsgetlatitude').html(prgrs_msg);
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

    $('#form_gpsgetlongitude').submit(function(e) 
    {
        $('#response_gpsgetlongitude').html(prgrs_msg);
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

    $('#gpsgetdateButton').click(function() 
    {
        $('#response_gpsgetdate').html(prgrs_msg);
        $.get('/gpsgetdate', function(response)
        {
            $('#response_gpsgetdate').html(response);
        });
    });

    $('#gpsgettimeButton').click(function() 
    {
        $('#response_gpsgettime').html(prgrs_msg);
        $.get('/gpsgettime', function(response)
        {
            $('#response_gpsgettime').html(response);
        });
    });

    $('#rtcgetdateButton').click(function() 
    {
        $('#response_rtcgetdate').html(prgrs_msg);
        $.get('/rtcgetdate', function(response)
        {
            $('#response_rtcgetdate').html(response);
        });
    });

    $('#rtcgettimeButton').click(function() 
    {
        $('#response_rtcgettime').html(prgrs_msg);
        $.get('/rtcgettime', function(response)
        {
            $('#response_rtcgettime').html(response);
        });
    });

    $('#form_rtcsetdate').submit(function(e) 
    {
        $('#response_rtcsetdate').html(prgrs_msg);
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

    $('#form_rtcsettime').submit(function(e) 
    {
        $('#response_rtcsettime').html(prgrs_msg);
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

    $('#form_version').submit(function(e) 
    {
        $('#response_version').html(prgrs_msg);
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

    $('#form_deviceversion').submit(function(e) 
    {
        $('#response_deviceversion').html(prgrs_msg);
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

    $('#form_model').submit(function(e) 
    {
        $('#response_model').html(prgrs_msg);
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