# Generated by Django 4.0.3 on 2022-03-30 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authtoken.token'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Юр.Лицо', 'Юр.Лицо'), ('Физ.Лицо', 'Физ.Лицо')], max_length=10, null=True),
        ),
    ]
