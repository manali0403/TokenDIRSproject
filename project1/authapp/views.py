from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView


# Create your views here.

class UserAPI(CreateAPIView):
    serializer_class = UserSerializer

