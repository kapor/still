

// When the user scrolls down 80px from the top of the document, resize the navbar
window.onscroll = function() {scrollNav()};
function scrollNav() {
  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    document.getElementById("nav_bar").style.margin = "0px 0px";
    document.getElementById("nav_bar").style.boxShadow = "0px 2px .10px #CCC";
    document.getElementById("nav_bar").style.padding="20px 24px";
    document.getElementById("navbar_right").style.lineHeight = "24px";
    document.getElementById("navbar_left").style.lineHeight = "24px";
  } else {
    document.getElementById("nav_bar").style.margin = "0px 0px";
    document.getElementById("nav_bar").style.boxShadow = "0px 0px 0px #CCC";
    document.getElementById("nav_bar").style.padding="20px 32px";
    document.getElementById("navbar_right").style.lineHeight = "48px";
    document.getElementById("navbar_left").style.lineHeight = "48px";
  }
};



document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
  document.getElementById('underlay').style.display = "none";
  document.getElementById('dialog_modal').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
  }
});

document.getElementById('btn_modal').addEventListener('click', function() {
  document.getElementById('underlay').classList.add('is_visible');
  document.getElementById('dialog_modal').classList.add('is_visible');
  document.getElementById('underlay').style.display = "block";
  document.getElementById('dialog_modal').style.display = "flex";
  document.body.style.overflow = "hidden"; 
  document.body.style.height = "100%"; 
});

document.getElementById('close_btn').addEventListener('click', function() {
  document.getElementById('underlay').classList.remove('is_visible');
  document.getElementById('dialog_modal').classList.remove('is_visible');
  document.getElementById('underlay').style.display = "none";
  document.getElementById('dialog_modal').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
});

document.getElementById('confirm_btn').addEventListener('click', function() {
  document.getElementById('underlay').classList.remove('is_visible');
  document.getElementById('dialog_modal').classList.remove('is_visible');
  document.getElementById('underlay').style.display = "none";
  document.getElementById('dialog_modal').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
});

document.getElementById('underlay').addEventListener('click', function() {
  document.getElementById('underlay').classList.remove('is_visible');
  document.getElementById('dialog_modal').classList.remove('is_visible');
  document.getElementById('underlay').style.display = "none";
  document.getElementById('dialog_modal').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
});







/* ++++++++++ DISABLE SCROLLBAR ++++++++++ */


$('#col_3').click(function(){
  $('.lotsofstuff').css("overflow", "hidden");
  $('body').css("overflow", "hidden");
});


$('.info_overlay_left').click(function(){
  $('body').css("overflow", "visible");
});

$('.info_close').click(function(){
  $('body').css("overflow", "visible");
});

$(document).keyup(function(e) {
 if (e.key === "Escape") { 
    $('body').css("overflow", "visible");
  }
});

$('#col_2_mobile').click(function(){
  $('#big_2').css("overflow", "hidden");
  $('body').css("overflow", "hidden");
  $('.menu_grid_mobile').css("overflow", "scroll");
});

$('.mygrid_data_column_1').click(function(){
  $('body').css("overflow", "visible");
});

$('#closebutton').click(function(){
  $('body').css("overflow", "visible");
});
