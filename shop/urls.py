from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [
    path(r'category/', views.showproducts, name="showproducts")
]