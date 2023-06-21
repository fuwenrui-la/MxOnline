from datetime import datetime

from django.db import models

from apps.users.models import BaseModel,UserProfile, Department

from DjangoUeditor.models import UEditorField

#1. 设计表结构有几个重要的点
"""
实体1 <关系> 实体2
课程 章节 视频 课程资源
"""
#2. 实体的具体字段

#3. 每个字段的类型，是否必填


class Course(BaseModel):
    user = models.ForeignKey(UserProfile,verbose_name="上传人", on_delete=models.CASCADE,null=True)
    teacher = models.CharField(verbose_name="讲师",  max_length=15,default="")
    name = models.CharField(verbose_name="课程名", max_length=50)
    introduce= models.TextField(verbose_name="课程描述",default="")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name='学习人数')   
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="课程专业",null=True)
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    end_time = models.DateTimeField(verbose_name="结束时间",null=True)
    if_required = models.BooleanField(default=False,verbose_name="是否必修")
    if_only_department = models.BooleanField(default=False,verbose_name="是否专业必修")
    
    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name 

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()

    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<img src='{}'>".format(self.image.url))
    show_image.short_description = "图片"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/course/{}'>跳转</a>".format(self.id))
    go_to.short_description = "跳转"

class EvaluteItem(BaseModel):
    evalute_type = models.CharField(max_length=10,verbose_name="评分项")
    
    class Meta:
        verbose_name = "评分项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.evalute_type

class Standard(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    evalute_item = models.ForeignKey(EvaluteItem,on_delete=models.CASCADE, verbose_name="评分项")
    evalute_standard = models.CharField(max_length=30,verbose_name="评分标准")
    proportion = models.IntegerField(default=0, verbose_name="分值占比")
    class Meta:
        verbose_name = "评分标准"
        verbose_name_plural = verbose_name
    


class BannerCourse(Course):
    
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    tag = models.CharField(max_length=100, verbose_name="标签")

    class Meta:
        verbose_name = "课程标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Chapter(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程",null=True)  #on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name="章")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# class Section(BaseModel):
#     section = models.
class Section(BaseModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name="章",null=True)  #on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name="节")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")


    class Meta:
        verbose_name = "课程节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
class Video(BaseModel):
    section = models.ForeignKey(Section, verbose_name="节", on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=1000, verbose_name=u"访问地址")
    is_audit = models.BooleanField(verbose_name="是否通过审核",default=False)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="课程",null=True)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    file = models.FileField(upload_to="course/resourse/%Y/%m", verbose_name="下载地址", max_length=200)
    is_audit = models.BooleanField(verbose_name="是否通过审核",default=False)
    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
