# _*_ encoding:utf-8 _*_
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    user_bootswatch = True


class GlobalSettings(object):
    site_title = "暮学网后台管理系统"
    site_footer = "暮学在线"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type','send_time']  # 列表显示
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # 列表显示
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)