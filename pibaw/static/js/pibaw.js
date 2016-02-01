// menu animation
$(".nav").css({
	"top": "-3.5em",
});

$(document).ready(function() {
	setTimeout(function(){ 
		$('.nav').animate({
			top: '0em'
		}, {
			duration: 800,
			easing: 'easeOutBounce'

			
			// 1000, 
			// 
		});
	}, 1000);
	 
});
