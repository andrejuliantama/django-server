from rest_framework import serializers

from django.contrib.auth import get_user_model

from platform_auth.models import User

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
