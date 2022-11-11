from rest_framework import serializers
from .models import *


class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)


class signupSerializer(serializers.Serializer):
    f_name = serializers.CharField(required = True)
    l_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    phone = serializers.CharField(required = False)
    password = serializers.CharField(required = True)


class otpSerializer(serializers.Serializer):
    otp = serializers.IntegerField(required = True)
    password = serializers.CharField(required = True)


class emailSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)


class CustomerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ["f_name", "l_name"]

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ["f_name", "l_name", "email", "phone"]

class PhoneNoSerializer(serializers.Serializer):
    phone = serializers.CharField(required = True)

class NameSerializer(serializers.Serializer):
    f_name = serializers.CharField(required = True)
    l_name = serializers.CharField(required = True)
