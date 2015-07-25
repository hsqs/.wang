
$(function(){
	$(".navbar-default .navbar-nav>li>a").bind("click", function(){
		var links = $(".navbar-default .navbar-nav>li>a");
		$.each(links, function(index, data){
			$(this).css("color", "#fff");
		});

		var className = $(this).attr('class');
		$(".navbar-default .navbar-nav>li>." + className).css("color", "#000");
	});
});