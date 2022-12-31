from django.db import models

from products.models import Product
from user.models import User

class Cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_sold=models.DateTimeField(auto_created=True,auto_now_add=True)
