const post_content = document.getElementById('post_content')
const id_message = document.getElementById('id_message')
const id_group = document.getElementById('id_group')
const id_image = document.getElementById('id_image')

const post_form = document.getElementById('post_form')
const url_delete = window.location.href + "/delete/"



/////////////////////////////////////////
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




console.log('hello world')
console.log(window.location)


////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff





let newPostId = null
post_form.addEventListener('submit', e => {
	e.preventDefault(

	$.ajax({
		type: 'POST',
		url: '',
		data: {
			// how to access the form token
			'csrfmiddlewaretoken': csrf[0].value,
			'message': id_message.value,
			'group': id_group.value,
			'image': id_image.value,
		},
		success: function(response) {
			console.log(response)
			newPostId = response.id
			// places post at top of post_content
			post_content.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
					<div id="post_list">
					  <div class="post3">

					    <div class="post_message_group">

					      <div class="button_group">
					        <div class="post_message">
					        <a href="${url}${response.group}"><h3>${response.message}</h3></a>
					        </div>
					      </div>

						    <span class="username">
						      <a href="${url}${response.user}">@${response.user}</a> posted this just now
								</span>

							</div>

					  </div>
					</div>
				`
			)
			$('#modal_form').modal('hide')
			//window.location = document.location
			handle_alerts('message_success', 'New post added')
			document.getElementById("post_form").reset()
			//window.location.reload();
			window.location = document.referrer;
		},
		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		}
	}))
})









