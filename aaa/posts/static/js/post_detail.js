// POSTS
// EDIT / DELETE
const url_update = window.location.href + "/update/"
const url_delete = window.location.href + "/delete/"
const url = window.location.href + "/data/"

const form_edit = document.getElementById('edit_form')
const form_delete = document.getElementById('delete_form')

const back = document.getElementById('back_button')
const edit = document.getElementById('edit_button')
const remove = document.getElementById('delete_button')
const cancel = document.getElementById('cancel_button')
const close = document.getElementById('close_x')

const post_list = document.getElementById('post_list')

const post_message = document.getElementById('id_message')
const post_group = document.getElementById('id_group')
const post_image = document.getElementById('id_image')

const modal_content = document.getElementsByClassName('modal_content')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('csrf', csrf[0].value)



// BACK BUTTON
back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})


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

		post_message.value = data.message
		post_group.value = data.group
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
			success: function(response) {
				if (response.status === 'success') {
					// $('#modal_form').modal('hide')
					// document.getElementById("post_form").reset()
					// likeUnlikePost()
					// window.location = document.referrer;
					history.go(0)
					// history.back(-1).location.reload();
					// localStorage.setItem('message', post_message.value)
					// handle_alerts('alert_error', 'Post Deleted')*/
				} else {
					// console.log(error)
					handle_alerts('alert_error', 'An error occurred')
				}
			},
			error: function(error) {
				console.log(error)
				handle_alerts('alert_error', 'An error occurred')
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
	const success_url = "posts/"

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
			handle_alerts('alert_error', 'An error occurred')
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







