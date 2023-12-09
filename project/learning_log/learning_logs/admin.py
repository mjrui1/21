from django.contrib import admin

# Register your models here.

# 向管理网站注册模型Topic, Entry
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

