from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CustomUserForm, SignInForm
from .models import CustomUser, Follow
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
            return redirect('sign-in')  # Change 'login' to the name of your login URL
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


def view_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    is_following = Follow.objects.filter(follower_user=request.user, following_user=user).exists()
    return render(request, 'register/view-profile.html', {'user': user, 'is_following': is_following})


# ////////////////////// -------------------- TEST ZONE ------------------- //////////////////////

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    if request.user != user_to_follow:
        Follow.objects.get_or_create(follower_user=request.user, following_user=user_to_follow)
    return redirect('view-profile', username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    Follow.objects.filter(follower_user=request.user, following_user=user_to_unfollow).delete()
    return redirect('view-profile', username=username)
