
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



// LOAD MORE PAGINATION

// var _current_item = $('.single_content').length
// console.log(_current_item);
const loadBtn = document.getElementById('btn');
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
            loadBtn.classList.add('not-visible');
            spinner.classList.remove('not-visible');
        },
        success: function (response) {
            const data = response.groups
            spinner.classList.add('not-visible')
            data.map(group => {
                console.log(group.title);
                content_container.innerHTML += `<div class="single_content border border-success mt-2 pl-2">
                                                    <h3>${group.name}</h3>
                                                    <p>${group.description}</p>
                                                </div>`
            })
            if (_current_item == total) {
                alert.classList.remove('not-visible');
            } else {
                loadBtn.classList.remove('not-visible');
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

