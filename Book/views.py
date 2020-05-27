from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.template import context
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

from Book.models import *


def index(request):
    allcategory = Category.objects.all()
    allbooks = Book.objects.all()
    context = {
        'allcategory': allcategory,
        'allbooks': allbooks,
    }

    return render(request, 'index base.html', context)


def categories(request):

    allcategory = Category.objects.all().order_by('index')
    allbooks = Book.objects.all().order_by('time')
    context = {
        'allcategory': allcategory,
        'allbooks': allbooks,
    }
    return render(request, 'categories.html', context)


def books_show(request):
    allbooks = Book.objects.all()
    context = {
        'allbooks': allbooks,
    }
    return render(request, 'product.html', context)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户名和密码，通过的话，返回User对象
        user = auth.authenticate(users=name, password=password)
        if user:

            auth.login(request, user)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        User.objects.create_user(users=name, password=password)
        return HttpResponseRedirect('login/')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('http://127.0.0.1:8000/')


def tag(request, category):
    list = Book.objects.filter(category__book=tag)  # 通过文章标签进行查询文章
    allcategory = Category.objects.all()
    tname = Category.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    return render(request, 'tags.html', locals())

