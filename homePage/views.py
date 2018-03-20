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
    return render(request, "index.html", locals())


def register_do(request):
    try:
        mobile_hashkey = CaptchaStore.generate_key()
        email_hashkey = CaptchaStore.generate_key()
        mobile_imgage_url = captcha_image_url(mobile_hashkey)
        email_imgage_url = captcha_image_url(email_hashkey)
        if request.method == "POST":
            # 如果是手机注册
            if request.POST["type"] == "mobile":
                mobile_register_form = MobileRegisterForm(request.POST)
                if mobile_register_form.is_valid():
                    user = User.objects.create(mobile=mobile_register_form.cleaned_data["mobile"],
                                               username=mobile_register_form.cleaned_data["mobile"],
                                               password=make_password(mobile_register_form.cleaned_data["password"]),
                                               is_active=False,)
                    user.save()
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return redirect('/')
                else:
                    mobile_register_form = MobileRegisterForm(request.POST)
                    email_register_form = EmailRegisterForm()
                    return render(request, 'register.html', locals())
            # 如果是邮件注册
            else:
                email_register_form = EmailRegisterForm(request.POST)
                if email_register_form.is_valid():
                    user = User.objects.create(email=email_register_form.cleaned_data["email"],
                                               username=email_register_form.cleaned_data["email"],
                                               password=make_password(email_register_form.cleaned_data["password1"]),
                                               is_active=False,)
                    user.save()
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return redirect('/')
                else:
                    email_register_form = EmailRegisterForm(request.POST)
                    mobile_register_form = MobileRegisterForm()
                    return render(request, 'register.html', locals())
        else:
            mobile_register_form = MobileRegisterForm()
            email_register_form = EmailRegisterForm()
    except Exception as e:
        print(e)
    return render(request, 'register.html', locals())


def login_do(request):
    try:
        if request.method == 'POST':
            login_form = EmailRegisterForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(request, user)
                    return redirect(request.POST.get('source_url'))
                else:
                    reason = 'pwd_error'
                    return render(request, 'login.html', locals())
            else:
                return render(request, 'login.html', locals())
        else:
            login_form = EmailRegisterForm()
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



