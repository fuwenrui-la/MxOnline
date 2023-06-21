from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)

class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True

class Department(BaseModel):
    department = models.CharField(max_length=25,verbose_name="专业",unique=True)
    department_tag= models.CharField(max_length=25,verbose_name="专业标签",default="")
    
    class Meta:
        verbose_name = "课程专业"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.department

class UserProfile(AbstractUser):
    name = models.CharField(max_length=50, verbose_name="姓名", default="")
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    mobile = models.CharField(max_length=11, verbose_name="手机号码", default="")
    employee_id = models.CharField(max_length=15,verbose_name="工号", default="") 
    department = models.ForeignKey(Department,verbose_name="部门",on_delete=models.CASCADE,null=True)
    image = models.ImageField(verbose_name="用户头像", upload_to="head_image/%Y/%m", default="default.jpg")
    is_expert = models.BooleanField(verbose_name="是否为专家",default=False)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def unread_nums(self):
        #未读消息数量
        return self.usermessage_set.filter(has_read=False).count()

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username

