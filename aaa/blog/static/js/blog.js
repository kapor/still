const tab2 = document.getElementById('tab2')

const id_title = document.getElementById('id_title')
const id_message = document.getElementById('id_message')
const id_image = document.getElementById('id_image')

const modal_form = document.getElementById('modal_form')


const back = document.getElementById('back_button')

// BACK BUTTON
back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})



////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// form stuff



blog_form.addEventListener('submit', e => {
	e.preventDefault()

	$.ajax({

		type: 'POST',
		url: '',
		datatype: 'JSON',
		data: {
			// how to access the form token
			'csrfmiddlewaretoken': csrf[0].value,
			'title': id_title.value,
			'message': id_message.value,
		},
			success: function(response) {
				console.log(response)
			// places post at top of post_content
			tab2.insertAdjacentHTML('afterbegin',
			///use backticks to inject html
				`
			  <div class="post4" id="post_list">

			      <div class="post_message_group">

			        <div>
			          <!-- TITLE/MESSAGE -->
			          <div class="post_message">
			            <a href="{% url 'blog_detail' pk=item.pk %}">
			            <h3>${response.title}<span class="draft_indicator"> [draft]</span></h3> 
			            </a>
			          </div>
			          <!-- MESSAGE/TEXT -->
			          <div class="post_text">
			            <a href="{% url 'blog_detail' pk=item.pk %}">
			              <p>${response.message}</p>
			            </a>
			          </div>
			          <!-- USER/URL/TIMESTAMP -->
			          <span class="username">
			              Created just now
			            <br>
			          </span>
			        </div>

			      </div>

			  </div>
				`
			)
			$('#modal_form').modal('hide')
			handle_alerts('message_success', 'New post added in "Drafts"')
			document.getElementById("blog_form").reset()
		  },

			error: function(error) {
				console.log(error)
				handle_alerts('message_success', 'Something went wrong...')
			},

	})
});

/////////////////////////////////////////
/// CLOSE MODAL ==> FORM RESET


const form = document.getElementById('modal_form');
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
    document.getElementById('blog_form').reset();
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_dialog) {
    form.reset();
  } else {
  	// Do nothing
  }
});


// PUBLISH/DRAFT TABS
const tabHeaders = document.querySelectorAll('.tab_header');
const tabContents = document.querySelectorAll('.tab_content');

tabHeaders.forEach(header => {
	header.addEventListener('click', () => {
		// Deactivate all tabs and content
		tabHeaders.forEach(h => h.classList.remove('active'));
		tabContents.forEach(content => content.classList.remove('active'));

		// Activate the clicked tab and corresponding content
		header.classList.add('active');
		const tabId = header.getAttribute('data-tab');
		document.getElementById(tabId).classList.add('active');
	});
});


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

/*blog_form.addEventListener('submit', function(event) {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Submit the form data using AJAX
  fetch(blog_form.action, {
    method: 'POST',
    body: new FormData(blog_form),
    headers: {
      'X-Requested-With': 'XMLHttpRequest' //Identify AJAX request for Django
    }
  })
  .then(response => {
    if (response.ok) {
      // Reload the page
      window.location.reload();
    } else {
      // Handle errors if needed
      console.error('Error submitting form');
    }
  });
});
*/
