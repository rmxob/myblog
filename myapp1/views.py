from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import resiger,new_resiger,MyBlog
from django.contrib.auth.models import User
import random
import json
#首页
def index(request):
    blog_all=MyBlog.objects.all()
    blog_num=len(blog_all)
    for i in blog_all:
        blog=i.content
        title=i.title
    return HttpResponse("你还没有一篇文章") if blog_num==0 else render(request,'pubu/index.html',{'blog01':blog,'title01':title,'blog_all':blog_all})
#注册
def resiger1(request):
    return render(request,'pubu/register.html')
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect
#登录
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
    s = request.session.get("flag", True)
    if s == False:
        str = "验证码错误，注册失败"
        request.session.clear()
        return HttpResponse(str)
    code1 = request.GET.get("verifycode").upper()
    code2 = request.session["verify"].upper()
    if code1 == code2:
        return render(request, 'pubu/resiger_success.html')
    else:
        request.session["flag"] = False
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
def now_login(request):
    return render(request,"pubu/resiger_success.html")
def article(request):
    article_num=request.get_full_path().split('/')[2]
    blog_all=MyBlog.objects.all().filter(id=article_num)
    for i in blog_all:
        article_detiles = i.content
    article_fontnums=len(article_detiles)
    md=markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    article_detiles=md.convert(article_detiles)
    article_markdown=article_detiles
    article_view = MyBlog.objects.get(id=article_num)
    # 浏览量 +1
    article_view.total_views += 1
    article_view.save(update_fields=['total_views'])
    return render(request,'pubu/articles.html',{'article':article_markdown,'article_fontnums':article_fontnums,'toc':md.toc,'blog_all':blog_all})
def time(request):
    blog_all = MyBlog.objects.all()
    blog_num = len(blog_all)
    for i in blog_all:
        blog = i.content
        title = i.title
    return render(request,'time/index.html',{'blog_all':blog_all})
def main(request):
    cloum_num=request.get_full_path().split('/')[2]
    blog_all = MyBlog.objects.all().filter(column_id=cloum_num)
    for i in range(len(blog_all)):
        blog_all[i].content=markdown.markdown(blog_all[i].content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc'  # 自动生成目录
    ]) # 修改blog.content内容为html
    return render(request,'pubu/main.html',{'blog_list':blog_all})

from django.core.paginator import Paginator
def main_all(request):
    blog_all = MyBlog.objects.all()
    for i in range(len(blog_all)):
            blog_all[i].content=markdown.markdown( blog_all[i].content[0:260], extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
             ])
    blog_all=blog_all[::-1]
    return render(request, 'pubu/main.html', {'blog_list': blog_all})











# 验证码
def verifycode(request):
   from PIL import Image,ImageDraw,ImageFont
   import  random
   bgcolor=(random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
   width=100
   height=50
   im=Image.new('RGB',(width,height),bgcolor)
   draw=ImageDraw.Draw(im)
   for i in range(0,100):
       xy=(random.randrange(0,width),random.randrange(0,height))
       fill=(random.randrange(0,255),255,random.randrange(0,255))
       draw.point(xy,fill=fill)
   str='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKL'
   rand_str=''
   for i in range(0,4):
       rand_str+=str[random.randrange(0,len(str))]
   font=ImageFont.truetype(r'‪C:\Windows\Fonts\arial.ttf',40)
   fontcolor1=(255,random.randrange(0,255),random.randrange(0,255))
   fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
   fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
   fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
   draw.text((5,2),rand_str[0],font=font,fill=fontcolor1)
   draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
   draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
   draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
   del draw
   request.session['verify']=rand_str
   import  io
   buf=io.BytesIO()
   im.save(buf,'png')
   return HttpResponse(buf.getvalue(),'image/png')