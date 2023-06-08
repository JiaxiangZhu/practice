from django.contrib import admin
# 导入模型
from .models import BookInfo, PeopleInfo
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
