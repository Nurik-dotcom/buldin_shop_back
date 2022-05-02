from django.db import models
from django.db.models.signals import post_save
# Create your models here.
import os
from django.template.defaultfilters import slugify
from django.dispatch import receiver
def get_upload_path(instance, filename):
    return os.path.join(instance.title ,instance.product.title, filename)

class Brand(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title


class Category(models.Model):
    slug = models.SlugField(default='',editable=False)
    category = models.CharField(max_length=100, help_text='Писать на английском. ТОЛЬКО')
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Категория: {}, Тип Продукта: {}'.format(self.category, self.type)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    is_aviable = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    describtion = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/product', default='default.png')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    add_time = models.DateField(auto_now_add=True, null=True, blank=True)
    saled = models.IntegerField(default=0, null=True, blank=True)
    in_sale = models.IntegerField(default=0, null=True, blank=True)
    weigth = models.IntegerField(null=True, blank=True)
    heigth = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    thicness = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=15, null=True, blank=True)

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

