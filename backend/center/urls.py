from django.urls import path
from . import views


urlpatterns = [
    path('', views.hub, name='hub'),
    path('about/', views.about, name='about'),


    # ------- Utilities ------------
    # path('access/', views.access_granted, name='success')
]