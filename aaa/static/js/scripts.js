

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




/* ++++++++++ LOAD MORE ++++++++++ */
  
// var _current_item = $('.single_content').length
// console.log(_current_item);
const loadBtn = document.getElementById('loadBtn');
const spinner = document.getElementById('spinner');
const total = JSON.parse(document.getElementById('json-total').textContent);
const alert = document.getElementById('alert');

function loadmorePost() {
    var _current_item = $('.single_content').length
    const content_container = document.getElementById("content");
    $.ajax({
        url: '{% url "load" %}',
        type: 'GET',
        data: {
            'offset': _current_item
        },
        beforeSend: function () {
            loadBtn.classList.add('not_visible');
            spinner.classList.remove('not_visible');
        },
        success: function (response) {
            const data = response.groups
            spinner.classList.add('not_visible')
            data.map(group => {
                console.log(group.name);
                content_container.innerHTML += 
                `<div class="single_content">
                  <h3>${group.name}</h3>
                  <h4>${group.description}</h4>
                </div>`
            })
            if (_current_item == total) {
                alert.classList.remove('not_visible');
            } else {
                loadBtn.classList.remove('not_visible');
            }
        },
        error: function (err) {
            console.log(err);
        },
    });
}
loadBtn.addEventListener('click', () => {
    loadmorePost()
});



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



