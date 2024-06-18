from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/create', views.create_post, name='create_post'),
    path('post/detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    # under development // newly added
    path('likes/', views.likes, name='likes'),
]