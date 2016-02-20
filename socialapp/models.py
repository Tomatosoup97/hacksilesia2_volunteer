# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
	name = models.CharField(max_length=200)
	icon = models.ImageField(blank=True)

	def __str__(self):
		return self.name

class Organisation(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	logo = models.ImageField()
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.name

class Order(models.Model):
	organisation = models.ForeignKey(Organisation)
	icon = models.ImageField()
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class UserProfile(AbstractUser):  
	about = models.TextField()
	avatar = models.ImageField(blank=True)
	orders = models.ManyToManyField(Order, blank=True)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

def create_user_profile(sender, instance, created, **kwargs):  
	if created:  
		profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(blank=True)
	date = models.DateTimeField()
	organisation = models.ForeignKey(Organisation)
	user = models.ForeignKey(UserProfile)

	def __str__(self):
		return self.title