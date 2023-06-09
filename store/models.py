from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email =models.EmailField(max_length=200, null=True)


    def str(self):
        return self.name
    

class product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price =models.FloatField()
    digital = models.BooleanField(default=False, null=True,)
    photo =models.ImageField(upload_to="products", default=False)


    def str(self):
       return 'Producto: %s, Precio: %s' %(self.name, self.price)
