import re
from typing import Generic
from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer, UserSignUpSerializer, UserSignInSerializer
from rest_framework import generics
from .mixins import CustomLoginRequiredMixin

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()[:20]
    serializer_class = UserSerializer


class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer


class UserCheckLogin(CustomLoginRequiredMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user], many=True)
        return Response(serializer.data[0])


class UserList(CustomLoginRequiredMixin, generics.ListAPIView):
    # Get all users, limit = 20
    queryset = User.objects.all()[:20]
    serializer_class = UserSerializer
