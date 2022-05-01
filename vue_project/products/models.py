from django.db import models
from django.db.models.signals import post_save
# Create your models here.
import os

from django.dispatch import receiver
def get_upload_path(instance, filename):
    return os.path.join(instance.title ,instance.product.title, filename)

class Brand(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return 'Категория: {}, Тип Продукта: {}'.format(self.category, self.type)


class Product(models.Model):
    is_aviable = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    describtion = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/product', default='default.png')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    add_time = models.DateField(auto_now_add=True)
    saled = models.IntegerField(default=0)
    in_sale = models.IntegerField(default=0)
    weigth = models.IntegerField()
    heigth = models.IntegerField()
    width = models.IntegerField()
    thicness = models.IntegerField()
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.in_sale == 0:
            self.is_aviable = False
        super(Product, self).save(*args, **kwargs)

    @property
    def full_count(self):
        full_count = self.in_sale + self.saled
        return full_count

