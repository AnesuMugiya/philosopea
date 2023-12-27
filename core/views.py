from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Message
from .forms import ContactForm

# Landing page
def index(request):
     # if this is a POST request we need to process the form data
     if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, f'Your message has been sent. Expect a response soon!')
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
     else:
          form = ContactForm()

     return render(request, 'core/index.html', {'form': form})

# About Page
def about(request):
     return render(request, 'core/about.html')


