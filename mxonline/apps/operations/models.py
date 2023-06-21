from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

COURSETYPE_CHOICES = (
    ("not_start", "未开始"),
    ("progressing", "正在进行"),
    ("endding", "已结束")
)


UserProfile = get_user_model()

class Banner(BaseModel):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=200, verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=0, verbose_name="顺序")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    
class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    comments = models.CharField(max_length=200, verbose_name="评论内容")
    like = models.IntegerField(verbose_name="点赞数",default=0)
    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.comments
    
class  CourseReply(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    comments = models.ForeignKey(CourseComments,on_delete=models.CASCADE, verbose_name="评论内容")
    reply = models.CharField(verbose_name="回复",max_length=200)
    like = models.IntegerField(verbose_name="点赞数",default=0)
    class Meta:
        verbose_name = "课程回复"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.reply


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

class UserAllCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名")
    last_click_time = models.DateTimeField(verbose_name="上次点击时间",null=True)
    is_required = models.BooleanField(verbose_name="是否必修",default=False)
    course_type = models.CharField(verbose_name="课程类别", max_length=20,choices=COURSETYPE_CHOICES)

    class Meta:
        verbose_name = "全部课程" 
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.course.name



