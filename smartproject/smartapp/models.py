from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.hashers import make_password,check_password


class mainuser(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=35, null=False)
    user_mail = models.EmailField(unique=True, null=False)
    user_password = models.CharField(max_length=128, null=False)
    user_phonenumber = models.BigIntegerField(unique=True, null=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)


    def check_password(self, raw_email,raw_password):
        # Implement password validation logic here
        if (self.user_mail == raw_email) and (self.user_password == raw_password):
            return True
        else:
            return False

    def check_mail(self, mail):
        if self.user_mail == mail:
            return True
        else:
            return False
    
    
    class Meta:
        db_table ="sp_mainuser"
        


# models.py
from django.db import models

class Device(models.Model):
    device_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(mainuser, on_delete=models.CASCADE,default=1)
    DEVICE_TYPES = [
        ('sensor', 'Sensor'),
        ('actuator', 'Actuator'),
        ('controller', 'Controller'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=False,choices=DEVICE_TYPES)

    def __str__(self):
        return self.name


    class Meta:
        db_table ="sp_device"

class Contact(models.Model):
    device = models.ForeignKey(Device,  on_delete=models.CASCADE,default=1)
    email = models.EmailField(unique=True,null=False)
    phone = models.CharField(max_length=10,unique=True,null=False)

    def __str__(self):
        return f"{self.email} - {self.phone}"
    
    
    class Meta:
        db_table ="sp_contact"



class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(mainuser, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    customization = models.CharField(max_length=50)
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    razorpay_order_id = models.CharField(max_length=100, default=0)
    razorpay_payment_id = models.CharField(max_length=100, null=True, default=0)
    
    
    class Meta:
        db_table ="sp_order"
        
        


from django.db import models
from .models import mainuser, Device

class History(models.Model):
    user = models.ForeignKey(mainuser, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio_history/%Y/%m/%d/')
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.device.name} - {self.recorded_at}"
    
    class Meta:
        db_table ="sp_history"