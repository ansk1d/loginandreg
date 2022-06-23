from django.urls import *
from . import views

urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('success',views.success),
    path('logout',views.logout),
]