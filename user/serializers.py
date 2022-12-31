from rest_framework import serializers
from .models import User


# USERS and AUTH
class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = ["email","phone_number","is_staff"]


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password reset endpoint.
    """

    email = serializers.EmailField(required=True)


class NewPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    new_password = serializers.CharField()
    short_code = serializers.IntegerField()