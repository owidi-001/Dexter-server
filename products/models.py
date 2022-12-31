from django.db import models
from user.models import User

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    minQuantity=models.IntegerField()
    image=models.TextField()
    type=models.CharField(max_length=200)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)


    def __str__(self) -> str:
        return f"name: {self.name}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name',)