console.log('profiles')
console.log(window.location)



// MODAL IMAGE ENLARGE
/*document.addEventListener('DOMContentLoaded', function() {
const image_small = document.getElementById('profile_crop_detail');
const image_large = document.getElementById('modal_image_large');
const modal_form = document.getElementById('modal_form');
const shader = document.getElementById('shader');
const info_image_large = document.getElementById('info_image_large');
const bodyElement = document.body;

image_small.style.cursor = "pointer";
image_large.style.cursor = "pointer";
shader.style.cursor = "pointer";

image_small.addEventListener('click', () => {
	image_large.classList.remove('not_visible')
	bodyElement.classList.add('modal_open')
	info_image_large.style.width = "600px"
	info_image_large.style.height = "auto"
	modal_image_large.style.minHeight = "100%"
	modal_image_large.style.minWidth = "100%"
	shader.style.display = "block";
});

image_large.addEventListener('click', () => {
	image_large.classList.add('not_visible')
	bodyElement.classList.remove('modal_open')
	shader.style.display = "none";
});

shader.addEventListener('click', () => {
	image_large.classList.add('not_visible')
	bodyElement.classList.remove('modal_open')
	shader.style.display = "none";
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    image_large.classList.add('not_visible')
	bodyElement.classList.remove('modal_open')
    shader.style.display = "none";
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_form) {
    image_large.classList.add('not_visible')
 	bodyElement.classList.remove('modal_open')
    shader.style.display = "none";
  } else {
    // Do nothing
  }
});
})*/


const uploaded_image = document.getElementById('uploaded_image')
const form = document.getElementById('profile_form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const bioInput = document.getElementById('id_bio')
const imageInput = document.getElementById('id_image')
const clear = document.getElementById('picture_clear_id')
const msg = document.getElementById('msg')
const change_photo = document.getElementById('change_photo')
const submit_button = document.getElementById('submit_button')
const clear_container = document.getElementById('clear_container')
const info_image_large = document.getElementById('info_image_large')







form.addEventListener('submit', function(e) {
	e.preventDefault();

	const formData = new FormData(form);
	formData.append('csrfmiddlewaretoken', csrf[0].value)
	formData.append('bio', bioInput.value)
	formData.append('picture', imageInput.files[0])

	$.ajax({
		type: 'POST',
		url: '',
		enctype: 'multipart/form-data',
		data: formData,
		headers: {'X-CSRFToken': csrf, 'X-Requested-With': 'XMLHttpRequest', },

		success: function(response) {

			console.log(response)
			uploaded_image.innerHTML = `
				<img src="${response.picture}" id="info_image_large">
			`;

			//clear.checked = false;
			submit_button.className = "button_secondary";
			submit_button.setAttribute('disabled', '');
			submit_button.setAttribute('style', 'cursor: not-allowed;');
			change_photo.innerHTML = `
				Change Photo
			`
			bioInput.value = response.bio
			$('#alert_box').show().html();
			$('#alert_box').delay(5000).fadeOut(); 
			handle_alerts('message_success', 'Profile Updated')
			// $('#modal_form').modal('hide')
			// document.getElementById("blog_form").reset()
			// window.location.reload();
			// msg.classList.remove('not_visible')
		},

		error: function(error) {
			console.log(error)
			handle_alerts('message_success', 'Something went wrong...')
		},
		processData: false,
		contentType: false,
		cache: false,
	});
});




////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
// SUBMIT BUTTON ACTIVATE/DEACTIVATE TOGGLE



document.getElementById("profile_form").addEventListener("change", function() {
    document.getElementById("submit_button").disabled = false;
			submit_button.className = "button_accent";
			submit_button.setAttribute('style', '');
});




////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
// CLEAR FILE CHECKBOX



/*document.addEventListener('DOMContentLoaded', function() {


		function clearImage() {
			imageInput.value = '';
		};

    clear.addEventListener('change', function() {
        if (this.checked) {
            clearImage();
        }
    });
});

*/



/*imageInput.addEventListener('input', function() {
  if (field.value) {
    clear_container.style.display = 'block';
  } else {
    clear_container.style.display = 'none';
  }
});
*/


