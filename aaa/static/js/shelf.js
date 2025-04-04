const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')

const shelf_table = document.getElementById('shelf_table')

const title = document.getElementById('id_title')
const author = document.getElementById('id_author')
const year = document.getElementById('id_year')
const type = document.getElementById('id_type')
const publisher = document.getElementById('id_publisher')
const artist = document.getElementById('id_artist')
const quality = document.getElementById('id_quality')
const price = document.getElementById('id_price')
const location_ = document.getElementById('id_location')
const tags = document.getElementById('id_tags')
const weight = document.getElementById('id_weight')
const pages = document.getElementById('id_pages')
const isbn = document.getElementById('id_isbn')
const description = document.getElementById('id_description')
const notes = document.getElementById('id_notes')
const image = document.getElementById('id_image')


const url_data = window.location.href + "data"
const edit = document.getElementById('shelf_edit')
const shelf_detail = document.getElementById('shelf_detail')
const remove = document.getElementById('shelf_delete')
const data_top = document.getElementById('shelf_data_top')
const data_bottom = document.getElementById('shelf_data_bottom')


/////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const form = document.getElementById('shelf_form');
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
    document.getElementById('shelf_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_dialog) {
    form.reset();
  } else {
  	// Do nothing
  }
});


////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff (adding an item)

document.getElementById('shelf_form').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent the default form submission

  fetch(this.action, {
    method: 'POST',
    body: new FormData(this),
    headers: {
      'X-Requested-With': 'XMLHttpRequest', // Identify as AJAX request
    }
  })
  .then(response => {
    if (response.ok) {
    	handle_alerts('message_success', 'New item added')
      window.location.reload();
      handle_alerts('message_success', 'New item added') // Reload the page on success
    } else {
      // Handle errors, e.g., display an error message
      console.error('Error submitting form');
    }
  })
  .catch(error => {
    console.error('Network error:', error);
  });
});

/*shelf_form.addEventListener('submit', e => {
	e.preventDefault()

		$.ajax({

			type: 'POST',
			url: '',
			processData: true,
			contentType: false,
			datatype: "JSON",
			data: {
				// how to access the form token
				'csrfmiddlewaretoken': csrf[0].value,
				'title': id_title.value,
				'author': id_author.value,
				'year': id_year.value,
				'type': id_type.value,
				'publisher': id_publisher.value,
				'artist': id_artist.value,
				'quality': id_quality.value,
				'price': id_price.value,
				'location_': id_location.value,
				'genre': id_author.value,
				//'tags': id_tags.value,
				'weight': id_weight.value,
				'pages': id_pages.value,
				'isbn': id_isbn.value,
				'description': id_description.value,
				'notes': id_notes.value,
				//'image': id_image.value,
			},


			success: async function(response) {

				console.log(response)
				// places post at top of group_list
				shelf_table.insertAdjacentHTML('afterbegin',
				///use backticks to inject html
					`
						<tr id="shelf_row">
							<td>${response.year}</td>
							<td>${response.title}</td>
							<td>${response.author}</td>
							<td>ID</td>
							<td>User</td>
							<td>
								<div class=cover_crop>
									<img class="photo_blank" src="/media/shelves/blank.jpg">
								</div>
							</td>
						</tr>
					`
				)

				$('#modal_form').modal('hide')
				handle_alerts('message_success', 'New item added')
				document.getElementById("group_form").reset()
		  },

			error: function(error) {
				console.log(error)
				handle_alerts('message_success', 'Something went wrong...')
			}

	})
});*/







////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff (editing an item)



$.ajax({
	type: 'GET',
	url: url_data,
	success: function(response) {
		console.log(response)
		const data = response.data

		// another way to add permissions is to compare the "user" who authored the item and the user who's currently "logged_in"
/*		if (data.logged_in !== data.user ) {
			console.log('different')
		} else {
			console.log('the_same')
		}
*/
/*		const label_info = document.createElement('div')
		title.setAttribute('class', 'label_info')
		shelf_detail.appendChild(data_top)
		shelf_detail.appendChild(data_bottom)*/


		loader.classList.add('not_visible')
	},
	error: function(error) {
		console.log(error)
	}
})











function getCookie(name) {
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



