const post_content = document.getElementById('post_content')
const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')

const url = window.location.href

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
					<div id="post_list">
					  <div>
					    <div class="post_message_group">
					      <div class="button_group">
					        <div class="post_message">
					        <a href="${url}${item.slug}"><h3>${item.message}</h3></a>
					        </div>
					      </div>
					    </div>    

					    <span class="username">
					      <a href="${url}${item.user.username}">${item.user.username}</a>posted in
					    <span class="group-name">
					    <a href="${url}${item.group.name}">${item.group.name}</a>
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
/*			post_content.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
					<div id="post_list">
					  <div>
					    <div class="post_message_group">
					      <div class="button_group">
					        <div class="post_message">
					        <a href="${url}/user/${item.user}"><h3>${item.message}</h3></a>
					        </div>
					      </div>
					    </div>    

					    <span class="username">
					      <a href="${url}${item.user.username}">${item.user.username}</a>posted in
					    <span class="group-name">
					    <a href="${url}${item.group.name}">${item.group.name}</a>
					    </span>${item.created_at}</span>
					  </div>
					</div>
				`
			)*/
			$('#post_form').modal('hide')
			handle_alerts('message_success', 'New post added')
			document.getElementById("post_form").reset()
		},
		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		}
	})
})









/*load_button.addEventListener('click', () => {
	loader.classList.remove('not_visible')
	visible += 40
	getData()
})

getData()*/
