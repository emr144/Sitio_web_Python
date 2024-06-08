from django.urls import path
from .views import login_view, logout_view, register_view, not_login_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('accounts/login/', not_login_view.as_view(), name='Notlogin'),
    ]