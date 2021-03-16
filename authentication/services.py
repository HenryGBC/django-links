from django.contrib.auth.models import User
from users.models import Profile


class AuthServices:

    @staticmethod
    def create_user(
            email: str,
            first_name: str,
            last_name: str,
            password: str,
            role: str,
            username: str,
    ) -> Profile:
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        return Profile.objects.create(
            user=user,
            role=role
        )

        # email = serializers.EmailField()
        # first_name = serializers.CharField(max_length=100)
        # last_name = serializers.CharField(max_length=100)
        # password = serializers.CharField()
        # role = serializers.CharField(max_length=150)
