# Generated by Django 4.0.4 on 2022-04-26 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default='default.png', on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]