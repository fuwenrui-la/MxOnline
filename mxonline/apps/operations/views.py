from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render

from apps.operations.forms import  CommentsForm
# UserFavForm,
from apps.operations.models import CourseComments
# UserFavorite, 
from apps.courses.models import Course
from apps.operations.models import UserAllCourse
from apps.users.models import Department

from django.http import HttpResponse

def trans(obj,attr):
    lis = []
    for n in obj:
        a = n[attr]
        lis.append(a)
    return lis


class IndexView(View):
    def get(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            user = request.user
            departments = Department.objects.all().order_by("id")
            arr = [1,2,3]
            is_learnings_mid = UserAllCourse.objects.values("course_id").filter(user=user).order_by("-course__fav_nums")[:3]
            course_id = trans(is_learnings_mid,"course_id")
            history_courses = Course.objects.values("id","name","if_required","image","teacher","tag").filter(id__in=course_id)
            num = 0
            for n in history_courses:
                n["num"] = arr[num]
                num = num+1
            required_courses_mid = UserAllCourse.objects.values("course_id").filter(user=user).order_by("-course__if_required","course__end_time")[:3]
            required_courses_id = trans(required_courses_mid,"course_id")
            required_courses = Course.objects.values("id","name","if_required","image","teacher","tag").filter(id__in=required_courses_id)
            hot_courses = Course.objects.values("id","name","if_required","image","teacher","tag").all().order_by("-fav_nums")[:3]
            return render(request, "index.html",{
                "departments":departments,
                "user":user,
                "history_courses":history_courses,
                "required_courses":required_courses,
                "hot_courses":hot_courses
            })
        else:
            return render(request, "403.html")
        
class CommentView(View):
    def post(self, request, *args, **kwargs):
        """
        用户收藏，取消收藏
        """
        if not request.user.is_authenticated:
            return JsonResponse({
                "status":"fail",
                "msg":"用户未登录"
            })

        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            course = comment_form.cleaned_data["course"]
            comments = comment_form.cleaned_data["comments"]

            comment = CourseComments()
            comment.user = request.user
            comment.comments = comments
            comment.course = course
            comment.save()

            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "参数错误"
            })


# class AddFavView(View):
#     def post(self, request, *args, **kwargs):
#         """
#         用户收藏，取消收藏
#         """
#         #先判断用户是否登录
#         if not request.user.is_authenticated:
#             return JsonResponse({
#                 "status":"fail",
#                 "msg":"用户未登录"
#             })

#         user_fav_form = UserFavForm(request.POST)
#         if user_fav_form.is_valid():
#             fav_id = user_fav_form.cleaned_data["fav_id"]
#             fav_type = user_fav_form.cleaned_data["fav_type"]

#             #是否已经收藏
#             existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
#             if existed_records:
#                 existed_records.delete()

#                 if fav_type == 1:
#                     course = Course.objects.get(id=fav_id)
#                     course.fav_nums -= 1
#                     course.save()
#                 elif fav_type == 2:
#                     course_org = CourseOrg.objects.get(id=fav_id)
#                     course_org.fav_nums -= 1
#                     course_org.save()
#                 elif fav_type == 3:
#                     teacher = Teacher.objects.get(id=fav_id)
#                     teacher.fav_nums -= 1
#                     teacher.save()

#                 return JsonResponse({
#                     "status": "success",
#                     "msg": "收藏"
#                 })
#             else:
#                 user_fav = UserFavorite()
#                 user_fav.fav_id = fav_id
#                 user_fav.fav_type = fav_type
#                 user_fav.user = request.user
#                 user_fav.save()

#                 return JsonResponse({
#                     "status": "success",
#                     "msg": "已收藏"
#                 })
#         else:
#             return JsonResponse({
#                 "status": "fail",
#                 "msg": "参数错误"
#             })




