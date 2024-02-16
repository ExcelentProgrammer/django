from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from core.http.models import Post, PendingUser, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', "desc", "image"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["first_name", "last_name", "phone"]
        model = User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=255, validators=[
        UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "password"]
        extra_kwargs = {
            "first_name": {
                "required": True,
            },
            "last_name": {
                "required": True
            }
        }


class ConfirmSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)


class PendingUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'phone', 'first_name', 'last_name']
        model = PendingUser


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = User.objects.filter(phone=value)
        if user.exists():
            return value

        raise serializers.ValidationError(_("User does not exist"))


class ResetConfirmationSerializer(serializers.Serializer):
    code = serializers.IntegerField(min_value=1000, max_value=9999)
    phone = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate_phone(self, value):
        user = User.objects.filter(phone=value)
        if user.exists():
            return value
        raise serializers.ValidationError(_("User does not exist"))
