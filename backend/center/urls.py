from django.urls import path
from . import views


urlpatterns = [
    path('', views.hub, name='hub'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),


    # ------- Utilities ------------
    path('granted/', views.access_granted, name='granted'),
    path('denied/', views.access_denied, name='denied'),
    path('search/', views.search, name='search'),
]