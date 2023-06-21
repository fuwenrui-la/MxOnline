from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from apps.courses.models import Course,Standard,EvaluteItem,Chapter,Section, CourseTag, CourseResource, Video
from apps.operations.models import  CourseComments

def trans(obj,attr):
    lis = []
    for n in obj:
        a = n[attr]
        lis.append(a)
    return lis

class CourseIntroduceView(View):
    def get(self,request,course_id,*args, **kwargs):
        if  request.user.is_authenticated:
            user = request.user
            courses_detail = Course.objects.values("id","name","if_required","image","teacher","tag","introduce").filter(id__in=course_id)
            return render(request, "course-introduce.html",{
               "courses_detail" : courses_detail[0]
            })
        return render(request, "403.html")

    
class CourseStandardView(View):
    def get(self,request,course_id,*args, **kwargs):
        if  request.user.is_authenticated:   
            user = request.user
            courses_detail = Course.objects.values("id","name","if_required","image","teacher","tag","introduce").filter(id__in=course_id)
            courses_evaluteitem =EvaluteItem.objects.values("id","evalute_type")
            courses_standard_detail = Standard.objects.values("evalute_item","evalute_standard","proportion").filter(course_id=courses_detail[0]["id"])
            for i in courses_standard_detail:
                id = i['evalute_item']
                for n in courses_evaluteitem:
                    if n["id"] == id:
                        i['evalute_item'] = n["evalute_type"]
            print(courses_standard_detail)
            return render(request, "course-standard.html",{
                "courses_detail" : courses_detail[0],
                "courses_standard_detail":courses_standard_detail
            })
        return render(request, "403.html") 

class CourseContentView(View):
    def get(self,request,course_id,*args, **kwargs):
        if  request.user.is_authenticated:   
            user = request.user
            courses_detail = Course.objects.values("id","name","if_required","image","teacher","tag","introduce").filter(id__in=course_id)
            chapter = Chapter.objects.values("id", "name","course_id").filter(course_id=course_id)
            chp_id = trans(chapter,"id")
            section = Section.objects.values("id","name","chapter_id").filter(chapter_id__in=chp_id).order_by("name")
            print(section)
            return render(request, "course-content.html",{
                "courses_detail" : courses_detail[0],
                "chapter":chapter,
                "section":section
            })
        return render(request, "403.html") 

class CourseVideoView(View):
    def get(self,request,course_id,chapter_id,section_id,*args, **kwargs):


        if  request.user.is_authenticated:   
            return render(request, "course-video-detail.html",{
                
            })
        return render(request, "403.html") 
    
class CourseAssignmentView(View):
    def get(self,request,course_id,*args, **kwargs):
        if  request.user.is_authenticated:   
            user = request.user
            courses_detail = Course.objects.values("id","name","if_required","image","teacher","tag","introduce").filter(id__in=course_id)
            
            return render(request, "course-assignment.html",{
                "courses_detail" : courses_detail[0]
            })
        return render(request, "403.html") 
    
class CourseExamView(View):
    def get(self,request,course_id,*args, **kwargs):
        if  request.user.is_authenticated:   
            user = request.user
            courses_detail = Course.objects.values("id","name","if_required","image","teacher","tag","introduce").filter(id__in=course_id)
            return render(request, "course-exam.html",{
                "courses_detail" : courses_detail[0]
            })
        return render(request, "403.html") 
# ,UserFavorite, UserCourse,
# class VideoView(LoginRequiredMixin, View):
#     login_url = "/login/"

    # def get(self, request, course_id, video_id, *args, **kwargs):
    #     """
    #     获取课程章节信息
    #     """
    #     course = Course.objects.get(id=int(course_id))
    #     course.click_nums += 1
    #     course.save()

    #     video = Video.objects.get(id=int(video_id))

    #     #查询用户是否已经关联了该课程
    #     user_courses = UserCourse.objects.filter(user=request.user, course=course)
    #     if not user_courses:
    #         user_course = UserCourse(user=request.user, course=course)
    #         user_course.save()

    #         course.students += 1
    #         course.save()

        # #学习过该课程的所有同学
        # user_courses = UserCourse.objects.filter(course=course)
        # user_ids = [user_course.user.id for user_course in user_courses]
        # all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # # related_courses = [user_course.course for user_course in all_courses if user_course.course.id != course.id]
        # related_courses = []
        # for item in all_courses:
        #     if item.course.id != course.id:
        #         related_courses.append(item.course)

        # course_resources = CourseResource.objects.filter(course=course)

        # return render(request, "course-play.html", {
        #     "course": course,
        #     "course_resources":course_resources,
        #     "related_courses":related_courses,
        #     "video":video,
        # })
    
# class CourseCommentsView(LoginRequiredMixin, View):
#     login_url = "/login/"

#     def get(self, request, course_id, *args, **kwargs):
#         course = Course.objects.get(id=int(course_id))
#         course.click_nums += 1
#         course.save()

#         comments = CourseComments.objects.filter(course=course)

#         # 查询用户是否已经关联了该课程
#         user_courses = UserCourse.objects.filter(user=request.user, course=course)
#         if not user_courses:
#             user_course = UserCourse(user=request.user, course=course)
#             user_course.save()

#             course.students += 1
#             course.save()

#         # 学习过该课程的所有同学
#         user_courses = UserCourse.objects.filter(course=course)
#         user_ids = [user_course.user.id for user_course in user_courses]
#         all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
#         # related_courses = [user_course.course for user_course in all_courses if user_course.course.id != course.id]
#         related_courses = []
#         for item in all_courses:
#             if item.course.id != course.id:
#                 related_courses.append(item.course)

#         course_resources = CourseResource.objects.filter(course=course)

#         return render(request, "course-comment.html", {
#             "course": course,
#             "course_resources": course_resources,
#             "related_courses": related_courses,
#             "comments":comments
#         })


# class CourseLessonView(LoginRequiredMixin, View):
#     login_url = "/login/"

#     def get(self, request, course_id, *args, **kwargs):
#         """
#         获取课程章节信息
#         """
#         course = Course.objects.get(id=int(course_id))
#         course.click_nums += 1
#         course.save()

        #1. 用户和课程之间的关联
        #2. 对view进行login登录的验证
        #3. 其他课程

        #查询用户是否已经关联了该课程
        # user_courses = UserCourse.objects.filter(user=request.user, course=course)
        # if not user_courses:
        #     user_course = UserCourse(user=request.user, course=course)
        #     user_course.save()

        #     course.students += 1
        #     course.save()

        # #学习过该课程的所有同学
        # user_courses = UserCourse.objects.filter(course=course)
        # user_ids = [user_course.user.id for user_course in user_courses]
        # all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # # related_courses = [user_course.course for user_course in all_courses if user_course.course.id != course.id]
        # related_courses = []
        # for item in all_courses:
        #     if item.course.id != course.id:
        #         related_courses.append(item.course)

        # course_resources = CourseResource.objects.filter(course=course)

        # return render(request, "course-video.html", {
        #     "course": course,
        #     "course_resources":course_resources,
        #     "related_courses":related_courses
        # })

# class CourseDetailView(View):
#     def get(self, request, course_id, *args, **kwargs):
#         """
#         获取课程详情
#         """
#         course = Course.objects.get(id=int(course_id))
#         course.click_nums += 1
#         course.save()

#         #获取收藏状态
#         has_fav_course = False
#         has_fav_org = False
#         if request.user.is_authenticated:
#             if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
#                 has_fav_course = True
#             if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
#                 has_fav_org = True

#         #通过课程的tag做课程的推荐
#         # tag = course.tag
#         # related_courses = []
#         # if tag:
#         #     related_courses = Course.objects.filter(tag=tag).exclude(id__in=[course.id])[:3]

#         tags = course.coursetag_set.all()
#         tag_list = [tag.tag for tag in tags]

#         course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
#         related_courses = set()
#         for course_tag in course_tags:
#             related_courses.add(course_tag.course)

#         return render(request, "course-detail.html", {
#             "course":course,
#             "has_fav_course":has_fav_course,
#             "has_fav_org":has_fav_org,
#             "related_courses":related_courses
#         })


# class CourseListView(View):
#     def get(self, request, *args, **kwargs):
#         """获取课程列表信息"""
#         all_courses = Course.objects.order_by("-add_time")
#         hot_courses = Course.objects.order_by("-click_nums")[:3]

#         #搜索关键词
#         keywords = request.GET.get("keywords", "")
#         s_type = "course"
#         if keywords:
#             all_courses = all_courses.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(desc__icontains=keywords))

#         #课程排序
#         sort = request.GET.get("sort", "")
#         if sort == "students":
#             all_courses = all_courses.order_by("-students")
#         elif sort == "hot":
#             all_courses = all_courses.order_by("-click_nums")

#         # 对课程机构数据进行分页
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1

#         p = Paginator(all_courses, per_page=1, request=request)
#         courses = p.page(page)

#         return render(request, "course-list.html", {
#             "all_courses":courses,
#             "sort":sort,
#             "hot_courses":hot_courses,
#             "keywords":keywords,
#             "s_type":s_type
#         })

