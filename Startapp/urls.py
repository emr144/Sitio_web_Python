
from django.urls import path
from .views import login_view, logout_view, register_view, NotLoginView, update_profile, profile_view  

urlpatterns = [
    path(' login/', login_view, name='login'),
    path(' logout/', logout_view, name='logout'),
    path(' register/', register_view, name='register'),
    path(' not-login/', NotLoginView.as_view(), name='not_login'), 
    path(' update-profile/', update_profile, name='update_profile'),
    path(' profile/', profile_view, name='profile'),
]