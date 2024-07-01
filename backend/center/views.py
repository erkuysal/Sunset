from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from backend.utilities.access_level import access_level_required

from first.models import CustomUser


@login_required
@access_level_required(5)
def dashboard(request):
    return render(request, 'center/dashboard.html', {'title': 'Command Center'})


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


def search(request):
    query = request.GET.get('q')
    if query:
        users = CustomUser.objects.filter(username__icontains=query)
    else:
        users = None

    return render(request, 'center/search.html', {'results': users})
