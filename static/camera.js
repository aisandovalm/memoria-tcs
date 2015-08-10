$(document).ready(function() 
{
	var prgrs_msg = 'Operation in progress, please wait.';

	document.getElementById('imgparameter').onchange = function()
	{
		document.form_imagesettings.elements['response_imagesettings'].value = '';
		var paramvalue = document.form_imagesettings.imgparamvalue;
		var selected = document.form_imagesettings.elements['imgparameter'].value;
		
		paramvalue.options.length = 0;//Se resetea la cantidad de options
		if (selected == "imagesize") 
		{
		  paramvalue.options[0] = new Option('6016x4000','0');
		  paramvalue.options[1] = new Option('4512x3000','1');
		  paramvalue.options[2] = new Option('3008x2000','2');
		}

		if (selected == "iso") 
		{
		  paramvalue.options[0] = new Option('100','0');
		  paramvalue.options[1] = new Option('200','1');
		  paramvalue.options[2] = new Option('400','2');
		  paramvalue.options[3] = new Option('800','3');
		  paramvalue.options[4] = new Option('1600','4');
		  paramvalue.options[5] = new Option('3200','5');
		  paramvalue.options[6] = new Option('6400','6');
		  paramvalue.options[7] = new Option('12800','7');
		}

		if (selected == "whitebalance") 
		{
		  paramvalue.options[0] = new Option('Automatic','0');
		  paramvalue.options[1] = new Option('Daylight','1');
		  paramvalue.options[2] = new Option('Fluorescent','2');
		  paramvalue.options[3] = new Option('Tungsten','3');
		  paramvalue.options[4] = new Option('Flash','4');
		  paramvalue.options[5] = new Option('Cloudy','5');
		  paramvalue.options[6] = new Option('Shade','6');
		  paramvalue.options[7] = new Option('Preset','7');
		}
	};

	$('#form_imagesettings').submit(function(e) 
	{
		if (document.form_imagesettings.imgparamvalue.value == " ") 
		{
			alert("Invalid operation: Please select parameter and value and then click 'Apply setting'");
		}
		else
		{
	        $('#response_imagesettings').html(prgrs_msg);
	        $.ajax(
	        {
	            type: 'POST',
	            url: '/imagesettings',
	            data: $(this).serialize(),
	            success: function(response) {
	                $('#response_imagesettings').html(response);
	            }
	        });
	    }
	    e.preventDefault();
    });
    
    $('#form_currentimagesettings').submit(function(e) 
    {
        $('#response_currentimagesettings').html(prgrs_msg);
        $.ajax({
            type: 'POST',
            url: '/currentimagesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_currentimagesettings').html(response);
            }
        });
        e.preventDefault();
    });


	document.getElementById('captureparameter').onchange = function()
	{
		document.form_capturesettings.elements['response_capturesettings'].value = '';
		var paramvalue = document.form_capturesettings.captureparamvalue;
		var selected = document.form_capturesettings.elements['captureparameter'].value;
		paramvalue.options.length = 0;//Se resetea la cantidad de options
		if (selected == "exposurecompensation") 
		{
		  paramvalue.options[0] = new Option('-5','0');
		  paramvalue.options[1] = new Option('-4.666','1');
		  paramvalue.options[2] = new Option('-4.333','2');
		  paramvalue.options[3] = new Option('-4','3');
		  paramvalue.options[4] = new Option('-3.666','4');
		  paramvalue.options[5] = new Option('-3.333','5');
		  paramvalue.options[6] = new Option('-3','6');
		  paramvalue.options[7] = new Option('-2.666','7');
		  paramvalue.options[8] = new Option('-2.333','8');
		  paramvalue.options[9] = new Option('-2','9');
		  paramvalue.options[10] = new Option('-1.666','10');
		  paramvalue.options[11] = new Option('-1.333','11');
		  paramvalue.options[12] = new Option('-1','12');
		  paramvalue.options[13] = new Option('-0.666','13');
		  paramvalue.options[14] = new Option('-0.333','14');
		  paramvalue.options[15] = new Option('0','15');
		  paramvalue.options[16] = new Option('0.333','16');
		  paramvalue.options[17] = new Option('0.666','17');
		  paramvalue.options[18] = new Option('1','18');
		  paramvalue.options[19] = new Option('1.333','19');
		  paramvalue.options[20] = new Option('1.666','20');
		  paramvalue.options[21] = new Option('2','21');
		  paramvalue.options[22] = new Option('2.333','22');
		  paramvalue.options[23] = new Option('2.666','23');
		  paramvalue.options[24] = new Option('3','24');
		  paramvalue.options[25] = new Option('3.333','25');
		  paramvalue.options[26] = new Option('3.666','26');
		  paramvalue.options[27] = new Option('4','27');
		  paramvalue.options[28] = new Option('4.333','28');
		  paramvalue.options[29] = new Option('4.666','29');
		  paramvalue.options[30] = new Option('5','30');
		}

		if (selected == "flashmode") 
		{
		  paramvalue.options[0] = new Option('Red-eye automatic','0');
		  paramvalue.options[1] = new Option('Auto','1');
		  paramvalue.options[2] = new Option('Rear Curtain Sync + Slow Sync','2');
		}

		if (selected == "f-number") 
		{
		  paramvalue.options[0] = new Option('f/3.5','0');
		  paramvalue.options[1] = new Option('f/4','1');
		  paramvalue.options[2] = new Option('f/4.5','2');
		  paramvalue.options[3] = new Option('f/5','3');
		  paramvalue.options[4] = new Option('f/5.6','4');
		  paramvalue.options[5] = new Option('f/6.3','5');
		  paramvalue.options[6] = new Option('f/7.1','6');
		  paramvalue.options[7] = new Option('f/8','7');
		  paramvalue.options[8] = new Option('f/9','8');
		  paramvalue.options[9] = new Option('f/10','9');
		  paramvalue.options[10] = new Option('f/11','10');
		  paramvalue.options[11] = new Option('f/13','11');
		  paramvalue.options[12] = new Option('f/14','12');
		  paramvalue.options[13] = new Option('f/16','13');
		  paramvalue.options[14] = new Option('f/18','14');
		  paramvalue.options[15] = new Option('f/20','15');
		  paramvalue.options[16] = new Option('f/22','16');
		}

		if (selected == "imagequality") 
		{
		  paramvalue.options[0] = new Option('JPEG Basic','0');
		  paramvalue.options[1] = new Option('JPEG Normal','1');
		  paramvalue.options[2] = new Option('JPEG Fine','2');
		  paramvalue.options[3] = new Option('NEF (Raw)','3');
		  paramvalue.options[4] = new Option('NEF+Fine','4');
		}

		if (selected == "focusmode") 
		{
		  paramvalue.options[0] = new Option('Manual','0');
		  paramvalue.options[1] = new Option('AF-S','1');
		  paramvalue.options[2] = new Option('AF-C','2');
		  paramvalue.options[3] = new Option('AF-A','3');
		  paramvalue.options[4] = new Option('Unknown value 8013','4');
		}

		if (selected == "expprogram") 
		{
		  paramvalue.options[0] = new Option('M','0');
		  paramvalue.options[1] = new Option('P','1');
		  paramvalue.options[2] = new Option('A','2');
		  paramvalue.options[3] = new Option('S','3');
		  paramvalue.options[4] = new Option('Auto','4');
		  paramvalue.options[5] = new Option('Portrait','5');
		  paramvalue.options[6] = new Option('Landscape','6');
		  paramvalue.options[7] = new Option('Macro','7');
		  paramvalue.options[8] = new Option('Sports','8');
		  paramvalue.options[9] = new Option('Night Portrait','9');
		  paramvalue.options[10] = new Option('Night Landscape','10');
		  paramvalue.options[11] = new Option('Children','11');
		}

		if (selected == "capturemode") 
		{
		  paramvalue.options[0] = new Option('Single Shot','0');
		  paramvalue.options[1] = new Option('Burst','1');
		  paramvalue.options[2] = new Option('Timer','2');
		  paramvalue.options[3] = new Option('Quick Response Remote','3');
		  paramvalue.options[4] = new Option('Delayed Remote','4');
		  paramvalue.options[5] = new Option('Quiet Release','5');
		}

		if (selected == "focusmetermode") 
		{
		  paramvalue.options[0] = new Option('Multi-spot','0');
		  paramvalue.options[1] = new Option('Single Area','1');
		  paramvalue.options[2] = new Option('Closest Subject','2');
		  paramvalue.options[3] = new Option('Group Dynamic','3');
		}

		if (selected == "exposuremetermode") 
		{
		  paramvalue.options[0] = new Option('Center Weighted','0');
		  paramvalue.options[1] = new Option('Multi Spot','1');
		  paramvalue.options[2] = new Option('Center Spot','2');
		}

		if (selected == "shutterspeed") 
		{
		  paramvalue.options[0] = new Option('0.0002s','0');
		  paramvalue.options[1] = new Option('0.0003s','1');
		  paramvalue.options[2] = new Option('0.0004s','2');
		  paramvalue.options[3] = new Option('0.0005s','3');
		  paramvalue.options[4] = new Option('0.0006s','4');
		  paramvalue.options[5] = new Option('0.0008s','5');
		  paramvalue.options[6] = new Option('0.0010s','6');
		  paramvalue.options[7] = new Option('0.0012s','7');
		  paramvalue.options[8] = new Option('0.0015s','8');
		  paramvalue.options[9] = new Option('0.0020s','9');
		  paramvalue.options[10] = new Option('0.0025s','10');
		  paramvalue.options[11] = new Option('0.0031s','11');
		  paramvalue.options[12] = new Option('0.0040s','12');
		  paramvalue.options[13] = new Option('0.0050s','13');
		  paramvalue.options[14] = new Option('0.0062s','14');
		  paramvalue.options[15] = new Option('0.0080s','15');
		  paramvalue.options[16] = new Option('0.0100s','16');
		  paramvalue.options[17] = new Option('0.0125s','17');
		  paramvalue.options[18] = new Option('0.0166s','18');
		  paramvalue.options[19] = new Option('0.0200s','19');
		  paramvalue.options[20] = new Option('0.0250s','20');
		  paramvalue.options[21] = new Option('0.0333s','21');
		  paramvalue.options[22] = new Option('0.0400s','22');
		  paramvalue.options[23] = new Option('0.0500s','23');
		  paramvalue.options[24] = new Option('0.0666s','24');
		  paramvalue.options[25] = new Option('0.0769s','25');
		  paramvalue.options[26] = new Option('0.1000s','26');
		  paramvalue.options[27] = new Option('0.1250s','27');
		  paramvalue.options[28] = new Option('0.1666s','28');
		  paramvalue.options[29] = new Option('0.2000s','29');
		  paramvalue.options[30] = new Option('0.2500s','30');
		  paramvalue.options[31] = new Option('0.3333s','31');
		  paramvalue.options[32] = new Option('0.4000s','32');
		  paramvalue.options[33] = new Option('0.5000s','33');
		  paramvalue.options[34] = new Option('0.6250s','34');
		  paramvalue.options[35] = new Option('0.7692s','35');
		  paramvalue.options[36] = new Option('1.0000s','36');
		  paramvalue.options[37] = new Option('1.3000s','37');
		  paramvalue.options[38] = new Option('1.6000s','38');
		  paramvalue.options[39] = new Option('2.0000s','39');
		  paramvalue.options[40] = new Option('2.5000s','40');
		  paramvalue.options[41] = new Option('3.0000s','41');
		  paramvalue.options[42] = new Option('4.0000s','42');
		  paramvalue.options[43] = new Option('5.0000s','43');
		  paramvalue.options[44] = new Option('6.0000s','44');
		  paramvalue.options[45] = new Option('8.0000s','45');
		  paramvalue.options[46] = new Option('10.0000s','46');
		  paramvalue.options[47] = new Option('13.0000s','47');
		  paramvalue.options[48] = new Option('15.0000s','48');
		  paramvalue.options[49] = new Option('20.0000s','49');
		  paramvalue.options[50] = new Option('25.0000s','50');
		  paramvalue.options[51] = new Option('30.0000s','51');
		  paramvalue.options[52] = new Option('429496.7295s','52');
		}
	};

    $('#form_capturesettings').submit(function(e) 
    {
    	if (document.form_imagesettings.imgparamvalue.value == " ") 
		{
			alert("Invalid operation: Please select parameter and value and then click 'Apply setting'");
		}
		else
		{
	        $('#response_capturesettings').html(prgrs_msg);
	        $.ajax({
	            type: 'POST',
	            url: '/capturesettings',
	            data: $(this).serialize(),
	            success: function(response) {
	                $('#response_capturesettings').html(response);
	            }
	        });
	    }
        e.preventDefault();
    });
    
    $('#form_currentcapturesettings').submit(function(e) 
    {
        $('#response_currentcapturesettings').html(prgrs_msg);
        $.ajax({
            type: 'POST',
            url: '/currentcapturesettings',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_currentcapturesettings').html(response);
            }
        });
        e.preventDefault();
    });

    $('#form_imagesequence').submit(function(e) 
    {
        $('#response_imagesequence').html(prgrs_msg);
        $.ajax({
            type: 'POST',
            url: '/imagesequence',
            data: $(this).serialize(),
            success: function(response) {
                $('#response_imagesequence').html(response);
            }
        });
        e.preventDefault();
    });
});