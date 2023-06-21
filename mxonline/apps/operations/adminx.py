import xadmin

from apps.operations.models import  Banner,CourseComments,CourseReply, UserMessage,UserAllCourse


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', "index"]
    search_fields = ['title', 'image', 'url', "index"]
    list_filter = ['title', 'image', 'url', "index"]


class UserAllCourseAdmin(object):
    list_display = ['user', 'course', 'course_type']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'course_type']

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class CourseReplyAdmin(object):
    list_display = ['user', 'comments', 'reply', 'add_time']
    search_fields = ['user', 'comments', 'reply']
    list_filter = ['user', 'comments', 'reply', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(UserAllCourse, UserAllCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(CourseReply, CourseReplyAdmin)