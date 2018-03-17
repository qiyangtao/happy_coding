# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import *
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib.auth.hashers import make_password
from forms import *
from models import *
import logging

# Create your views here.
logger = logging.getLogger('homePage.view')


def home(request):
    print (request.user)
    return render(request, "index.html", locals())


def register_do(request):
    try:
        hashkey = CaptchaStore.generate_key()
        imgage_url = captcha_image_url(hashkey)
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = User.objects.create(email=register_form.cleaned_data["email"],
                                           username=register_form.cleaned_data["email"],
                                           password=register_form.cleaned_data["password"],
                                           is_active=False,)
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('/')
            else:
                return render(request, "register.html", register_form)
        else:
            register_form = RegisterForm()
    except Exception as e:
        logger.error(e)
    return render(request, "register.html", locals())


def login_do(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return redirect(request.POST.get('source_url'))
                else:
                    return render(request, 'login.html', {'reason': 'pwd_error'})
            else:
                return render(request, 'login.html', locals())
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, "login.html", locals())


def logout_do(request):
    try:
        logout(request)
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])


def ajax_val(request):
    if  request.is_ajax():
        cs = CaptchaStore.objects.filter(response=request.GET['response'],
                                     hashkey=request.GET['hashkey'])
        if cs:
            json_data={'status':1}
        else:
            json_data = {'status':0}
        return JsonResponse(json_data)
    else:
        # raise Http404
        json_data = {'status':0}
        return JsonResponse(json_data) #需要导入  from django.http import JsonResponse



