# -*- coding:utf-8 -*-
from models import User, EmailVerifyRecord
from django.views.generic.base import View
from django.shortcuts import render


class ActiveUserView(View):
    def get(self, request, active_code):
    # 用code在数据库中过滤处信息
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 通过邮箱查找到对应的用户
                user = User.objects.get(email=email)
                # 激活用户
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")