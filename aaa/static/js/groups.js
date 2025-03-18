const group_box = document.getElementById('group_box')

const group_form = document.getElementById('group_form')
const group_name = document.getElementById('group_name')
const group_description = document.getElementById('group_description')
// this is how to access the form token
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const alert_box = document.getElementById('alert_box')
console.log('csrf', csrf[0].value)





////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff

group_form.addEventListener('submit', e => {
	e.preventDefault()

	$.ajax({
		type: 'POST',
		url: '/groups/',
		data: {
			// how to access the form token
			'csrfmiddlewaretoken': csrf[0].value,
			'name': group_name.value,
			'description': group_description.value
		},
		success: function(response) {
			console.log(response)
			// places post at top of group_box
			group_box.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
			`
		    <div>
			    <div class="card">
					<h3 class='name'>${response.name}</h3>
				</div>
				<div class="card_lower">
					<div class="description">
						${response.name}
					</div>
					<div class="group_count">
						<div class="group_count_row">
						Members: 
						<span class="badge">0</span>
					</div>
					<div class="group_count_row">
						Posts: 
						<span class="badge">0</span>
					</div>
				</div>
		    </div>

			`
			)
			$('#add_post_modal').modal('hide')
			group_form.reset()
		},
		error: function(error) {
			console.log(error)
		}
	})

})









////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// get data with ajax


// 1. jquery ajax method

/*	const url = 'https://swapi.dev/api/people'

	$.ajax({
		type: 'GET',
		url: url,
		success: function(response){
			console.log('jquery ajax', response)
		},
		error: function(error){
			console.log(error)
		}

	})
*/


// 2. XMLHttpRequest

/*	const req = new XMLHttpRequest()

	req.addEventListener('readystatechange', ()=> {
		if(req.readyState==4){
			console.log('xhttp', JSON.parse(req.responseText))
		}
	})

	req.open('GET', url)
	req.send()

*/



// 3. Fetch Method

/*	fetch(url)
	.then(resp => resp.json()).then(data=>console.log('fetch', data))
	.catch(err => console.log(err))

*/





////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
//innerhtml success example

$.ajax({
	type: 'GET',
	url: '/posts/',
	success: function(response){
		click_header.innerHTML = "GET / <b>POSTS</b> / HTTP / 1.1 <b>200</b>"
	},
	error: function(error){
		click_header.innerHTML = "GET / <b>POST</b> / HTTP / 1.1 <b>404</b>"
	}
})

click_header.addEventListener('click', ()=> {
	click_header.innerHTML = "<b>YOU JUST CLICKED ME</b>"
})

















