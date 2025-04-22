

const alert_box = document.getElementById('alert_box')


const handle_alerts = (type, msg) => {
    alert_box.innerHTML =
    `
      <div class="${type}">
        ${msg}
      </div>
    `
}

$(document).ready(function() {
    setTimeout(function() {
        $('.alert_error').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});



// When the user scrolls down 80px from the top of the document, resize the navbar

window.onscroll = function() {scrollNav()};
function scrollNav() {
  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    document.getElementById("nav_bar").style.margin = "0px 0px";
    document.getElementById("nav_bar").style.boxShadow = "0px 2px .10px #CCC";
    document.getElementById("nav_bar").style.padding="20px 24px";
    document.getElementById("navbar_right").style.lineHeight = "24px";
    document.getElementById("navbar_left").style.lineHeight = "24px";
    document.getElementById("logout").style.height = "24px";
    //document.getElementById("logo").style.height = "24px";
  } else {
    document.getElementById("nav_bar").style.margin = "0px 0px";
    document.getElementById("nav_bar").style.boxShadow = "0px 0px 0px #CCC";
    document.getElementById("nav_bar").style.padding="20px 32px";
    document.getElementById("navbar_right").style.lineHeight = "48px";
    document.getElementById("navbar_left").style.lineHeight = "48px";
    document.getElementById("logout").style.height = "48px";
    //document.getElementById("logo").style.height = "48px";
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







// MODAL IMAGE ENLARGE
document.addEventListener('DOMContentLoaded', function() {
const image_small = document.getElementById('modal_image_thumb');
const image_large = document.getElementById('modal_image_large');
const modal_form = document.getElementById('modal_form');
const shader = document.getElementById('shader');

image_small.style.cursor = "pointer";
image_large.style.cursor = "pointer";
shader.style.cursor = "pointer";

image_small.addEventListener('click', () => {
image_large.classList.remove('not_visible')
shader.style.display = "block";
});

image_large.addEventListener('click', () => {
image_large.classList.add('not_visible')
shader.style.display = "none";
});

shader.addEventListener('click', () => {
image_large.classList.add('not_visible')
shader.style.display = "none";
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    image_large.classList.add('not_visible')
    shader.style.display = "none";
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_form) {
    image_large.classList.add('not_visible')
    shader.style.display = "none";
  } else {
    // Do nothing
  }
});
})

/*image_small.forEach(header => {
    header.addEventListener('click', () => {
        // Deactivate all tabs and content
        tabHeaders.forEach(h => h.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));

        // Activate the clicked tab and corresponding content
        header.classList.add('active');
        const tabId = header.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});
*/




