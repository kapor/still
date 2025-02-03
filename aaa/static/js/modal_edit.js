
var edit = document.getElementsByClassName("edit_book")[0];
var back = document.querySelectorAll("big_back")[0];
var btn_close = document.getElementsByClassName("modal_button_cancel")[0];
var modalback_e = document.getElementsByClassName("modal_edit_back")[0];
var modal_e = document.getElementsByClassName("modal_edit")[0];
var close = document.getElementsByClassName("modal_close")[0];

// FUNCTIONS

function openEdit() {
  modalback_e.style.display = "block";
  setTimeout(() => { modalback_e.style.opacity = "1"}, 20);
  setTimeout(() => { modal_e.style.height = "100%" }, 0);
  setTimeout(() => { edit.style.opacity = "0%" }, 0);
  setTimeout(() => { back.style.opacity = "0%" }, 0);
}

function closeEdit() {
  setTimeout(() => { modal_e.style.height = "0" }, 50);
  setTimeout(() => { modalback_e.style.opacity = "0"}, 50);
  setTimeout(() => { modalback_e.style.display = "none" }, 300);
  setTimeout(() => { edit.style.opacity = "100" }, 0);
}

edit.addEventListener( "click", openEditEvent );

function openEditEvent() {
  openEdit();
  setTimeout(() => {
    close.addEventListener( "click", closeEditEvent );
    btn_close.addEventListener( "click", closeEditEvent );;
  }, 20);
}

function closeEditEvent() {
  setTimeout(() => {
    close.removeEventListener( "click", closeEditEvent );
    btn_close.removeEventListener( "click", closeEditEvent );
    edit.addEventListener( "click", openEditEvent );
  }, 20);
  closeEdit();
}


$('.edit_book').click(function(){

  $('body').css("overflow", "hidden");
  $('#main').css("overflow", "hidden");
});

$('.info_overlay_left').click(function(){
  $('.rows_mob').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#main').css("overflow", "visible");
  $('body').css("overflow", "visible");
});

$('.modal_close').click(function(){
  $('.rows_mob').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#main').css("overflow", "visible");
});

$('.modal_button_cancel').click(function(){
  $('.rows_mob').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#main').css("overflow", "visible");
});

