import xadmin

from apps.users.models import Department
from xadmin.layout import Fieldset, Main, Side, Row


class DepatmentAdmin(object):
    list_display = ['department']


xadmin.site.register(Department, DepatmentAdmin)