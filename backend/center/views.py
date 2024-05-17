from django.shortcuts import render

# Create your views here.


def hub(request):
    return render(request, 'center/hub.html', {'title': 'To The?'})


def about(request):
    return render(request, 'center/about.html', {'title': 'About Us'})