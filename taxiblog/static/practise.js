

$(document).ready(function() {

var target = '.buttons';
var hoverClass = 'buttonsHover';

$(target).each(function() {
$(this).hover(

	function() {
	$(this).addClass(hoverClass);
	status=$(this).find('a').attr('href');
				},
	
	function() {
	$(this).removeClass(hoverClass);
	status='';
				});
	
	$(this).click(function() {
	location = $(this).find('a').attr('href');
	});
	
	$(this).css('cursor','pointer');

});

});