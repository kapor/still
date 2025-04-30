// GROUPS
const back = document.getElementById('back_button')
const url = window.location.href + "data/"

const post_content = document.getElementById('post_content')
const id_message = document.getElementById('id_message')
const id_group = document.getElementById('id_group')
const id_image = document.getElementById('id_image')

const post_form = document.getElementById('post_form')
const url_delete = window.location.href + "/delete/"

const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('csrf', csrf[0].value)


console.log('detail')
console.log(window.location)

////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
// MESSAGE CONFIRMATION TIMEOUT



$(document).ready(function() {
    setTimeout(function() {
        $('#alert_box').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});

$(document).ready(function() {
    setTimeout(function() {
        $('.alert_error').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});


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
const deleted = localStorage.getItem('message')

if (deleted) {
	handle_alerts('alert_error', 'Post Deleted')
	localStorage.clear()
}



// like unlike post
const likeUnlikeChirp = () => {
	const like_unlike_form = [...document.getElementsByClassName('like_unlike_form')]
	like_unlike_form.forEach(form => form.addEventListener('submit', e => {
		//prevent default stops form submitting in favor of custom ajax
		e.preventDefault()
		//clicked form is being stored in the custom attribute 'data_form_id'
		const clickedId = e.target.getAttribute('data_form_id')
		const clickedButton = document.getElementById(`like_unlike_chirp_${clickedId}`)

		$.ajax({
			type: 'POST',
			url: `/chirps/like_unlike/`,
			data: {
				//taken from https://docs.djangoproject.com/en/5.1/howto/csrf/
				'csrfmiddlewaretoken': csrftoken,
				'pk': clickedId,
			},
			success: function(response){
				console.log(response)
				clickedButton.textContent = response.liked ? 
				`Liked  | ${response.count}`
				: 
				`Like | ${response.count}`
			},
			error: function(error){
				console.log(error)
			}
		})
	}))
}



likeUnlikeChirp()





// like unlike post
const likeUnlikePost = () => {
	const like_unlike_post_form = [...document.getElementsByClassName('like_unlike_post_form')]
	like_unlike_post_form.forEach(form => form.addEventListener('submit', e => {
		//prevent default stops form submitting in favor of custom ajax
		e.preventDefault()
		//clicked form is being stored in the custom attribute 'data_form_id'
		const clickedId = e.target.getAttribute('data_form_id')
		const clickedButton = document.getElementById(`like_unlike_post_${clickedId}`)

		$.ajax({
			type: 'POST',
			url: `/posts/like_unlike/`,
			data: {
				//taken from https://docs.djangoproject.com/en/5.1/howto/csrf/
				'csrfmiddlewaretoken': csrftoken,
				'pk': clickedId,
			},
			success: function(response){
				console.log(response)
				clickedButton.textContent = response.liked ? 
				`Unlike  | ${response.count}`
				: 
				`Like | ${response.count}`
			},
			error: function(error){
				console.log(error)
			}
		})
	}))
}



likeUnlikePost()








////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const form = document.getElementById('post_form');
const cancel_button = document.getElementById('cancel_button');
const close_x = document.getElementById('close_x');
const modal_dialog = document.getElementById('modal_dialog'); 

cancel_button.addEventListener('click', function() {
	document.getElementById('post_form').reset();
});

close_x.addEventListener('click', function() {
	document.getElementById('post_form').reset();
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    document.getElementById('post_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_dialog) {
    form.reset();
  } else {
  	// Do nothing
  }
});







form.addEventListener('submit', function(e) {
	e.preventDefault();
	const formData = new FormData(form);
	$.ajax({
		type: 'POST',
		url: '',
		data: formData,
		processData: false,
		contentType: false,
    	headers: {'X-CSRFToken': csrftoken},
		success: function(response) {
			likeUnlikePost()
			$('#modal_form').modal('hide')
			document.getElementById("post_form").reset()
			window.location.reload();
		},
		error: function(error) {
			console.log(error)
		}
	});
});




