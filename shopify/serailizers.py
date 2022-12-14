from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import Signup


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'
