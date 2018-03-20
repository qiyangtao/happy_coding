# -*- coding:utf-8 -*-
from django.core.mail import send_mail # 发送邮件模块
from happy_coding.settings import *  # setting.py添加的的配置信息


if __name__ == "__main__":
    email_title = "注册激活链接"
    email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}"
    # 发送邮件
    send_status = send_mail(email_title, email_body, EMAIL_FROM, ['393082981@qq.com',])
    print (send_status)