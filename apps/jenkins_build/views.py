"""
views Configuration
"""
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from jenkins_mobile_build.settings import COMPANY_NAME
from .models import *
import jenkins
from utils.login_check import LoginStatusCheck


######################################
# 发布页面
######################################
class IndexView(LoginStatusCheck, View):
    def get(self, request):
        company_name = COMPANY_NAME

        # 获取所有项目
        all_projects = CompanyProject.objects.all()

        context = {
            'company_name': company_name,
            'all_projects': all_projects,
        }

        return render(request, 'index.html', context=context)


######################################
# 系统构建
######################################
class JenkinsBuildView(LoginStatusCheck, View):
    def post(self, request):
        try:
            # 查找对应的项目
            jenkins_project_id = request.POST.get("jenkins_project_id")
            jenkins_project = JenkinsProject.objects.get(id=int(jenkins_project_id))

            # 定义 Jenkins 信息
            jenkins_url = jenkins_project.jenkins_env.url
            jenkins_username = jenkins_project.jenkins_env.username
            jenkins_password = jenkins_project.jenkins_env.api_token
            jenkins_job_name = jenkins_project.project_name

            # 实例化 Jenkins
            server = jenkins.Jenkins(url=jenkins_url, username=jenkins_username, password=jenkins_password)

            # 构建参数
            parm_dict = dict()
            parm_list = server.get_job_info(jenkins_job_name)['actions'][0]['parameterDefinitions']
            if len(parm_list):
                for i in parm_list:
                    name = i['name']
                    value = i['defaultParameterValue']['value']
                    parm_dict[name] = value

            # 获取本次构建的 ID
            jenkins_build_number = server.get_job_info(jenkins_job_name)['nextBuildNumber']

            # 开始构建
            server.build_job(jenkins_job_name, parm_dict)
            return HttpResponse('{"status":"success", "msg":"构建已经触发，请关注钉钉构建结果！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"未知错误！"}', content_type='application/json')
