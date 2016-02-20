# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from socialapp.models import Organisation, Post, Order
from socialapp.models import Category, UserProfile
from socialapp import views 
	
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'post', views.PostViewSet)
# router.register(r'category', views.CategoryViewSet)
# router.register(r'organisation', views.OrganisationViewSet)

urlpatterns = [
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),
    url(r'^user/$', views.UserProfileList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserProfileDetail.as_view()),
    url(r'^organisation/$', views.OrganisationList.as_view()),
    url(r'^organisation/(?P<pk>[0-9]+)$', views.OrganisationDetail.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)$', views.OrderDetail.as_view()),
]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^post/', post_list, name="post_list"),
    #url(r'^socialapp/', include('socialapp.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include(router.urls)),
	]