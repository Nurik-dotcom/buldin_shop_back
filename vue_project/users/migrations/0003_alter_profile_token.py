# Generated by Django 4.0.3 on 2022-03-30 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('users', '0002_profile_token_alter_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='token',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authtoken.token'),
        ),
    ]
