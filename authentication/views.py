import serializers as serializers
from django.shortcuts import render
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from .serializers import SignUpSerializer, AuthTokenSerializer
from  .services import AuthServices
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
from rest_framework.views import APIView


class SignUpView(APIView):


    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = AuthServices.create_user(**serializer.validated_data)

        return Response(200)


class LoginView(APIView):

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.get_or_create(user=user)
        data = {
            'token': user.auth_token.key
        }

        return Response(data)