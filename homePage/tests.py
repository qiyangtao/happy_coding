# -*- coding:utf-8 -*-
from random import Random
from django.core.cache import cache
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


# 生成随机字符串
def random_str(random_length=6):
    sms_str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        sms_str += chars[random.randint(0, length)]
    return sms_str


if __name__ == "__main__":
    try:
        phone_numbers = [18502872291]
        sms_str = random_str(6)
        cache.set(18502872291, sms_str)
        appid = 1400076616
        appkey = '09763fbca1dc0c93de646671f07082ff'
        template_id = 97608
        tel = 'testNum'
        params = [sms_str, 3, 'tel']
        ssender = SmsSingleSender(appid, appkey)
        content = format("【畅编网】：您的注册验证为s%"%sms_str)
        result = ssender.send(86, phone_numbers[0],
                              template_id, params)
        if result ==0:
            cache.set(phone_numbers,sms_str)
        print(result)
    except Exception as e:
        pass
