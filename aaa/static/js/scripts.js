const csrf = document.getElementsByName('csrfmiddlewaretoken')
const url = window.location.href
const back = document.getElementById('back_button')

const alert_box = document.getElementById('alert_box')


const handle_alerts = (type, msg) => {
    alert_box.innerHTML =
    `
      <div class="${type}">
        ${msg}
      </div>
    `
}

back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})


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






/* ++++++++++ SCROL TOP ++++++++++ */


function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

/* ++++++++++ CONFIRMATION PROMPT ++++++++++ */


function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 


/* ++++++++++ MESSAGE CONFIRMATION TIMEOUT ++++++++++ */


$(document).ready(function() {
    setTimeout(function() {
        $('.message_success').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});



/* ++++++++++ ESCAPE KEY TO CLOSE MODAL ++++++++++ */

/*document.addEventListener('keydown', function(event) {
    if (event.keyCode === 27) {
        const modal = document.querySelector('.modal'); // Replace '.modal' with the actual selector of your modal
        if (modal && modal.style.display !== 'none') {
            const closeButton = modal.querySelector('#modal_close'); // Replace '.close-button' with the actual selector of your close button
            if (closeButton) {
                closeButton.click();
            }
        }
    }
});*/


/* ++++++++++ DISABLE SCROLLBAR ++++++++++ */

/*$('.modal_underlay').click(function(){
    $('.body_block').css("overflow", "visible");
    $('body').css("overflow", "visible");
});

$('#modal_close').click(function(){
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
*/


////////////////////////////////











