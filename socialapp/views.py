# -*- coding: utf-8 -*-
import django_filters

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin

from socialapp.models import UserProfile, Category
from socialapp.models import Organisation, Post, Order
from socialapp.serializers import UserProfileSerializer
from socialapp.serializers import OrganisationSerializer
from socialapp.serializers import CategorySerializer
from socialapp.serializers import PostSerializer
from socialapp.serializers import OrderSerializer


class UserOrders(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
	
	def get(self, request, *args, **kwargs):
		user = self.request.user
		return Order.objects.filter(user=user)

class UserPosts(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
	
	def get(self, request, *args, **kwargs):
		user = self.request.user
		return Post.objects.filter(user=user)

@permission_classes((AllowAny, ))
class PostList(CsrfExemptMixin,
				mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('title', 'location')

	@csrf_exempt
	def dispatch(self, request, *args, **kwargs):
		return super(PostList, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class PostDetail(CsrfExemptMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	@csrf_exempt
	def dispatch(self, request, *args, **kwargs):
		return super(PostDetail, self).dispatch(request, *args, **kwargs)

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
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'location')

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
	filter_backends = (filters.SearchFilter,)
	search_fields = ('first_name', 'last_name', 'location')

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