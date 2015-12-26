

function initAboutTitle() {

	var links = $(".navbar-default .navbar-nav>li>a");
	$.each(links, function(index, data){
		$(this).css("color", "#fff");
	});

	$(".navbar-default .navbar-nav>li>.title-about").css("color", "#000");
}


$(function(){
	
	initAboutTitle();
});