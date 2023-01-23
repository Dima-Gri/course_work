from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/user', move_to_user_panel, name='user_panel'),
    path('login/manager', move_to_manager_panel, name='manager_panel')
]
