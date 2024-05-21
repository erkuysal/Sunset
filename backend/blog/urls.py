from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('post/', views.post, name='post'),
    path('commnet/', views.comment, name='comment'),
]