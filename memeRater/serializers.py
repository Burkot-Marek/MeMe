from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Meme


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('id','created', 'title', 'picture', 'dateOfBirth', 'dateOfDeath', 'description', 'public')