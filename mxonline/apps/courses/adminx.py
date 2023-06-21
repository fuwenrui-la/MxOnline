import xadmin

from apps.courses.models import Course,EvaluteItem, Chapter,Section,Standard, Video, BannerCourse, CourseResource, CourseTag,CourseResource
from xadmin.layout import Fieldset, Main, Side, Row

class GlobalSettings(object):
    site_title = "城交院教育平台"
    site_footer = "慕学在线网"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class ChapterInline(object):
    model = Chapter
    # style = "tab"
    extra = 0
    exclude = ["add_time"]


class CourseResourceInline(object):
    model = CourseResource
    style = "tab"
    extra = 1




class CourseAdmin(object):
    list_display = ['name', 'introduce',  'learn_times', 'students']
    search_fields = ['name', 'introduce',  'students']
    list_filter = ['name', 'teacher', 'introduce',  'learn_times', 'students']
    list_editable = ["desc"]


class BannerCourseAdmin(object):
    list_display = ['name', 'introduce', 'learn_times', 'students']
    search_fields = ['name', 'introduce',  'students']
    list_filter = ['name', 'introduce',  'learn_times', 'students']
    list_editable = ["introduce"]

from import_export import resources

class MyResource(resources.ModelResource):
    class Meta:
        model = Course
        # fields = ('name', 'description',)
        # exclude = ()


#固定的ip
#1. 本地的ip是一个动态分配的ip地址
#2. 数据包转发问题 scp
class NewCourseAdmin(object):
    import_export_args = {'import_resource_class': MyResource, 'export_resource_class': MyResource}
    list_display = ['name', 'introduce', 'show_image', 'go_to', 'learn_times', 'students']
    search_fields = ['name', 'introduce',  'students']
    list_filter = ['name', 'name', 'introduce', 'learn_times', 'students']
    list_editable = ["introduce"]
    readonly_fields = ["students", "add_time"]
    # exclude = ["click_nums", "fav_nums"
    model_icon = 'fa fa-address-book'
    inlines = [ChapterInline]
   



class ChapterAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

class SectionAdmin(object):
    list_display = ['chapter', 'name', 'add_time']
    search_fields = ['chapter', 'name']
    list_filter = ['chapter__name', 'name', 'add_time']

class EvaluteItemAdmin(object):
    list_display = ['evalute_type']

class StandardAdmin(object):
    list_display = ["course","evalute_item","evalute_standard","proportion"]
    search_fields = ["course","evalute_item","evalute_standard","proportion"]
    list_filter = ["course__name","evalute_standard","proportion"]


class VideoAdmin(object):
    list_display = ['section', 'name', 'add_time']
    search_fields = ['section', 'name']
    list_filter = ['section', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['section', 'name', 'file', 'add_time']
    search_fields = ['section', 'name', 'file']
    list_filter = ['section', 'name', 'file', 'add_time']


class CourseTagAdmin(object):
    list_display = ['course', 'tag','add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag','add_time']

# xadmin.site.register(Course, CourseAdmin)

xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Course, NewCourseAdmin)
xadmin.site.register(EvaluteItem, EvaluteItemAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Section, SectionAdmin)
xadmin.site.register(Standard, StandardAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)
# xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
# xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)