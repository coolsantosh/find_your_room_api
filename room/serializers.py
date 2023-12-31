from rest_framework import serializers
from .models import Room
from account.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','mobile']


class RoomSerializer(serializers.ModelSerializer):
    user=  UserSerializer()
    class Meta:
        model= Room
        fields= "__all__"
        