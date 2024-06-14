
from django.urls import path
from Startapp.views import  NotLoginView
from . import views

urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('not-login/', NotLoginView.as_view(), name='not_login'),
    path('user/', views.UserView.as_view(), name='user'), 
    path('update-profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile_view, name='profile'),
]