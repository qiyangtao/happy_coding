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

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView, AddCommentView


urlpatterns = [
    url('^list/', CourseListView.as_view(), name='course-list'),
    url('^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course-detail'),
    url('^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course-info'),
    url('^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course-comment'),
    url('^addcomment/', AddCommentView.as_view(), name='course-addcomment'),
]
