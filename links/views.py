from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import Profile
from .models import Links
from rest_framework import serializers, exceptions
from rest_framework.response import Response

class LinksView(APIView):
    permission_classes = (IsAuthenticated,)

    class LinkModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = Links
            fields = '__all__'

    class LinkSerializer(serializers.Serializer):
        url = serializers.CharField(max_length=240)
        name = serializers.CharField(max_length=240)


    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        print(profile)
        links = Links.objects.filter(profile__pk=profile.pk).order_by('-created_at')
        serializer = self.LinkModelSerializer(data=links, many=True)
        serializer.is_valid()
        return Response(serializer.data)


    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.LinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        url = serializer.validated_data.get('url')
        link = Links.objects.create(
            profile=profile,
            name=name,
            url=url
        )

        serializer_data = self.LinkModelSerializer(link)

        return Response(serializer_data.data)