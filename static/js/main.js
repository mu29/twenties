$(document).ready(function() {
	$('nav').affix({
		offset: {
			top: $(window).height()
		}
	});

	$('nav ul li a').click(function(event) {
		event.preventDefault();
		var where = $(this).text().toLowerCase();
		$('html,body').animate({
			scrollTop: $('a[name=' + where + ']').offset().top
		});
	});
});
