from django.contrib import admin
from .models import User, Devices, Orders

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'user')
    list_filter = ('user',)

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id', 'boo')
    list_filter = ('device_id', 'boo')
