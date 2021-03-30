from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserLoginForm, UserRegisterForm
from accounts.models import User
from utils import constants
from utils.verify import VerifyCode


def user_login(request):
    """用户登录"""
    if request.method == 'POST':
        # 这个form是得到前台传过来的数据,这里得到的是字典对象的数据
        form = UserLoginForm(request=request, data=request.POST)
        print(request.POST)
        client = VerifyCode(request)
        """前端得到的验证码"""
        code = request.POST.get('verify_code', None)
        rest = client.validate_code(code)
        print("验证结果", rest)
        # 表单是否通过验证
        if form.is_valid():
            print('验证通过')
            # 执行登录
            # 使用自定义方式实现登录
            data = form.cleaned_data
            # user = User.objects.get(username=data['username'], password=data['password'])
            # # 设置用户ID到session
            # request.session[constants.LOGIN_SESSION_ID] = user.id
            # return redirect('index')
            # 使用django-auth方式实现登录
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                # 登录后的跳转
                return redirect('index')

        else:
            print(form.errors)
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {
        'form': form
    })


def user_logout(request):
    """用户退出"""
    logout(request)
    return redirect('index')


def user_register(request):
    """用户注册"""
    """拿到用户注册表单的对象渲染到前端"""
    if request.method == 'POST':
        form = UserRegisterForm(request=request, data=request.POST)
        if form.is_valid():
            # 调用注册方法
            form.register()
            return redirect('account:user_login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm(request=request)
    return render(request, 'register.html', {
        'form': form
    })
