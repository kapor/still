/*const close_button = document.getElementById('modal_close');
const underlay = document.getElementsByClassName('modal_underlay');
const body_block = document.getElementsByClassName("body_block");
const button_xsmall = document.getElementsByClassName("modal_button_xsmall");


underlay.addEventListener('click', function() {
  if (document.body.style.overflow === 'hidden') {
    document.body.style.overflow = 'visible';
  } else {
    document.body.style.overflow = 'hidden';
  }
});
underlay.addEventListener('click', function() {
  if (body_block.classList.contains("hidden")) {
    body_block.classList.remove("hidden");
  } else {
    body_block.classList.add("hidden");
  }
});

close_button.addEventListener('click', function() {
  if (document.body.style.overflow === 'hidden') {
    document.body.style.overflow = 'visible';
  } else {
    document.body.style.overflow = 'hidden';
  }
});
close_button.addEventListener('click', function() {
  if (body_block.classList.contains("hidden")) {
    body_block.classList.remove("hidden");
  } else {
    body_block.classList.add("hidden");
  }
});

button_xsmall.addEventListener('click', function() {
  if (document.body.style.overflow === 'hidden') {
    document.body.style.overflow = 'visible';
  } else {
    document.body.style.overflow = 'hidden';
  }
});
button_xsmall.addEventListener('click', function() {
  if (body_block.classList.contains("hidden")) {
    body_block.classList.add("hidden");
  } else {
    body_block.classList.add("hidden");
  }
});
*/




/* ++++++++++ DISABLE SCROLLBAR ++++++++++ */

$('.modal_underlay').click(function(){
  $('.body_block').css("overflow", "visible");
  $('body').css("overflow", "visible");
});


$(document).keyup(function(e) {
 if (e.key === "Escape") { 
    $('.body_block').css("overflow", "visible");
    $('body').css("overflow", "visible");
  }
});

$('.modal_button_xsmall').click(function(){
  $('.body_block').css("overflow", "hidden");
  $('body').css("overflow", "hidden");
});

$('#modal_trigger').click(function(){
  $('.body_block').css("overflow", "hidden");
  $('body').css("overflow", "hidden");
});

$('#modal_close').click(function(){
    $('.body_block').css("overflow", "visible");
    $('body').css("overflow", "visible");
});




document.addEventListener('keydown', function(event) {
  if (event.keyCode === 27) {
    const modal = document.querySelector('#modal'); // Replace '.modal' with the actual selector of your modal
    if (modal && modal.style.display !== 'none') {
      const closeButton = modal.querySelector('#modal_close'); // Replace '.close-button' with the actual selector of your close button
      if (closeButton) {
        closeButton.click();
      }
    }
  }
});

