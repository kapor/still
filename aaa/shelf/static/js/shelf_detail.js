// SHELF
const back = document.getElementById('back_button')
const url_update = window.location.href + "update/"
const url_delete = window.location.href + "delete/"
const url = window.location.href + "data/"


const form_edit = document.getElementById('edit_form')
const form_delete = document.getElementById('delete_form')

const post_title = document.getElementById('id_title')
const post_author = document.getElementById('id_author')
const post_year = document.getElementById('id_year')
const post_type = document.getElementById('id_type')
const post_publisher = document.getElementById('id_publisher')
const post_artist = document.getElementById('id_artist')
const post_quality = document.getElementById('id_quality')
const post_price = document.getElementById('id_price')
const post_location = document.getElementById('id_location')
const post_tags = document.getElementById('id_tags')
const post_weight = document.getElementById('id_weight')
const post_pages = document.getElementById('id_pages')
const post_isbn = document.getElementById('id_isbn')
const post_description = document.getElementById('id_description')
const post_notes = document.getElementById('id_notes')
const post_image = document.getElementById('id_image')



const url_data = window.location.href + "data"
const edit = document.getElementById('shelf_edit')
const shelf_detail = document.getElementById('shelf_detail')
const remove = document.getElementById('shelf_delete')
const data_top = document.getElementById('shelf_data_top')
const data_bottom = document.getElementById('shelf_data_bottom')

const modal_content = document.getElementsByClassName('modal_content')

const csrf = document.getElementsByName('csrfmiddlewaretoken')


// BACK BUTTON
back.addEventListener('click', ()=> {
    // history.back()
    window.location = document.referrer;
})


console.log('detail')
console.log(window.location)


////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
////////////////////////////////////
// MESSAGE CONFIRMATION TIMEOUT



$(document).ready(function() {
    setTimeout(function() {
        $('#alert_box').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});

$(document).ready(function() {
    setTimeout(function() {
        $('.alert_error').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000); // 3000 milliseconds (3 seconds)
});



////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
////LIKE UNLIKE STUFF

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

// handles success messaging for deleted post
const deleted = localStorage.getItem('title')

if (deleted) {
    handle_alerts('alert_error', 'Post Deleted')
    localStorage.clear()
}





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
// DETAIL VIEW 

$.ajax({
    type: 'GET',
    url: url,
    success: function(response) {
        console.log(response)
        const data = response.data

        post_title.value = data.title
        post_author.value = data.author
        post_year.value = data.year
        post_type.value = data.type
        post_publisher.value = data.publisher
        post_artist.value = data.artist
        post_quality.value = data.quality
        post_price.value = data.price
        post_location.value = data.location
        post_tags.value = data.tags
        post_weight.value = data.weight
        post_pages.value = data.pages
        post_isbn.value = data.isbn
        post_description.value = data.description
        post_notes.value = data.notes

    },
    error: function(error) {
        console.log(error)
    }

})


////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// EDIT STUFF

$(document).ready(function() {
    $('#edit_form').on('submit', function(e) {
        e.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            type: 'POST',
            url: url_update,
            enctype: 'multipart/form-data',
            data: formData,
            contentType: false,
            processData: false,
            headers: {'X-CSRFToken': csrftoken},
            success: function(response) {
                window.location.reload();
                // handle_alerts('message_success', 'Post Updated')
            },
            error: function(error) {
                console.log(error)
                handle_alerts('message_success', 'An error occurred')
            }
        });
    });
});





////////////////////////////
////////////////////////////
////////////////////////////
////////////////////////////
// DELETE STUFF




form_delete.addEventListener('submit', e=> {
    e.preventDefault()


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
            // localStorage.setItem('message', post_message.value)
            // handle_alerts('alert_error', 'Post Deleted')
        },
        error: function(error) {
            console.log(error)
            handle_alerts('alert_error', 'An error occurred')
        }

    })

})





// MODAL IMAGE ENLARGE
document.addEventListener('DOMContentLoaded', function() {
const image_small = document.getElementById('modal_image_thumb');
const image_large = document.getElementById('modal_image_large');
const modal_form = document.getElementById('modal_form');
const shader = document.getElementById('shader');

image_small.style.cursor = "pointer";
image_large.style.cursor = "pointer";
shader.style.cursor = "pointer";

image_small.addEventListener('click', () => {
image_large.classList.remove('not_visible')
shader.style.display = "block";
});

image_large.addEventListener('click', () => {
image_large.classList.add('not_visible')
shader.style.display = "none";
});

shader.addEventListener('click', () => {
image_large.classList.add('not_visible')
shader.style.display = "none";
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    image_large.classList.add('not_visible')
    shader.style.display = "none";
  }
});

window.addEventListener('click', (event) => {
  if (event.target === modal_form) {
    image_large.classList.add('not_visible')
    shader.style.display = "none";
  } else {
    // Do nothing
  }
});
})



