from django.http import HttpResponse
from django.shortcuts import render
from .models import resiger,new_resiger,MyBlog1
from django.contrib.auth.models import User
import random
def index(request):
    blog_all=MyBlog1.objects.all()
    blog_num=len(blog_all)
    for i in blog_all:
        blog=i.content
        title=i.title
    imgs=[
        "http://pic.netbian.com/uploads/allimg/171216/160104-15134112648908.jpg",
        "http://pic.netbian.com/uploads/allimg/180712/213018-1531402218fa16.jpg",
        "http://pic.netbian.com/uploads/allimg/180101/225655-1514818615716f.jpg",
        "http://pic.netbian.com/uploads/allimg/180822/094020-1534902020298c.jpg",
    ]
    id=random.randint(0, 3)
    imgs_url="http://pic.netbian.com/uploads/allimg/180822/094020-1534902020298c.jpg"
    print(imgs_url)
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
import markdown
from .models import *
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
    blog_all=MyBlog1.objects.all().filter(id=article_num)
    for i in blog_all:
        article_detiles = i.content
        article_title=i.title
    article_detiles = markdown.markdown(article_detiles, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc'  # 自动生成目录
    ])  # 修改blog.content内容为html
    return render(request,'pubu/article.html',{'article':article_detiles,'title':article_title})
