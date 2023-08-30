from django.contrib import admin
from django.urls import path,include
from .views import *;

urlpatterns = [
  path('login',login_view,name='account.login'),
  path('logout',logout_view,name='account.logout'),
  path('emp',emp,name="emp"),
  path('client',client,name="client")
]


