from dataclasses import field
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import *
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]

class ProfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.ModelSerializer):
    user = ProfUserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'type', 'phone_number']
    # def update(self, instance, validated_data):
    #     instance.type = validated_data.get('type', instance.type)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)

    #     return instance








    # def create(self, validated_data):
    #     profile = Profile.objects.create(
    #         type = validated_data['type'],
    #         phone_number = validated_data['phone_number'],
    #     )
    #     return profile
    #     profile_data = validated_data.pop('profile')
    #     profile = Profile.objects.create(
    #         user=user,
    #         type = profile_data['type'],
    #         phone_number = profile_data['phone_number']
    #     )
    #     return user
        

class NumberPhone(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number']

class UserLogIn(serializers.ModelSerializer):
    profile = ProfileSerializer
    class Meta:
        model = User
        fields = ['profile', 'username']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

class UserSerializerer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class LogInSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['phone_number', 'user']

class ProfileSeralizers(serializers.ModelSerializer):
    user = UserSerializerer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'address', 'phone_number']




class AuthTokenSerializers(serializers.Serializer):
    phone_number = serializers.CharField(
        label=_("Phone number"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        q = Profile.objects.get(phone_number=phone_number)
        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                username=q, password=password)
            if not user:
                msg = _('Неправильный логин или пароль')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
