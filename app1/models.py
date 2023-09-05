from django.db import models

# Create your models here.
class user_rdp(models.Model):
    Emp_Id=models.CharField(max_length=10)
    IP_Address=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    
    
    
