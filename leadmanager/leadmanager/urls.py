
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path, include

urlpatterns = [
    url('', include('frontend.urls')),
    url('', include('leads.urls')),
]
