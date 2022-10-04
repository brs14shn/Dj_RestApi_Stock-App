from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializers



class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializers




