from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hub(request):
    return render(request, 'main/hub.html', {'title': 'To The?'})


def sign_up(request):
    return render(request, 'register/sign-up.html', {'title': 'Join Us'})


def sign_in(request):
    return render(request, 'register/sign-in.html', {'title': 'Come in'})

