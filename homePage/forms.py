# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from models import User
from django.core.validators import RegexValidator


# 登录form
class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.TextInput(attrs={"id":"account_l", "placeholder": "请输入您的邮箱", }, ),
                                max_length=30, error_messages={"required": "用户名不能为空", "invalid": "邮箱格式不正确"})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"password_l", "placeholder": "请输入您的密码" }),
                               max_length=30, error_messages={"required": "密码不能为空"})

    # 验证用户是否存在
    def clean_username(self):
        try:
            username = self.cleaned_data.get("username")
            user = User.objects.filter(username=username).first()
            if not user:
                self._errors["username"] = self.error_class(["用户名不存在！"])
        except Exception as e:
            pass
        return username


# 邮箱注册form
class EmailRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"id": "id_email", "placeholder": "请输入您的邮箱地址", }, ),
                             max_length=30, error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式不正确"})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"id":"id_password1", "placeholder": "请输入8-20位非中文字符密码" }, render_value=True),
                                max_length=30, min_length=8, error_messages={"required": "密码不能为空", "min_length": '密码长度不能少于8' },
                                # validators=[
                                # # 下面的正则内容一目了然，我就不注释了
                                # RegexValidator(r'((?=.*\d))^.{6,12}$', '必须包含数字'),
                                # RegexValidator(r'((?=.*[a-zA-Z]))^.{6,12}$', '必须包含字母'),
                                # RegexValidator(r'((?=.*[^a-zA-Z0-9]))^.{6,12}$', '必须包含特殊字符'),
                                # RegexValidator(r'^.(\S){6,10}$', '密码不能包含空白字符'),
                                # ], #用于对密码的正则验证)
                                )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"id":"id_password2", "placeholder": "请再次输入密码" },  render_value=True),
                                max_length=30, error_messages={"required": "确认密码不能为空"})
    captcha_1 = forms.CharField(widget=forms.TextInput(attrs={"id":"id_reg_captcha_1", "placeholder": "请输入验证码",
                                                              "class": "form-control form-control-captcha fl"}),
                                max_length=8, error_messages={"required": "验证码不能为空"})
    captcha = CaptchaField()

    # 验证邮箱是否注册过
    def clean_email(self):
        try:
            email = self.cleaned_data.get("email")
            user = User.objects.filter(email=email).first()
            if user:
                self._errors["email"] = self.error_class(["该邮箱已被注册过！"])
        except Exception as e:
            pass
        return email

    # 验证两次密码是否一致
    def clean_email_password2(self):
        try:
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 != password2:
                self._errors["password2"] = self.error_class(["两次密码输入不一致！"])
        except Exception as e:
            print(password1 != password2)
        return password2


# 手机注册form
class MobileRegisterForm(forms.Form):
    mobile = forms.CharField(widget=forms.TextInput(attrs={"id": "jsRegMobile", "placeholder": "请输入您的手机号码", "name": "account"}, ),
                               error_messages={"required": "手机号不能为空"},
                               validators=[RegexValidator(r'^[1][3,4,5,7,8][0-9]{9}$', '请输入正确的手机号')])
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"jsPhoneRegPwd1", "placeholder": "请输入8-20位非中文字符密码" }, render_value=True),
                                max_length=30, min_length=8, error_messages={"required": "密码不能为空", "min_length": '密码长度不能少于8' },
                                # validators=[
                                # # 下面的正则内容一目了然，我就不注释了
                                # RegexValidator(r'((?=.*\d))^.{6,12}$', '必须包含数字'),
                                # RegexValidator(r'((?=.*[a-zA-Z]))^.{6,12}$', '必须包含字母'),
                                # RegexValidator(r'((?=.*[^a-zA-Z0-9]))^.{6,12}$', '必须包含特殊字符'),
                                # RegexValidator(r'^.(\S){6,10}$', '密码不能包含空白字符'),
                                # ], #用于对密码的正则验证)
                                )
    sms = forms.IntegerField(widget=forms.TextInput(attrs={"id": "jsPhoneRegCaptcha", "placeholder": "请输入短信验证码","name": "mobile_code" }, ),
                               error_messages={"required": "请输入短信验证码"},
                               validators=[RegexValidator(r'^[0-9]{6}$', '请输入正确的短信验证码'),])
    captcha_1 = forms.CharField(widget=forms.TextInput(attrs={"id":"mobile-register-captcha_1", "placeholder": "请输入验证码","name":"captcha_m_1",
                                                              "autocomplete":"off","class": "form-control-captcha mobile-register-captcha"}),
                                max_length=8, error_messages={"required": "验证码不能为空"})
    captcha = CaptchaField()

    # 验证手机是否注册过
    def clean_email(self):
        try:
            mobile = self.cleaned_data.get("mobile")
            user = User.objects.filter(mobile=mobile).first()
            if user:
                self._errors["mobile"] = self.error_class(["该手机号已被注册过！"])
        except Exception as e:
            pass
        return mobile
