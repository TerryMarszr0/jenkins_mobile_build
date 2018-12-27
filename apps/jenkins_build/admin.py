"""
admin
"""
from django.contrib import admin
from .models import *


######################################
# 后台注册
######################################
admin.site.register(JenkinsEnv)
admin.site.register(CompanyProject)
admin.site.register(JenkinsProject)
