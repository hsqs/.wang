

function initTitleColor() {
	$(".navbar-default .navbar-nav>li>a").bind("click", function(){
		var links = $(".navbar-default .navbar-nav>li>a");
		$.each(links, function(index, data){
			$(this).css("color", "#fff");
		});

		var className = $(this).attr('class');
		$(".navbar-default .navbar-nav>li>." + className).css("color", "#000");
	});

	$(".navbar-default .navbar-nav>li>.title-home").css("color", "#000");
}

/**
 * load blog data
 */
function blogPageClick() {
	$(".navbar-default .navbar-nav>li>.title-blog").bind("click", function(){
		alert("uu");
	});
}

$(function(){

	initTitleColor();

	blogPageClick();
});