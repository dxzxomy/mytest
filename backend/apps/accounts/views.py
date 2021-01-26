from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views.generic import View
from django.core.cache import cache
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.backends import ModelBackend
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return HttpResponse("测试")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all()
    serializer_class = UserSerializer
