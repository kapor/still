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


const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('csrf', csrf[0].value)

const url = window.location.href


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



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff (adding an item)




form.addEventListener('submit', function(e) {
	e.preventDefault();
	const formData = new FormData(form);
	$.ajax({
		type: 'POST',
		url: '/shelf/',
		enctype: 'multipart/form-data',
		data: formData,
		processData: false,
		contentType: false,
    headers: {'X-CSRFToken': csrftoken},

		success: function(response) {
			console.log("success")
			$('#modal_form').modal('hide')
			document.getElementById("shelf_form").reset()
			window.location.reload();
			// handle_alerts('message_success', 'New item added')
		},

		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		}
	});
});
























