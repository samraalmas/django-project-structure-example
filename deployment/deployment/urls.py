# from .views import *
from django.contrib import admin
from django.urls import path

from authentication.views import *

urlpatterns = [path("admin/", admin.site.urls), path("", index, name="index")]
