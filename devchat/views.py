from django.shortcuts import render
from rest_framework import viewsets

from .custom.customviewsets import *
from .models import *
from rest_framework.filters import SearchFilter
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from devchat.custom.permissions import *


class GroupViewset(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, CustomGroupPermissions]
    filter_backends = [SearchFilter]
    filterset_fields = ['name']


class ProfileViewset(CustomProfileViewset):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, CustomGroupPermissions]
    # filter_backends = [SearchFilter]
    # filterset_fields = ['name']
