const post_content = document.getElementById('post_content')
const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')

const url = window.location.href

const id_message = document.getElementById('id_message')
const id_group = document.getElementById('id_group')
const id_image = document.getElementById('id_image')

const post_form = document.getElementById('post_form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log('csrf', csrf[0].value)

const alert_box = document.getElementById('alert_box')



const handle_alerts = (type, msg) => {
    alert_box.innerHTML =
    `
      <div class="${type}">
        ${msg}
      </div>
    `
}






////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// load more

/*let visible = 20

const getData = () => {

	$.ajax({
		type: 'GET',
		url: `/posts/${visible}/`,
		success: function(response){
			console.log(response)
			///this is grabbing the response 'data' from the view "load_post"...
			const data = response.data
			setTimeout(()=> {
				loader.classList.add('not_visible')
				console.log(data)
				///...and looping it through an array to inject html into the #post_content div
				data.forEach(item => {
					post_content.innerHTML += 
					///use backticks to inject html
					`
					<div class="post3" id="post_list">
						<div>
					    <div class="post_message_group">
					      <div class="button_group">
					        <div class="post_message">
					        <a href="#"><h3>${item.message}</h3></a>
					        </div>
					      </div>
					    </div>    

					    <span class="username">
					      <a href="#">${item.user}</a> posted in
					    <span class="group-name">
					    <a href="#">${item.group}</a>
					    </span>${item.created_at}</span>
						</div>
					</div>
					`
				});
			}, 50)
			console.log(response.size)
			if (response.size === 0) {
				nomore.textContent = 'Nothing yet'
			}
			else if (response.size <= visible) {
				load_button.classList.add('not_visible')
				nomore.textContent = 'the end'
			}
		},
		error: function(error){
			console.log(error) 
		}
	})

}*/



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff

post_form.addEventListener('submit', e => {
	e.preventDefault()

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
			// places post at top of post_content
			post_content.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
					<div id="post_list">
					  <div class="post3">

					    <div class="post_message_group">

					      <div class="button_group">
					        <div class="post_message">
					        <a href="/user/${response.user}"><h3>${response.message}</h3></a>
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
			handle_alerts('message_success', 'New post added')
			document.getElementById("post_form").reset()
		},
		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		}
	})
})

/////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const form = document.getElementById('post_form');
const cancel_button = document.getElementById('cancel_button');
const close_x = document.getElementById('close_x');
const modal_dialog = document.getElementById('modal_dialog'); 

cancel_button.addEventListener('click', function() {
	form.reset();
});

close_x.addEventListener('click', function() {
	form.reset();
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






