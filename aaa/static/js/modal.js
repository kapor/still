// modal class object
//....


class modal_1 {
	constructor ({
		titleText,
		messageText,
		confirmText,
		formId,
		formAction,
		formEnctype,
		button_secondary,
		button_accent,
	}) {
		this.titleText = titleText;
		this.messageText = messageText;
		this.confirmText = confirmText;
		this.formId = formId;
		this.formAction = formAction;
		this.formEnctype = formEnctype;
		this.button_secondary = button_secondary;
		this.button_accent = button_accent;
	}



	createAndOpen(onConfirm, onCancel) {


		// MAIN MODAL AND BACKGRUND 

		this.modalElem = document.createElement('div');
		this.modalElem.classList.add('modal2');
		this.modalElem.setAttribute('id', 'modal2');
		setTimeout(() => {
			this.modalElem.classList.add('show');
		}, 20);

		const modalUnderlayElem = document.createElement('div');
		modalUnderlayElem.classList.add('_underlay');
		this.modalElem.appendChild(modalUnderlayElem);

		modalUnderlayElem.addEventListener('click', () => {
			onCancel('Cancelled');
			this.close();
		});

		const modalContentElem = document.createElement('div');
		modalContentElem.classList.add('modal_content2');
		this.modalElem.appendChild(modalContentElem);




		// TITLE 

		const titleTextElem = document.createElement('h2');
		titleTextElem.classList.add('titleText');
		titleTextElem.textContent = this.titleText;
		modalContentElem.appendChild(titleTextElem);



		// FORM CONTAINER

		const modalFormElem = document.createElement('form');
		modalContentElem.appendChild(modalFormElem);

		const modalFormConElem = document.createElement('div');
		modalFormConElem.classList.add('form_container');
		modalContentElem.appendChild(modalFormConElem);





		/// buttons
		const modalBtnContainerElem = document.createElement('div');
		modalBtnContainerElem.classList.add('button_container_modal');
		modalContentElem.appendChild(modalBtnContainerElem);

		/// cancel/close/secondary button
		const modalBtnSecondary = document.createElement('button');
		modalBtnSecondary.classList.add('button_secondary');
		modalBtnSecondary.textContent = this.button_secondary;
		modalBtnSecondary.setAttribute('id', 'modal_close');
		modalBtnSecondary.setAttribute('style', 'width:50%');
		modalBtnSecondary.setAttribute('_', 'on click trigger close');
		modalBtnContainerElem.appendChild(modalBtnSecondary);

		modalBtnSecondary.addEventListener('click', () => {
			onCancel('Cancelled');
			this.close();
		});


		/// confirm/submit/action/primary button
		const modalBtnSubmit = document.createElement('input');
		modalBtnSubmit.classList.add('button_accent');
		modalBtnSubmit.value = this.button_accent;
		modalBtnSubmit.setAttribute('type', 'submit');
		modalBtnSubmit.setAttribute('style', 'width:50%');
		modalBtnContainerElem.appendChild(modalBtnSubmit);

		modalBtnSubmit.addEventListener('click', () => {
			onCancel('Success');
			this.close();
		});

		document.body.appendChild(this.modalElem);
		document.addEventListener('keydown', this.escapeKeyDown.bind(this));
	}



	open() {
		return new Promise((resolve, reject) => {
			this.createAndOpen(resolve, reject);
		});
	}


	close() {
		this.modalElem.classList.remove('show');
		setTimeout(() => {
			document.body.removeChild(this.modalElem);
		}, 40);

	}

	escapeKeyDown(event) {
		if (event.key === 'Escape') {
			this.close();
		}
	}




}






