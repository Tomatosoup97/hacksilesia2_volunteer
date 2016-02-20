# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, AbstractUser

class Category(models.Model):
	name = models.CharField(max_length=200)
	icon = models.ImageField(blank=True)
	icon2 = models.ImageField(blank=True)

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
	location = models.CharField(max_length=100)

	def __str__(self):
		if self.first_name:
			return "{} {}".format(self.first_name, self.last_name)
		else:
			return self.last_name

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(blank=True)
	date = models.DateTimeField()
	organisation = models.ForeignKey(
		Organisation, related_name='posts', blank=True)
	user = models.ForeignKey(UserProfile, blank=True)
	location = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.title