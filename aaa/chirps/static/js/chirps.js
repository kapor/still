const chirp_content = document.getElementById('chirp_content')
const id_message = document.getElementById('id_message')
const id_group = document.getElementById('id_group')
const id_image = document.getElementById('id_image')

const chirp_form = document.getElementById('chirp_form')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('csrf', csrf[0].value)

const url = window.location.href




////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const form = document.getElementById('chirp_form');
const cancel_button = document.getElementById('cancel_button');
const close_x = document.getElementById('close_x');
const modal_dialog = document.getElementById('modal_dialog'); 

cancel_button.addEventListener('click', function() {
	document.getElementById('chirp_form').reset();
});

close_x.addEventListener('click', function() {
	document.getElementById('chirp_form').reset();
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    document.getElementById('chirp_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_dialog) {
    form.reset();
  } else {
  	// Do nothing
  }
});



console.log('hello world')
console.log(window.location)


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



likeUnlikeChirp()








////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
// form stuff


/*let newPostId = null
chirp_form.addEventListener('submit', e => {
	e.preventDefault()

	$.ajax({
		type: 'POST',
		url: '/chirps/',
		data: {
			// how to access the form token
			'csrfmiddlewaretoken': csrf[0].value,
			'message': id_message.value,
			'group': id_group.value,
			//'image': id_image.value,
		},
		success: function(response) {
			console.log(response)
			newPostId = response.id
			// places post at top of chirp_content
			chirp_content.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
					<div id="post_list">
					  <div class="post6">

					    <div class="post_message_group">

					      <div class="button_group">
					        <div class="post_message">
					        <a href="${url}${response.group}"><h3>${response.message}</h3></a>
					        </div>
					      </div>

						    <span class="username">
						      <a href="${url}${response.user}">@${response.user}</a> posted this in ${response.group}
								</span>

							</div>

					  </div>
					</div>
				`
			)
			likeUnlikeChirp()
			//$('#modal_form').modal('hide')
			//window.location = document.location
			//handle_alerts('message_success', 'New post added')
			document.getElementById("chirp_form").reset()
			window.location.reload();
			//window.location = document.referrer;
		},
		error: function(error) {
			console.log(error)
			//handle_alerts('message_success', 'Something went wrong...')
		}
	})
})*/


form.addEventListener('submit', function(e) {
	e.preventDefault();
	const formData = new FormData(form);
	$.ajax({
		type: 'POST',
		url: '/chirps/',
		data: formData,
		processData: false,
		contentType: false,
    	headers: {'X-CSRFToken': csrftoken},
		success: function(response) {
			likeUnlikeChirp()
			// document.getElementById("chirp_form").reset()
			window.location.reload();
		},
		error: function(error) {
			console.log(error)
		}
	});
});








