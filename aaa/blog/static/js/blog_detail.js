// BLOG
// EDIT / DELETE
const url_update = window.location.href + "update/"
const url_delete = window.location.href + "delete/"
const url = window.location.href + "data/"

const form_edit = document.getElementById('edit_form')
const form_delete = document.getElementById('delete_form')

const back = document.getElementById('back_button')
const edit = document.getElementById('edit_button')
const remove = document.getElementById('delete_button')
const cancel = document.getElementById('cancel_button')
const close = document.getElementById('close_x')

const post_list = document.getElementById('post_list')

const post_title = document.getElementById('id_title')
const post_message = document.getElementById('id_message')
const post_group = document.getElementById('id_group')
const post_image = document.getElementById('id_image')
const post_tags = document.getElementById('id_tags')

const modal_content = document.getElementsByClassName('modal_content')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('csrf', csrf[0].value)



/*// BACK BUTTON
back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})*/


console.log('detail')
console.log(window.location)






////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// DETAIL VIEW 

$.ajax({
	type: 'GET',
	url: url,
	success: function(response) {
		console.log(response)
		const data = response.data

		post_title.value = data.title
		//post_group.value = data.group
		post_message.value = data.message
		// post_tags.value = data.tags
		// post_image.value = data.image


	},
	error: function(error) {
		console.log(error)
	}

})



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// DETAIL EDIT

$(document).ready(function() {
	$('#edit_form').on('submit', function(e) {
		e.preventDefault();

		var formData = new FormData(this);

		$.ajax({
			type: 'POST',
			url: url_update,
			data: formData,
			contentType: false,
			processData: false,
            headers: {'X-CSRFToken': csrftoken},
			success: function(response) {
				window.location.reload();
			},
			error: function(error) {
				console.log(error)
				handle_alerts('message_success', 'An error occurred')
			}
		});
	});
});





////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// DELETE STUFF

form_delete.addEventListener('submit', e=> {
	e.preventDefault()

	const message = document.getElementById('message')
	const success_url = "blog/"

	$.ajax({
		type: 'POST',
		url: url_delete,
		data: {
			'csrfmiddlewaretoken': csrf[0].value,
		},
		success: function(response) {
			// history.go(-2)
			window.location = document.referrer;
			// console.log(response)
			// history.back(-2).location.reload();
			// window.location.href = window.location.origin
			// localStorage.setItem('message', post_message.value)
			// handle_alerts('alert_error', 'Post Deleted')
		},
		error: function(error) {
			console.log(error)
			//handle_alerts('alert_error', 'An error occurred')
		}

	})

})


////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////LIKE UNLIKE STUFF

// like unlike token https://docs.djangoproject.com/en/5.1/howto/csrf/
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// handles success messaging for deleted post
const deleted = localStorage.getItem('title')

if (deleted) {
	handle_alerts('alert_error', 'Post Deleted')
	localStorage.clear()
}






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
