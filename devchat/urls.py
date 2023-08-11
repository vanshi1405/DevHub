from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from devchat.views import GroupViewset

router = DefaultRouter()
router.register('grp',viewset=GroupViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),

]
