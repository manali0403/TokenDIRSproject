from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset =  Student.objects.all()

class SimpleAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response(data={"detail":"this is simple API view "} ,status=200)


