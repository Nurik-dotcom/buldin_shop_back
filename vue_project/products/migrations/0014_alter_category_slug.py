# Generated by Django 4.0.4 on 2022-05-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_brand_url_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]