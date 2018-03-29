# _*_ encoding:utf-8 _*_
from django import forms
import re

from operation.models import UserAsk


# 咨询form
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]

    # 手机号码验证
    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        p = re.compile('^1[3|4|5|6|7|8]\d{9}$')
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码无效", code="mobile_invalid")