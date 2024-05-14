from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

# Create your views here.


def hub(request):
    return render(request, 'main/hub.html', {'title': 'To The?'})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user object
            login(request, user)  # Log in the user immediately after signing up
            return redirect('hub')  # Redirect to a home page or dashboard
    else:
        form = SignUpForm()

    return render(request, 'register/sign-up.html', {'title': 'Join Us', 'form': form})


def sign_in(request):
    return render(request, 'register/sign-in.html', {'title': 'Come in'})





