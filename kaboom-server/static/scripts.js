$(document).on('click', '.bomb:not(.inactive)', function() {
	var pin, time;
	pin = $(this).attr('rel');
	time = $('#time').val();
	$(this).addClass('inactive');
	$.post('shoot', 'pin=' + pin + '&time=' + time, function() {
		var pinLink = $('.bomb[rel="' + pin + '"]');
		pinLink.removeClass('inactive');
	});
	return false;
});
