# _*_ encoding:utf-8 _*_
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums', 'category',
                    'tag', 'youneed_know', 'teacher_tell', 'add_time']  # 列表显示
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums', 'category',
                    'tag', 'youneed_know', 'teacher_tell', 'add_time']


class CourseResourceCourseAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']  # 列表显示
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times', 'add_time']  # 列表显示
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'url', 'add_time']  # 列表显示
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceCourseAdmin)