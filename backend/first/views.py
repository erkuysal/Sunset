from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CustomUserForm, SignInForm
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            return redirect('sign_in')  # Change 'login' to the name of your login URL
    else:
        form = CustomUserForm()

    return render(request, 'register/sign-up.html', {'title': 'Join Us', 'form': form})


def sign_in(request):
    form = SignInForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f' welcome {username} ')
                return redirect(request.GET.get('redirect_to', 'profile'))
            else:
                messages.info(request, f'User not found. Please register.')

    return render(request, 'register/sign-in.html', {'title': 'Come in', 'form': form})


def sign_out(request):
    logout(request)
    return redirect('hub')


@login_required(login_url='/sign-in/', redirect_field_name='redirect_to')
def profile(request):
    return render(request, 'register/profile.html', {'title': 'Profile'})


