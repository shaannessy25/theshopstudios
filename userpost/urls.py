from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='userpost-home'),
    path('about/', views.about, name='userpost-about'),
]