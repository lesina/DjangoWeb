from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from application.settings import LOGIN_URL

urlpatterns = [
    url(r'list/$', VideoList.as_view(), name="video_list"),
    url(r'^(?P<pk>\d+)/$', VideoDetail.as_view(), name="video_detail"),
    url(r'(?P<pk>\d+)/edit/$', login_required(EditVideo.as_view(), login_url=LOGIN_URL), name='video_edit'),
    url(r'new/$', login_required(CreateVideo.as_view(), login_url=LOGIN_URL), name='create_video'),
    url(r'^list/(?P<slug>\w+)', VideoCategoryView.as_view(), name='list_category'),
]
