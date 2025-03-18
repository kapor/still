// create modal object
//....

const confirmModal = new modal_1 ({
	titleText: 'Are you sure?',
	messageText: 'This action is permenant',
	confirmText: 'Yes',
	cancelText: 'Cancel',
	button_secondary: 'Close',
	button_accent: 'Add',
})

console.log(confirmModal);

const element = document.getElementById('open_modal');
if (element) {
    element.addEventListener('click', () => {
	console.log('open modal clicked');

	confirmModal
		.open()
		.then(value => 
		console.log('User clicked confirm: ', value)
		)
		.catch(value =>
		console.log('User clicked cancel: ', value)
		);

	// further actions
});
}


