from rest_framework.authtoken import views
from django.urls import path
from .views import *
urlpatterns = [
    path('login', views.obtain_auth_token),
    path('register', register_user),
    path('delete', delete_user)
]