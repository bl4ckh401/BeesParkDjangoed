from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    post_id = models.IntegerField(
        primary_key=True, unique=True, auto_created=True, null=False)
    post = models.ImageField(upload_to='images', null=True)
    post_description = models.CharField(max_length=255, default='', null=True)
    likes = models.IntegerField(default=0, null=True)
    comment = models.CharField(max_length=255, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class Product(models.Model):
    product_id = models.IntegerField(
        primary_key=True, unique=True, auto_created=True, null=False)
    product_title = models.CharField(max_length=40, default='', null=True,)
    product_price = models.IntegerField(default=0, null=True)
    product_image = models.ImageField(upload_to='images', null=True)
    product_description = models.CharField(max_length=400, default='', )
    product_quantity = models.IntegerField(default=0, null=True)
    product_slug = models.SlugField(default='', max_length=20,)

    def __str__(self):
        return self.product_title


class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expiry_day = models.DateField()
    weekly_summary = models.CharField(max_length=255, default='', null=True)
    personal_best = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        return self.user.username
