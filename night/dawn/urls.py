from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sunrise/', views.sunrise, name="sunrise"),
    #path('noon/', views.noon, name="noon"),
    #path('sunset/', views.sunset, name="sunset"),
]
