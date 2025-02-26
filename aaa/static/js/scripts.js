

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
  document.getElementById('modal2').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
  }
});

document.getElementById('btn_modal').addEventListener('click', function() {
  document.getElementById('underlay').classList.add('is_visible');
  document.getElementById('modal2').classList.add('is_visible');
  document.getElementById('underlay').style.display = "block";
  document.getElementById('modal2').style.display = "flex";
  document.body.style.overflow = "hidden"; 
  document.body.style.height = "100%"; 
});

document.getElementById('close_btn').addEventListener('click', function() {
  document.getElementById('underlay').classList.remove('is_visible');
  document.getElementById('modal2').classList.remove('is_visible');
  document.getElementById('underlay').style.display = "none";
  document.getElementById('modal2').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
});
document.getElementById('underlay').addEventListener('click', function() {
  document.getElementById('underlay').classList.remove('is_visible');
  document.getElementById('modal2').classList.remove('is_visible');
  document.getElementById('underlay').style.display = "none";
  document.getElementById('modal2').style.display = "none";
  document.body.style.overflow = "auto";
  document.body.style.height = "auto";
});

