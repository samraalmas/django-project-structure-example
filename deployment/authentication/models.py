

from django.db import models


class User(models.Model):
    email = models.EmailField()
    

class Devices(models.Model):
    device_id = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank =True, null = True, on_delete=models.CASCADE)

    
class Orders(models.Model):
    name = models.CharField(max_length=255)
    device_id = models.ForeignKey(Devices, null =True, blank = True, on_delete=models.SET_NULL)
    boo = models.ForeignKey(User, null = True , blank = True , on_delete=models.SET_NULL)
