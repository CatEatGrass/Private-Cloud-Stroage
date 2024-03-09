# Create your views here.
from xml.dom import registerDOMImplementation
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

#主页面，可能要改一下
#@login_required
#def home_view(request):
#    return render(request, 'base.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('密码错误')
    return render(request, 'login/user_login.html')

def user_register(request):
    if request.method == "POST":
        form = registerDOMImplementation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')  # 设置成功消息
            return redirect('user_register')  # 重定向回注册页面以显示消息
    else:
        form = RegisterForm()
    return render(request, 'login/user_register.html', {'form': form})

