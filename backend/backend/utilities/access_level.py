from functools import wraps
from django.http import HttpResponseForbidden


def access_level_required(level):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_access_level = request.user.access_level  # Get the access level of the user

            if user_access_level < level:
                return HttpResponseForbidden("You don't have permission to access this page.")
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator