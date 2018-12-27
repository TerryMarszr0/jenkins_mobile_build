## Jenkins mobile build

### 1. 部署方式

Python 3 安装方法
> https://www.cnblogs.com/Dy1an/p/9649923.html

Django 部署方法
> https://www.cnblogs.com/Dy1an/p/9706628.html

### 项目说明

* 默认使用 sqlite 数据库，如果你需要使用 MySQL，只需要注释掉 ***jenkins_mobile_build/jenkins_mobile_build/settings.py*** 文件中 sqlite 放开并配置 MySQL 即可但是由于本服务很小且数据量并不大，体检使用 sqlite：

```python
# 自带数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '数据库',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': '用户名',
#         'PASSWORD': '密码',
#     }
# }
```

顺便一提，首页显示的公司名称可以到 settings.py 中配置！


* 当前 sqlite 中默认保存后台账户为 admin / 123456，修改可以去后台：
> http://你的地址/admin

* 为了项目尽量简单，没有单独的登录逻辑，这意味着你必须先登录后台，然后在使用首页

* 本项目总共三个业务表：
    Jenkins 平台：Jenkins 本身的信息，包括地址，用户名，API-Token 等
    公司项目：公司的项目，用于首页的分类显示
    构建任务：与前六个表存在主外键关系，配置具体想执行的任务的信息

* 由于本人的 Jenkins 构建自己配置了钉钉构建结果提示，所以该项目只作为手机上触发构建

* 如果你想在该平台上面提示构建结果，你需要自己再去写相关逻辑

### 效果图

![首页](https://github.com/PythonTra1nee/jenkins_mobile_build/blob/master/display/index.jpg?raw=true)