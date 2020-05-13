from rest_framework import serializers
#*from rest_framework.request import Request
#*from rest_framework.test import APIRequestFactory
from .models import Doctor
#*from .serializers import DoctorSerializer
"""
factory = APIRequestFactory()
request = factory.get('/')


serializer_context = {
    'request': Request(request),
}

d = Doctor.objects.first()
s = DoctorSerializer(instance=p, context=serializer_context)

print (s.data)
"""

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__') #* ('name', 'field', 'email', 'contact', 'address'  )
        