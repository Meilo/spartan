$(document).ready(function(){
	$('#sign').click(function(){
		$('#home-content').hide();
		$('#home-content-connect').hide();
		$('#home-content-sign').fadeIn();
		$('#sign').css('color', '#FF6600');
		$('#connect').css('color', '#ffffff');
		$('.retour').fadeIn();
	});
	$('#connect').click(function(){
		$('#home-content').hide();
		$('#home-content-sign').hide();
		$('#home-content-connect').fadeIn();
		$('#connect').css('color', '#FF6600');
		$('#sign').css('color', '#ffffff');
		$('.retour').fadeIn();
	});
	$('.retour').click(function(){
		$('#home-content').fadeIn();
		$('#home-content-connect').hide();
		$('#home-content-sign').hide();
		$('#sign').css('color', '#ffffff');
		$('#connect').css('color', '#ffffff');
		$('.retour').fadeOut();
	});
});