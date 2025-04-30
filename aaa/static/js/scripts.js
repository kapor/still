

const alert_box = document.getElementById('alert_box')


const handle_alerts = (type, msg) => {
    alert_box.innerHTML =
    `
      <div class="${type}">
        ${msg}
      </div>
    `
}











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
    //document.getElementById("avatar_lockup").style.height = "24px";
    // document.getElementById("user_label").style.lineHeight = "24px";
    //document.getElementById("logo").style.height = "24px";
  } else {
    document.getElementById("nav_bar").style.margin = "0px 0px";
    document.getElementById("nav_bar").style.boxShadow = "0px 0px 0px #CCC";
    document.getElementById("nav_bar").style.padding="20px 32px";
    document.getElementById("navbar_right").style.lineHeight = "48px";
    document.getElementById("navbar_left").style.lineHeight = "48px";
    document.getElementById("logout").style.height = "48px";
    //document.getElementById("avatar_lockup").style.height = "48px";
    // document.getElementById("user_label").style.lineHeight = "48px";
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



////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET

/*
const login_form = document.getElementById('login_form');
const login_cancel_button = document.getElementById('login_cancel_button');
const login_close_x = document.getElementById('login_close_x');
const modal_login = document.getElementById('modal_login'); 

login_cancel_button.addEventListener('click', function() {
  document.getElementById('login_form').reset();
});

login_close_x.addEventListener('click', function() {
  document.getElementById('login_form').reset();
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    document.getElementById('login_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_login) {
    login_form.reset();
  } else {
    // Do nothing
  }
});


*/
