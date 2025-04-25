console.log('profiles')
console.log(window.location)



// MODAL IMAGE ENLARGE
document.addEventListener('DOMContentLoaded', function() {
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
})


const profile_crop_detail = document.getElementById('profile_crop_detail')
const profileForm = document.getElementById('profile_form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const bioInput = document.getElementById('id_bio')
const imageInput = document.getElementById('id_image')