
var btn = document.getElementById("add_book");
var btn_close = document.getElementsByClassName("modal_button_cancel")[0];
var modalback = document.getElementsByClassName("modal_add_back")[0];
var modal = document.getElementsByClassName("modal_add")[0];
var close = document.getElementsByClassName("modal_close")[0];
var boxes = document.getElementsByClassName("boxes")[0];

// FUNCTIONS

function openModal() {
  modalback.style.display = "block";
  setTimeout(() => { modalback.style.opacity = "1"}, 20);
  setTimeout(() => { modal.style.height = "100%" }, 0);
  setTimeout(() => { btn.style.opacity = "0%" }, 0);
  setTimeout(() => { boxes.style.opacity = "0%" }, 0);
}

function closeModal() {
  setTimeout(() => { modal.style.height = "0" }, 50);
  setTimeout(() => { modalback.style.opacity = "0"}, 50);
  setTimeout(() => { modalback.style.display = "none" }, 300);
  setTimeout(() => { btn.style.opacity = "100" }, 0);
  setTimeout(() => { boxes.style.opacity = "100%" }, 0);
}

btn.addEventListener( "click", openModalEvent );

function openModalEvent() {
  openModal();
  setTimeout(() => {
    close.addEventListener( "click", closeModalEvent );
    btn_close.addEventListener( "click", closeModalEvent );;
  }, 20);
}

function closeModalEvent() {
  setTimeout(() => {
    close.removeEventListener( "click", closeModalEvent );
    btn_close.removeEventListener( "click", closeModalEvent );
    btn.addEventListener( "click", openModalEvent );
  }, 20);
  closeModal();
}




$('#add_book').click(function(){
  $('.rows').css("overflow", "hidden");
  $('#book_list').css("overflow", "hidden");
});

$('.info_overlay_left').click(function(){
  $('.rows').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#book_list').css("overflow", "visible");
});

$('.modal_close').click(function(){
  $('.rows').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#book_list').css("overflow", "visible");
});

$('.modal_button_cancel').click(function(){
  $('.rows').css("overflow", "visible");
  $('body').css("overflow", "visible");
  $('#book_list').css("overflow", "visible");
});

