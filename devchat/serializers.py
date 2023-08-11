from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    users = ProfileSerializer(many=True, required=False)

    class Meta:
        model = Group
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation()
        return data
