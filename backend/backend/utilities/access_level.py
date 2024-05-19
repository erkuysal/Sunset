from functools import wraps
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse


def access_level_required(level):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_access_level = getattr(request.user, 'access_level', 0)  # Get the access level of the user

            if user_access_level < level:
                request.session['show_access_denied'] = True
                return HttpResponseRedirect(reverse('denied'))

            # Check if we are on the access granted page already to avoid infinite loop
            # If not coming from the "access granted" page, redirect there first
            if 'access_granted_done' not in request.session or not request.session['access_granted_done']:
                request.session['show_access_granted'] = True
                request.session['access_granted_done'] = True
                access_granted_url = f"{reverse('granted')}?next={request.path}"
                return HttpResponseRedirect(access_granted_url)
            else:
                # Once the user is on the access granted page, reset the flag
                request.session['access_granted_done'] = False

            # If already on the access granted page, proceed to the original view
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
