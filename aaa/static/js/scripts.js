
// OVERLAY

document.addEventListener('DOMContentLoaded', function(){

  const overlay = document.getElementById('overlay');
  function overlayToggle() {
    overlay.classList.toggle('overlay-on');
  }

  const clickArea = document.getElementsByClassName('overlay-event');
  for(let i = 0; i < clickArea.length; i++) {
    clickArea[i].addEventListener('click', overlayToggle, false);
  }
	

  function stopEvent(event) {
    event.stopPropagation();
  }
  const overlayInner = document.getElementById('overlay-inner');
  overlayInner.addEventListener('click', stopEvent, false);
  
}, false);




// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
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
}

