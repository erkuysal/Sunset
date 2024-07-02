from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse

from .forms import CustomUserForm, SignInForm, EditProfileForm
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
    user = request.user
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile')
    else:
        edit_form = EditProfileForm(instance=user)

    return render(request, 'register/profile.html', {
        'user': user,
        'edit_form': edit_form,
        'is_editing': request.method == 'POST' or request.GET.get('edit') == 'true'
    })

    # user = get_object_or_404(CustomUser, username=username)
    # if request.user.username == username:
    #     if request.method == 'POST':
    #         edit_form = EditProfileForm(request.POST, instance=user)
    #         if edit_form.is_valid():
    #             edit_form.save()
    #             return redirect('profile', username=username)
    #     else:
    #         edit_form = EditProfileForm(instance=request.user)
    #     return render(request, 'register/profile.html', {
    #         'user': user,
    #         'profile_form': edit_form,
    #         'is_editing': request.path.endswith('edit/')
    #     })
    # else:
    #     return render(request, 'register/profile.html', {
    #         'user': user,
    #         'is_editing': request.method == 'POST' or request.GET.get('edit') == 'true'
    #         })

@login_required
def edit_profile(request, username):
    return profile(request, username)


def view_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    public_state = True
    if request.user.is_anonymous:
        return render(request, 'register/view-profile.html', {'user': user, 'public_state': public_state})
    else:
        is_following = Follow.objects.filter(follower_user=request.user, following_user=user).exists()
        public_state = False
        return render(request, 'register/view-profile.html', {'user': user, 'is_following': is_following, 'public_state': public_state})


# ////////////////////// -------------------- TEST ZONE ------------------- //////////////////////

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    follow, created = Follow.objects.get_or_create(
        follower_user=request.user,
        following_user=user_to_follow
    )
    if created:
        return JsonResponse({'status': 'followed'})
    return JsonResponse({'status': 'already followed'})


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    follow = Follow.objects.filter(
        follower_user=request.user,
        following_user=user_to_unfollow
    ).first()
    if follow:
        follow.delete()
        return JsonResponse({'status': 'unfollowed'})
    return JsonResponse({'status': 'not followed'})