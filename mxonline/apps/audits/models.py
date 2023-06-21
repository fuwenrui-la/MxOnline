from django.db import models
from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel
from django.contrib.auth import get_user_model
from apps.courses.models import Video,CourseResource

UserProfile = get_user_model()

class VideoAudit(BaseModel):
    user = models.ForeignKey(UserProfile,verbose_name="上传人", on_delete=models.CASCADE,null=True)
    video = models.OneToOneField(Video,on_delete=models.CASCADE,null=True)
    last_audit_time =models.DateField(verbose_name="上次审核时间",null=True)
    opinion = models.CharField(verbose_name="整体修改意见",default='',max_length=1000)
    class Meta:
        verbose_name = "视频审核"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.opinion


class VideoDetailOpinion(BaseModel):
    video_audit = models.ForeignKey(VideoAudit,verbose_name="审核视频",on_delete=models.CASCADE,null=True)
    timestamp = models.CharField(verbose_name="时间点",max_length=10)
    opinion = models.CharField(verbose_name="细节修改意见",default="",max_length=300)
    class Meta:
        verbose_name = "视频审核细节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.opinion
    
class DocumentAudit(BaseModel):
    user = models.ForeignKey(UserProfile,verbose_name="上传人", on_delete=models.CASCADE,null=True)
    document = models.OneToOneField(CourseResource,on_delete=models.CASCADE,null=True)
    last_audit_time =models.DateField(verbose_name="上次审核时间",null=True)
    opinion = models.CharField(verbose_name="整体修改意见",default="",max_length=1000)
    class Meta:
        verbose_name = "文档审核"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.opinion
    
class DocumentDetailOpinion(BaseModel):
    document_audit = models.ForeignKey(DocumentAudit,verbose_name="审核文档",on_delete=models.CASCADE,null=True)
    number = models.IntegerField(verbose_name="序号")
    opinion = models.CharField(verbose_name="细节修改意见",default="",max_length=300)    
    class Meta:
        verbose_name = "文档审核细节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.opinion
    

