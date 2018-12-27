"""
models
"""
from django.db import models


######################################
# Jenkins 构建环境
######################################
class JenkinsEnv(models.Model):
    name = models.CharField(verbose_name='环境名称', max_length=100, help_text="由于有些公司不只一个 Jenkins，该名称用于区分")
    url = models.CharField(verbose_name='URL地址', max_length=250, help_text="Jenkins 的访问地址")
    username = models.CharField(verbose_name='用户名', max_length=100, help_text="Jenkins 登录用户名")
    api_token = models.CharField(verbose_name='API Token', max_length=100,
                                 help_text="基于用户的 Token，在 Jenkins 登录后，点击右上角用户名，再点击左边的设置可以配置 Token")

    class Meta:
        verbose_name = 'Jenkins 平台'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 公司项目
######################################
class CompanyProject(models.Model):
    name = models.CharField(verbose_name='项目名称', max_length=100, unique=True, help_text="公司的项目名称，用于构建分类")

    class Meta:
        verbose_name = '公司项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 构建项目
######################################
class JenkinsProject(models.Model):
    jenkins_env = models.ForeignKey(JenkinsEnv, verbose_name='环境', related_name='jenkins_env', on_delete=models.CASCADE,
                                    help_text="配置任务所在的 Jenkins")
    company_project = models.ForeignKey(CompanyProject, verbose_name='项目', related_name='company_project',
                                        on_delete=models.CASCADE, help_text="配置任务所属的项目")
    name = models.CharField(verbose_name='名称', max_length=100, help_text="配置任务的名称，用于区分")
    project_name = models.CharField(verbose_name='构建任务名称', max_length=100, help_text="配置在 Jenkins 任务的全称")

    class Meta:
        verbose_name = '构建任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.company_project.name, self.name)
