from django.urls import path

from accounts.views import login_profile
from . import views

urlpatterns = [
    path('login/', login_profile, name = 'login_profile'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register_profile, name='register'),
]
