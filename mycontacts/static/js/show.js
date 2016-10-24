//Requires JQuery or Zepto
$(document).ready(function(){

// Cache Header
var $header = $('.header');

// Get height of global-header to use later as starting point
var $hHeight = $header.height();

// Set initial position to current position on page
var prevTop = $(window).scrollTop();

// Scroll event
$(window).on('scroll', function(e) {
  var st = $(this).scrollTop(); // Set scroll location
  if (st > prevTop && st > $hHeight) { 
    $header.addClass('js-global-header-scrolling');
  } else {
    $header.removeClass('js-global-header-scrolling');
  }
  prevTop = st;
});
});