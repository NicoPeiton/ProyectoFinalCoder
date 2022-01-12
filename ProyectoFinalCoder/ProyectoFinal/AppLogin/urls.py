from django.urls import path
from AppLogin import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name="AppLogin/logout.html"), name='Logout'),
]