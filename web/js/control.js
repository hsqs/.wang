

function initTitleColor() {

	var links = $(".navbar-default .navbar-nav>li>a");
	$.each(links, function(index, data){
		$(this).css("color", "#fff");
	});

	$(".navbar-default .navbar-nav>li>.title-home").css("color", "#000");
}

/**
 * load blog data
 */
function blogPageClick() {
	$(".navbar-default .navbar-nav>li>.title-blog").bind("click", function(){
		window.location.href = 'web/html/blog0001/blog0001.html';
	});
}

$(function(){

	initTitleColor();

	blogPageClick();
});