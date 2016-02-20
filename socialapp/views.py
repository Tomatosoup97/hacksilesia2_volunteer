# -*- coding: utf-8 -*-
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from socialapp.models import UserProfile, Category, Organisation, Post, Order
from socialapp.serializers import UserProfileSerializer, OrganisationSerializer
from socialapp.serializers import CategorySerializer, PostSerializer, OrderSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes((AllowAny, ))
class PostList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@permission_classes((AllowAny, ))
class CategoryList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class CategoryDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@permission_classes((AllowAny, ))
class OrganisationList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = Organisation.objects.all()
	serializer_class = OrganisationSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class OrganisationDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Organisation.objects.all()
	serializer_class = OrganisationSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

@permission_classes((AllowAny, ))
class UserProfileList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class UserProfileDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


@permission_classes((AllowAny, ))
class OrderList(mixins.ListModelMixin,
				  mixins.CreateModelMixin,
				  generics.GenericAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class OrderDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


# class UserViewSet(viewsets.ModelViewSet):
# 	queryset = UserProfile.objects.all()
# 	serializer_class = UserProfileSerializer

# class PostViewSet(viewsets.ModelViewSet):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
# 	queryset = Category.objects.all()
# 	serializer_class = CategorySerializer

# class OrganisationViewSet(viewsets.ModelViewSet):
# 	queryset = Organisation.objects.all()
# 	serializer_class = OrganisationSerializer