
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField()
    role = serializers.CharField(max_length=150)

    def validate_email(self, data):
        email = data.lower()

        if User.objects.filter(email=email).exists():
            msg = _("Ya existe un usuario registrado con este correo electrónico.")
            raise exceptions.ValidationError(msg)
        return email

    def validate(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        username = '%s.%s' % (first_name.lower(), last_name.lower())
        username = '{:.29}'.format(username)
        counter = User.objects.filter(first_name=first_name, last_name=last_name).count()
        if counter > 0:
            username += '%s' % (counter + 1)
        data['username'] = username
        return data



class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email').lower()
        password = data.get('password')

        if email and password:
            UserModel = get_user_model()
            if not User.objects.filter(email=email).exists():
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)

            user = UserModel._default_manager.get(email=email)
            check = user.check_password(password)
            if check:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        data['user'] = user
        return data

