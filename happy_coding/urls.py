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
from homePage import views
from homePage.activeuser import ActiveUserView

urlpatterns = [
    url(r'^$', include("homePage.urls")),
    url(r'^logout/$', views.logout_do, name="logout"),
    url(r'^register/$', views.register_do, name="register"),
    url(r'^login/$', views.login_do, name="login"),
    url(r'^captcha/', include('captcha.urls')),
    url('^ajax_val/', views.ajax_val, name='ajax_val'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),  # 提取出active后的所有字符赋给active_code
    url(r'^admin/', admin.site.urls),
]
