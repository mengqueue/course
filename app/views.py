from time import sleep

from django.contrib.auth import authenticate
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from django.views.decorators.cache import cache_page

from app.models import User, Course


def index(request):
    username = request.user
    # locals()返回字典类型的所有局部变量（这里是{'username':username}）
    return render(request, 'user/index.html', locals())


def login(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        n = authenticate(username=username, password=password)
        # 登录成功，获得当前登录数据，返回主页
        if n:
            login(request, user=n)
            return redirect('/')
    # 登录失败，重新回到登录页
    return render(request, 'user/login.html')


def logout(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        # 校验，用户名不可重复
        uname = User.objects.filter(uname=username).first()
        if uname:
            info = "该用户名已被注册"
            return render(request, 'user/ERROR.html', {'info': info})
        # 注册成功，增添一条用户信息，回到登录页面
        else:
            user = User()
            user.uname = username
            user.upassword = password
            user.save()
            return render(request, 'user/login.html')
    # 注册失败，重新注册
    return render(request, 'user/register.html')


# 使用缓存
# @cache_page(30)
def course_list(request):
    # 渲染页面前首先查找缓存里面有没有相应的数据
    result = cache.get("course_list")
    # 有，直接读出
    if result:
        return HttpResponse(result)
    # 无，从数据库调出并且存入缓存
    courses = Course.objects.all()
    # 假设多耗时5s
    sleep(5)
    data = {
        "courses": courses
    }
    response = render(request, 'course/course_list.html', context=data)

    cache.set("course_list", response.content, timeout=60)
    return response


def search(request):
    return HttpResponse("欢迎访问该页面")


