var TarValues;

function deleteSequence(seq)
{
	console.log("delete: " + TarValues[seq]);
	$.ajax(
    {
        type: 'POST',
        url: '/deletesequence',
        data: TarValues[seq],
        success: function(response) {
            $('#tar_'+seq).slideUp();
        }
    });
}

$(document).ready(function() 
{
    $('#gettarsbutton').click(function(){
    	$('#sequences').hide(1000);
    	$('#sequenceTable').empty();
    	$.getJSON('/gettars', function(response){
    		TarValues = response;
    		$('#sequenceTable').append('<tr><th>Sequence</th><th>Action</th></tr>');
    		$.each(response, function(key, val) {
    			$('#sequenceTable').append('<tr id="tar_'+key+'"><td><a href="/static/images/'+val+'" download="'+val+'">'+val+'</a></td><td><button class="btn btn-danger" onclick="deleteSequence('+key+')">Delete</button></td></tr>');
    		});
    		$('#sequences').show(1000);
    	});
    });
});


