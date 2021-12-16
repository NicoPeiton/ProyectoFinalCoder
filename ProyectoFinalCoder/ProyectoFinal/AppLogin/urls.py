from django.urls import path
from AppLogin import views

urlpatterns = [
    path('login', views.login, name='Login'),
]