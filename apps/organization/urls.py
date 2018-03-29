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
from django.conf.urls import url

from organization.views import OrgListView, AddUserAskView, OrgDetailView, CourseDetailView, DescDetailView, TeachersDetailView


urlpatterns = [
    url('^list/', OrgListView.as_view(), name='org-list'),
    url('^add_ask/', AddUserAskView.as_view(), name='add-ask'),
    url('^detail-homepage/(?P<org_id>\d+)/$', OrgDetailView.as_view(), name='detail-homepage'),
    url('^detail-course/(?P<org_id>\d+)/$', CourseDetailView.as_view(), name='detail-course'),
    url('^detail-desc/(?P<org_id>\d+)/$', DescDetailView.as_view(), name='detail-desc'),
    url('^detail-teachers/(?P<org_id>\d+)/$', TeachersDetailView.as_view(), name='detail-teachers'),
]
