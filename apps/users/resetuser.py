# -*- coding:utf-8 -*-
from models import User, EmailVerifyRecord
from django.views.generic.base import View
from django.shortcuts import render


class ResetUserView(View):
    def get(self, request, reset_code):
    # 用code在数据库中过滤处信息
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 通过邮箱查找到对应的用户
                return render(request, "password_reset.html", locals())
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")