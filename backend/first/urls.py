from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('profile/', login_required(views.profile, login_url='/sign-in/'), name='profile'),
    path('sign-out/', views.sign_out, name='sign-out'),
]