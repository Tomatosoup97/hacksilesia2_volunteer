from django.contrib.auth.models import User
from rest_framework import serializers
from socialapp.models import Post, Category, UserProfile 
from socialapp.models import Order, Organisation

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'id', 'content', 'organisation',
			'image', 'date', 'title', 'user',
			)

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = (
			'id', 'name', 'icon',
			)

class OrganisationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organisation
		fields = (
			'id', 'name', 'description',
			'logo', 'category',
			)

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = (
			'id', 'username', 'email', 'first_name',
			'last_name', 'about', 'avatar', 'password',
			'orders',
			)

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = (
			'id', 'organisation', 'name', 'icon'
			)
