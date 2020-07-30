from django.http import HttpResponse
from django.shortcuts import render
from .models import resiger,new_resiger,MyBlog
from django.contrib.auth.models import User
def index(request):
    blog_all=MyBlog.objects.all()
    blog_num=len(blog_all)
    for i in blog_all:
        blog=i.content
        title=i.title
    return render(request,'pubu/index.html',{'blog01':blog,'title01':title,'blog_all':blog_all})
def resiger1(request):
    return render(request,'pubu/register.html')
def login(request):
    all = new_resiger.objects.all()
    uid = request.GET.get('username')
    pwd = request.GET.get('password')
    for i in all:
        if uid == i.uid and pwd==i.pwd:
            return render(request, "pubu/index.html")
    return HttpResponse("用户名或密码错误")
def save_uid(request):
    all=new_resiger.objects.all()
    uid=request.GET.get('username')
    pwd=request.GET.get('password')
    is_exist=False
    for i in all:
        if uid==i.uid:
           is_exist=True
    if not is_exist:
        user=new_resiger()
        user.uid=uid
        user.pwd=pwd
        user.save()
        is_resiger=True
    return  HttpResponse("用户名已存在") if is_exist else render(request,"pubu/resiger_success.html")
def swiper(request):
    return render(request,'pubu/text swiper.html')


def article(request):
    article_num=request.get_full_path().split('/')[2]
    blog_all=MyBlog.objects.all().filter(id=article_num)
    for i in blog_all:
        article_detiles=i.content
    return render(request,'pubu/article.html',{'article':article_detiles})
