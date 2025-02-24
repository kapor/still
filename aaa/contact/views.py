from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()

# def ContactHome(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			return redirect('contact/form.html')
# 		else:
# 			form = ContactForm()
# 		return render(request, 'form.html', {'form': form})



def ContactHome(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)	
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            post = form.save()
            return redirect('contact')
    context = {'form':form}
    return render(request, 'contact/form.html', context)