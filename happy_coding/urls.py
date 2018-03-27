# -*- coding:utf-8 -*-
"""happy_coding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from users.activeuser import ActiveUserView
from users.resetuser import ResetUserView
import xadmin

# from homePage import views
from users.views import LoginView, register_do, logout_do, sms_sender, ForgetPwdView, ModifyView, UserInfoView


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^$', include("homePage.urls")),
    # url('^ajax_val/', views.ajax_val, name='ajax_val'),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', logout_do, name="logout"),
    url(r'^register/$', register_do, name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),  # 提取出active后的所有字符赋给active_code
    url('^sms_sender/', sms_sender, name='sms_sender'),
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetUserView.as_view(), name="user_reset"),  # 提取出active后的所有字符赋给active_code
    url('^modify/$', ModifyView.as_view(), name='modify_pwd'),
    url('^usercenter-info/', UserInfoView.as_view(), name='usercenter-info'),
]
