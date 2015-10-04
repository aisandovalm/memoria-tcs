var LogValues;

function deleteSystemLog(log)
{
	console.log("delete: " + LogValues[log]);
	$.ajax(
    {
        type: 'POST',
        url: '/deletesystemlog',
        data: LogValues[log],
        success: function(response) {
            console.log(response);
            $('#system_'+log).slideUp(1000);
        }
    });
}

function deleteServerLog(log)
{
	console.log("delete: " + LogValues[log]);
	$.ajax(
    {
        type: 'POST',
        url: '/deleteserverlog',
        data: LogValues[log],
        success: function(response) {
            console.log(response);
            $('#server_'+log).slideUp(1000);
        }
    });
}

$(document).ready(function() 
{
    $('#systembutton').click(function(){
    	$('#serverlogs').hide(1000);
    	$.getJSON('/getsystemlogs', function(response){
    		LogValues = response;
    		$.each(response, function(key, val) {
    			$('#systemTable').append('<tr id="system_'+key+'"><td><a href="/static/logs/system/'+val+'" download="'+val+'">'+val+'</a></td><td><button class="btn btn-danger" onclick="deleteSystemLog('+key+')">Delete</button></td></tr>');
    		});
    		$('#systemlogs').show(1000);
    	});
    });

    $('#serverbutton').click(function(){
    	console.log('serverlogs');
    	$('#systemlogs').hide(1000);
    	$.getJSON('/getserverlogs', function(response){
    		LogValues = response;
    		$.each(response, function(key, val) {
    			$('#serverTable').append('<tr id="server_'+key+'"><td><a href="/static/logs/server/'+val+'" download="'+val+'">'+val+'</a></td><td><button class="btn btn-danger" onclick="deleteServerLog('+key+')">Delete</button></td></tr>');
    		});
    		$('#serverlogs').show(1000);
    	});
    });
});
