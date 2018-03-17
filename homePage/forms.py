# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"required": "required", }),
                               max_length=30, error_messages={"required": "用户名不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"required": "required", }),
                               max_length=30, error_messages={"required": "密码不能为空"})


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    captcha = CaptchaField()
