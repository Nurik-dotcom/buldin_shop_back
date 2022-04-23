from django.db import models

# Create your models here.

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
    image = models.ImageField(upload_to='images/product')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
    add_time = models.DateField(auto_now_add=True)
    saled = models.IntegerField(default=0)
    in_sale = models.IntegerField(default=0)
    weigth = models.IntegerField()
    heigth = models.IntegerField()
    width = models.IntegerField()
    thicness = models.IntegerField()
    color = models.CharField(max_length=15)
    count = models.IntegerField()
    def __str__(self):
        return self.title