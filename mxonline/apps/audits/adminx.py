import xadmin
from django.db import models
from apps.audits.models  import VideoAudit,VideoDetailOpinion,DocumentAudit,DocumentDetailOpinion


class VideoAuditAdmin(object):
    list_display = ['user','video','last_audit_time','opinion']
    search_fields =  ['user','video','opinion']
    list_filter =  ['user','video','opinion']

class VideoDetailOpinionAdmin(object):
    list_display = ['video_audit','timestamp','opinion']
    search_fields =  ['video_audit','timestamp','opinion']
    list_filter =  ['video_audit','timestamp','opinion']
  
class DocumentAuditAdmin(object):
    list_display = ['user','document','last_audit_time','opinion']
    search_fields =  ['user','document','opinion']
    list_filter =  ['user','document','opinion']

class DocumentDetailOpinionAdmin(object):
    list_display = ['document_audit','number','opinion']
    search_fields =  ['document_audit','number','opinion']
    list_filter =  ['document_audit','number','opinion']


xadmin.site.register(VideoAudit,VideoAuditAdmin)
xadmin.site.register(VideoDetailOpinion,VideoDetailOpinionAdmin)
xadmin.site.register(DocumentAudit,DocumentAuditAdmin)
xadmin.site.register(DocumentDetailOpinion,DocumentDetailOpinionAdmin)