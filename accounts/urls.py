from django.conf.urls import *
from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),

]
