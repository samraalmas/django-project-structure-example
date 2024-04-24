from django.contrib import admin
from django.urls import path
# from .views import *
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index")
]
