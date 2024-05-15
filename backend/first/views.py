from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import CustomUserForm
# Create your views here.


def hub(request):
    return render(request, 'main/hub.html', {'title': 'To The?'})


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            return redirect('hub')  # Change 'login' to the name of your login URL
    else:
        form = CustomUserForm()

    return render(request, 'register/sign-up.html', {'title': 'Join Us', 'form': form})


def sign_in(request):
    return render(request, 'register/sign-in.html', {'title': 'Come in'})





