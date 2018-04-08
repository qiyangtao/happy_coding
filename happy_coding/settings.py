# -*- coding:utf-8 -*-

"""
Django settings for happy_coding project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import importlib
import sys

import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^8m4d2#^1(uuy+0mg+tz0ke7#a_zxy2!oewo$2l3(6#3uj2uc+'

# SECURITY WARNING: don't run with debug turned on in production!
# if socket.gethostbyname('119.27.162.156') == 'VM_0_10_centos':
#     DEBUG = TEMPLATE_DEBUG = True
#     DATABASE_NAME = 'devdb'
# else:
DEBUG = TEMPLATE_DEBUG = False
#     DATABASE_NAME = 'pro_db'

ALLOWED_HOSTS = [
    '*',
]

ADMINS = (
    ('陶志强', '393082981@qq.com'),
)

MANAGERS = (
    ('陶志强', '393082981@qq.com'),
)

# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'xadmin',
    'crispy_forms',
    'users',
    'courses',
    'organization',
    'operation'
]

CAPTCHA_IMAGE_SIZE = (78, 36)  #大小

CAPTCHA_TIMEOUT = 1  # 超时(minutes)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'happy_coding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/html')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     # login 在template中可以用 "{% url socialauth_begin 'douban-oauth2' %}"
#     'social_auth.context_processors.social_auth_by_type_backends',
#     'social_auth.context_processors.social_auth_login_redirect',
# )


WSGI_APPLICATION = 'happy_coding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'proj_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
    }
}

CACHES = {
    'default': {
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS":{
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'TIMEOUT': 60
    },
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social_auth.backends.pipeline.social.social_auth_user',
#     # 用户名与邮箱关联，文档说可能出现问题
#     # 'social_auth.backends.pipeline.associate.associate_by_email',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'social_auth.backends.pipeline.user.create_user',
#     'social_auth.backends.pipeline.social.associate_user',
#     'social_auth.backends.pipeline.social.load_extra_data',
#     'social_auth.backends.pipeline.user.update_user_details',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
# )
#
# AUTHENTICATION_BACKENDS = (
#         'social_auth.backends.contrib.douban.Douban2Backend',
#         # 注意这个比较特殊,因为django-social-auth是依赖python-social-auth的
#         # python-social-auth==0.1.26,已经包含的qq的backend
#         # django-social-auth==0.8.1, 还没包含进来
#         # 你需要在django-social-auth/social_auth/backends/contrib中添加一个文件qq.py
#         # 就一行
#         # from social.backends.qq import QQOAuth2 as QQBackend
#         # 然后setup一下就ok
#         'social_auth.backends.contrib.qq.QQBackend',
#         'social_auth.backends.contrib.weibo.WeiboBackend',
#         # 必须加，否则django默认用户登录不上
#         'django.contrib.auth.backends.ModelBackend',
# )
#
#
# # 各种重定向连接
# SOCIAL_AUTH_LOGIN_URL = '/login-url/'
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
# SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
#
# # 各种key, secret
# SOCIAL_AUTH_WEIBO_KEY = 'YOUR KEY'
# SOCIAL_AUTH_WEIBO_SECRET = 'YOUR SECRET'
#
# SOCIAL_AUTH_QQ_KEY = 'YOUR KEY'
# SOCIAL_AUTH_QQ_SECRET = 'YOUR SECRET'
#
# SOCIAL_AUTH_DOUBAN_OAUTH2_KEY = 'YOUR KEY'
# SOCIAL_AUTH_DOUBAN_OAUTH2_SECRET = 'YOUR SECRET'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 自定义Model
AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'   # 服务器
EMAIL_PORT = 25               # 一般情况下都为25
EMAIL_HOST_USER = "qiyangtao002@163.com"   # 账号
EMAIL_HOST_PASSWORD = "qiyangtao008"  # 密码
EMAIL_USE_TLS = True             # 一般都为False
EMAIL_FROM = "qiyangtao002@163.com"        # 邮箱来自

