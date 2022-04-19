from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from .models import blog_content, other


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, person, validated_data):
        person.validation_data.get('fisrt_name', person.name)
        person.save()
        return person


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_content
        fields = ['author', 'title']


class BothSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_content
        fields = '__all__'
