from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfilesSerializer
from rest_framework.response import Response



class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfilesSerializer(profile)
        return Response(serializer.data)
