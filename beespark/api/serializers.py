from dataclasses import field
from pyexpat import model
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Posts, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'username', 'password')


class UserLogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post', 'post_description', 'likes', 'comment']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_title', 'product_price',
                  'product_image', 'product_description', 'product_quantity', 'product_slug']
