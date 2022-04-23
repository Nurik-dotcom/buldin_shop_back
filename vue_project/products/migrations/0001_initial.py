# Generated by Django 4.0.4 on 2022-04-23 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_aviable', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('describtion', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/product')),
                ('add_time', models.DateField(auto_now_add=True)),
                ('saled', models.IntegerField(default=0)),
                ('in_sale', models.IntegerField(default=0)),
                ('weigth', models.IntegerField()),
                ('heigth', models.IntegerField()),
                ('width', models.IntegerField()),
                ('thicness', models.IntegerField()),
                ('color', models.CharField(max_length=15)),
                ('count', models.IntegerField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]