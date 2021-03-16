from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from .models import Profile

class UsersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'date_joined'
        )


class ProfilesSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'role'
        )