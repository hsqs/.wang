
$(function(){
	$(".title-home").bind("click", function(){
		var htmlobj = $.ajax({url:"http://hsqs.wang",async:false});
  		$("body").html(htmlobj.responseText);
	});
});