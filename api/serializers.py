from email.policy import default
from multiprocessing import allow_connection_pickling
import random
import string
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import PhoneNumberUser, OTPRequest


class RequestOTPSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=50, allow_null=False)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = '__all__'


def generate_username():
    username = string.ascii_lowercase
    return ''.join(random.choice(username) for i in range(10))


class VerifyOtpRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False)
    receiver = serializers.CharField(max_length=64, allow_null=False)


class ObtainTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=128, allow_null=False)
    request_id = serializers.UUIDField(allow_null=False)
    username = serializers.CharField(max_length=128, allow_null=False)
    phone = serializers.CharField(max_length=15, allow_null=False)
    created = serializers.BooleanField()
