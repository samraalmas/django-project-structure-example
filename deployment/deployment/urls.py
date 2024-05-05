# from .views import *
from django.contrib import admin
from django.urls import path

from authentication.views import *



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/orders/", OrdersByUserOrDevice.as_view(), name="index"),
]
