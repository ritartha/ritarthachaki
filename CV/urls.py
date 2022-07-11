from django.urls import path
from . import views
import os

#register the app namespace
app_name = 'Home'  #do not change this variable name

urlpatterns = [
    path('',views.cv_home_page, name='home'),
    
]

