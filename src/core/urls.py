from django.conf.urls import url, include
from .views import home, UserView, RegisterView
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.decorators import login_required
from application.settings import LOGIN_URL
from .views import *

urlpatterns = [
    url(r'^accounts/logout/$', login_required(logout, login_url=LOGIN_URL), {'next_page': '/'}, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/registration/$', RegisterView.as_view(), name='registration'),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^users/(?P<slug>\w+)/$', login_required(UserView.as_view(), login_url=LOGIN_URL), name="user"),
    url(r'^users/(?P<slug>\w+)/edit/$', login_required(UserEdit.as_view(), login_url=LOGIN_URL), name="user_edit"),
    url(r'^$', home, name='home'),
]
