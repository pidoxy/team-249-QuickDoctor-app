from django.shortcuts import render
from django.http import HttpResponse
#*from django.shortcuts import get_objects_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import viewsets

from .serializers import DoctorSerializer
from .models import Doctor

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('name')
    serializer_class = DoctorSerializer
    """
    def get(self, request):
        doctoring = Doctor.objects.all()
        serializer = DoctorSerializer(doctoring, many=True)

        return Response(serializer.data)

    def post(self, request):
        pass
"""