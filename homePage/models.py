# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True,
                               null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=10, choices=(("register", u"注册"), ("forget", u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now())

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)
