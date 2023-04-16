from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import email_validator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# customize token claim
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'password',
            'confirm_password'
        ]

    def validate_email(self,value):
        """
        check if the value is a valid email address
        """
        email_validator(value)
        return value

        
    def validate(self, attrs):
    
        """
        check if passwords match
        """
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('passwords does not match')
            
        
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
