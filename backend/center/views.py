from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from backend.utilities.access_level import access_level_required

# Create your views here.


@login_required
@access_level_required(5)
def dashboard(request):
    return render(request, 'center/dashboard.html', {'title': 'Command Center'})


# @login_required
# def another_view(request):
#     # Example logic for another view
#     if request.user.is_authenticated:
#         # Redirect to the access granted view with the target URL
#         return HttpResponseRedirect(f'/access-granted/?next=/another-destination/')
#     else:
#         return render(request, 'access_denied.html')


def hub(request):
    return render(request, 'center/hub.html', {'title': 'To The?'})


def about(request):
    return render(request, 'center/about.html', {'title': 'About Us'})


# -------------- utilities--------------
def access_granted(request):
    if not request.session.pop('show_access_granted', False):
        return redirect(reverse('hub'))  # Replace 'home' with your homepage URL name
    target_url = request.GET.get('next', '/')
    return render(request, 'utilities/access_granted.html', {'target_url': target_url, 'title': 'ACCESS GRANTED'})


def access_denied(request):
    if not request.session.pop('show_access_denied', False):
        return redirect(reverse('hub'))  # Replace 'home' with your homepage URL name
    return render(request, 'utilities/access_denied.html', {'title': 'ACCESS DENIED'})

