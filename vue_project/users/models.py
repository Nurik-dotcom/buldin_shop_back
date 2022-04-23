from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
# Create your models here.
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

TYPE_OF_FACE = [
    ('Юр.Лицо', 'Юр.Лицо'),
    ('Физ.Лицо', 'Физ.Лицо')
]

STATUS = [
    ('Saler', 'Saler'),
    ('Client', 'Clint')
]
# TYPE_OF_WORK = [
#     ('IP', 'ИП'),
#     ('ТОО', 'ТОО')
# ]

class Profile(models.Model):
    type = models.CharField(choices=TYPE_OF_FACE, max_length=10, null=True)
    status = models.CharField(choices=STATUS, max_length=7, default=STATUS[1])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True, unique=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    i_agree = models.BooleanField(default=False)
    # token = models.ForeignKey(Token, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self) -> str:
        return self.user.username
    
    def is_authenticated(self):
        return True
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
# class IP_TOO(models.Model):
#     title = models.CharField(max_length=1000, null=True)

class YrLico(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # work = models.CharField(choices=TYPE_OF_WORK, max_length=10)
    # ip_too = models.ForeignKey(IP_TOO, on_delete=models.CASCADE)
    ip_too = models.CharField(max_length=100)

class FizLico(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    father_name = models.CharField(max_length=100)
