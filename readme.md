# 通过control创建一般用户
from django.contrib.auth.models import User
User.objects.create_user('yang','yang@qq.com','123456')
#创建超级管理员
# python manage.py createsuperuser
判断用户是否具有某权限
request.user.has_perm('foo.add_bar)
强制权限验证
@permission_required('polls.can_vote')
def my_view(request):
    pass

user.check_password('原来的密码')
用于修改密码
user.set_password('新密码')
对用户进行扩展
在自设计的模型上加上django原来的模型数据
（替换现有的模型）
一、配置用户模型，告诉django框架
AUTH_USER_MODEL='oauth.User'
二、继承自AbstractUser抽象模型
三、添加字段，同步到数据模型数据库
四、admin的配置