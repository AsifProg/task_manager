from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='home'),
]
