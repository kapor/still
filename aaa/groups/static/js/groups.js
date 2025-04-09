const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')



const group_list = document.getElementById('group_list')

const id_name = document.getElementById('id_name')
const id_description = document.getElementById('id_description')
const id_slug = document.getElementById('id_slug')
const id_member = document.getElementsByClassName('leave_join')

const modal_form = document.getElementById('modal_form')








////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// load more
let visible = 40

const getData = () => {

	$.ajax({
		type: 'GET',
		url: `/groups/${visible}/`,
		success: function(response){
			console.log(response)
			///this is grabbing the response 'data' from the view "load_post"...
			const data = response.data
			setTimeout(()=> {
				loader.classList.add('not_visible')
				console.log(data)
				///...and looping it through an array to inject html into the #group_list div
				data.forEach(item => {
					group_list.innerHTML += 
					///use backticks to inject html
					`
					${item.member ? `
					<a href="${url}${item.slug}">
				    <div class="card" style="background-color:#75ffba">
				    <h3 class='name'>${item.name}</h3>
					<div class="leave_join">Member</div>
				     
				      <div class="card_lower">
						${item.description ? 
							`<div class="description">${item.description}</div>`: 
							`<div class="description">No description yet.</div>`}

				      </div>

				    </div>
					</a>
					`
						: 
					`
					<a href="${url}${item.slug}">
				    <div class="card">
				    <h3 class='name'>${item.name}</h3>
				     
				      <div class="card_lower">
						${item.description ? 
							`<div class="description">${item.description}</div>`: 
							`<div class="description">No description yet.</div>`}

				      </div>

				    </div>
					</a>
					`}
					`
				});
			}, 100)

			setTimeout(()=> {
				endbox.classList.remove('not_visible')
			}, 150)

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

}



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff

modal_form.addEventListener('submit', e => {
	e.preventDefault()

	$.ajax({
		type: 'POST',
		url: '',
		data: {
			// how to access the form token
			'csrfmiddlewaretoken': csrf[0].value,
			'name': id_name.value,
			'description': id_description.value
		},
		success: function(response) {
			console.log(response)
			// places post at top of group_list
			group_list.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
				<a href="${url}${response.slug}">
			    <div class="card" style="background-color:#f6ceff">
			    <h3 class='name'>${response.name}</h3>
				<div class="leave_join">Just added</div>
			     
			      <div class="card_lower">
					${response.description ? 
						`<div class="description" style="color:black">${response.description}</div>`: 
						`<div class="description" style="color:black">No description yet.</div>`}

			      </div>

			    </div>
				</a>
				`
			)
			$('#modal_form').modal('hide')
			handle_alerts('message_success', 'New post added')
			document.getElementById("group_form").reset()
		},
		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		}
	})
})





/////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const cancel_button = document.getElementById('cancel_button');
const form = document.getElementById('group_form');
const close_x = document.getElementById('close_x');
const modal_dialog = document.getElementById('modal_dialog'); 

cancel_button.addEventListener('click', function() {
	form.reset();
	console.log("hello")
});

close_x.addEventListener('click', function() {
	form.reset();
	console.log("two")
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    document.getElementById('group_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_dialog) {
    form.reset();
	console.log("three")
  } else {
  	// Do nothing
  }
});



load_button.addEventListener('click', () => {
	loader.classList.remove('not_visible')
	visible += 40
	getData()
})

getData()
