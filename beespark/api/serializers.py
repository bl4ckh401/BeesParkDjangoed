from django.db import models
from rest_framework import fields, serializers
from .models import ReserveTable, Tables

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('file')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveTable
        fields = ('table', 'name', 'arrival')

class CreateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ("__all__")