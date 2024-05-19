from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    # Check if the user has the appropriate access level
    if request.user.has_perm('your_app.your_permission'):  # Replace with your actual permission check
        # Redirect to the access granted view with the target URL
        return HttpResponseRedirect(f'/access/?next={request.path}')
    else:
        return render(request, 'utilities/access_denied.html')

    #return render(request, 'center/dashboard.html', {'title': 'Command Center'})


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
    target_url = request.GET.get('next', '/')
    return render(request, 'utilities/access_granted.html', {'target_url': target_url, 'title': 'ACCESS GRANTED<'})

