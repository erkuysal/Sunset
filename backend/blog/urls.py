from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/', views.create_post, name='post'),
    path('post/detail/',views.post_detail, name='post_detail'),
    #path('comment/', views.comment, name='comment'),
]