const post_content = document.getElementById('post_content')
const id_message = document.getElementById('id_message')
const id_group = document.getElementById('id_group')
const id_image = document.getElementById('id_image')

const remove = document.getElementById('delete_button')

const post_form = document.getElementById('post_form')
const url_delete = window.location.href + "/delete/"

const form_edit = document.getElementById('edit_form')
const form_delete = document.getElementById('delete_form')




const back = document.getElementById('back_button')

// BACK BUTTON
back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})




console.log('hello world')
console.log(window.location)



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// DELETE STUFF




form_delete.addEventListener('submit', e=> {
	e.preventDefault()

	const message = document.getElementById('message')
	const success_url = "posts/"

	$.ajax({
		type: 'POST',
		url: url_delete,
		data: {
			'csrfmiddlewaretoken': csrf[0].value,
		},
		success: function(response) {
			// history.go(-2)
			window.location = document.referrer;
			// console.log(response)
			// history.back(-2).location.reload();
			// window.location.href = window.location.origin
			localStorage.setItem('message', post_message.value)
			//handle_alerts('alert_error', 'Post Deleted')
		},
		error: function(error) {
			console.log(error)
			handle_alerts('alert_error', 'An error occurred')
		}

	})

})








