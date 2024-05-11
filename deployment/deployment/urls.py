# from .views import *
from django.contrib import admin
from django.urls import path

from authentication.views import *
from channels_with_celery.views import StartLongRunningTask


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/orders/", OrdersByUserOrDevice.as_view(), name="index"),
    path('api/start_long_running_task/', StartLongRunningTask.as_view(), name='start_long_running_task'),
]
