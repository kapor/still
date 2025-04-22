// like unlike post
const likeUnlikeShelf = () => {
    const like_unlike_shelf_form = [...document.getElementsByClassName('like_unlike_shelf_form')]
    like_unlike_shelf_form.forEach(form => form.addEventListener('submit', e => {
        //prevent default stops form submitting in favor of custom ajax
        e.preventDefault()
        //clicked form is being stored in the custom attribute 'data_form_id'
        const clickedId = e.target.getAttribute('data_form_id')
        const clickedButton = document.getElementById(`like_unlike_shelf_${clickedId}`)

        $.ajax({
            type: 'POST',
            url: `/shelf/like_unlike/`,
            data: {
                //taken from https://docs.djangoproject.com/en/5.1/howto/csrf/
                'csrfmiddlewaretoken': csrftoken,
                'pk': clickedId,
            },
            success: function(response){
                console.log(response)
                clickedButton.textContent = response.liked ? 
                `Unlike  | ${response.count}`
                : 
                `Like | ${response.count}`
            },
            error: function(error){
                console.log(error)
            }
        })
    }))
}



likeUnlikeShelf()
