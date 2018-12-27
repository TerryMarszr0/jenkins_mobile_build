"""
tags
"""
from jenkins_build.models import *
from django import template

register = template.Library()


######################################
# 获取平台
######################################
@register.simple_tag
def get_jenkins_platform(pro_id):
    return JenkinsProject.objects.filter(company_project_id=int(pro_id))
