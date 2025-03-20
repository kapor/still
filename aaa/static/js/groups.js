const group_list = document.getElementById('group_list')
const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')

const url = window.location.href



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
					<a href="${url}${item.slug}">
				    <div class="card">

				      
				        <h3 class='name'>${item.name}</h3>
				      
				     
				      <div class="card_lower">
				        <div class="description">
							${item.description}
				        </div>

				      </div>

				    </div>
					</a>
					`
				});
			}, 100)
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

load_button.addEventListener('click', () => {
	loader.classList.remove('not_visible')
	visible += 40
	getData()
})

getData()
