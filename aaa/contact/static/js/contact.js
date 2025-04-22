const post_box = document.getElementById('post_box')
const loader = document.getElementById('loader_container')
const load = document.getElementById('load_button')
const nomore = document.getElementById('nomore')

const post_form = document.getElementById('post_form')
const post_title = document.getElementById('id_title')
const post_message = document.getElementById('id_message')
// this is how to access the form token
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const alert_box = document.getElementById('alert_box')
console.log('csrf', csrf[0].value)
