from django.conf import settings


def debug_mode(request):
    return {
        'DEBUG': settings.DEBUG
    }


def register_nav_links(request):
    nav_links = [
    ]

    if request.user.is_authenticated:
        nav_links.append({'url': 'sign-out', 'name': 'Sign Out'})
    else:
        nav_links.append({'url': 'sign-in', 'name': 'Sign In'})
        nav_links.append({'url': 'sign-up', 'name': 'Sign Up'})

    return {
        'nav_links': nav_links
    }
