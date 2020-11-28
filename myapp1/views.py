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
# 验证码
def verifycode(request):
   from PIL import Image,ImageDraw,ImageFont
   #from PIL.Image import point
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
# 判断设备信息
import re
def judge_pc_or_mobile(ua):
    factor = ua
    is_mobile = False

    _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp' \
                    r'|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)' \
                    r'|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    _long_matches = re.compile(_long_matches, re.IGNORECASE)
    _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)' \
                     r'|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)' \
                     r'|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw' \
                     r'|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8' \
                     r'|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit' \
                     r'|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)' \
                     r'|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji' \
                     r'|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx' \
                     r'|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi' \
                     r'|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)' \
                     r'|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg' \
                     r'|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21' \
                     r'|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-' \
                     r'|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it' \
                     r'|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)' \
                     r'|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)' \
                     r'|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit' \
                     r'|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'

    _short_matches = re.compile(_short_matches, re.IGNORECASE)

    if _long_matches.search(factor) != None:
        is_mobile = True
    user_agent = factor[0:4]
    if _short_matches.search(user_agent) != None:
        is_mobile = True
    return is_mobile

#注册登录模块
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

#点赞
def support(request):
    cloum_num = request.get_full_path().split('/')[2]
    cloum_num=cloum_num[7:]
    blog = MyBlog.objects.get(id=cloum_num)
    blog.likes+=1
    blog.save(update_fields=['likes'])
    return HttpResponse(blog.likes)

#文章详细页面
def article(request):
    article_num=request.get_full_path().split('/')[2]
    blog_all=MyBlog.objects.all().filter(id=article_num)
    for i in blog_all:
        article_detiles = i.content
        article_title=i.title
        try:
         likes=i.likes
        except:
            likes=0
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
    total = request.headers
    #ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    #调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    #将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    if mobile:
         return render(request, 'pubu/mobledetail.html',{'article':article_markdown,'article_fontnums':article_fontnums,'toc':md.toc,'blog_all':blog_all,'title':article_title,'likes':likes})
    else:
         return render(request,'pubu/articles.html',{'article':article_markdown,'article_fontnums':article_fontnums,'toc':md.toc,'blog_all':blog_all,'title':article_title,'likes':likes})

#舍弃的jquery页面
def time(request):
    blog_all = MyBlog.objects.all()
    blog_num = len(blog_all)
    for i in blog_all:
        blog = i.content
        title = i.title
    return render(request,'time/index.html',{'blog_all':blog_all})
#分类查找文章
def main(request):
    cloum_num=request.get_full_path().split('/')[2]
    blog_all = MyBlog.objects.all().filter(column_id=cloum_num)
    for i in range(len(blog_all)):
        blog_all[i].content=markdown.markdown(blog_all[i].content[0:260], extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc'  # 自动生成目录
    ]) # 修改blog.content内容为html
    blog_all = blog_all[::-1]
    total = request.headers
    # ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    # 调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    # 将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    if not mobile:
     return render(request,'pubu/main.html',{'blog_list':blog_all})
    else:
        return render(request, 'pubu/moblemain.html', {'blog_list': blog_all})
#所有页面
from django.core.paginator import Paginator
def main_all(request):
    blog_all = MyBlog.objects.exclude(column_id=4)
    for i in range(len(blog_all)):
            blog_all[i].content=markdown.markdown( blog_all[i].content[0:260], extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
             ])
    blog_all=blog_all[::-1]
    total = request.headers
    #ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    #调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    #将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    if mobile:
         return render(request, 'pubu/moblemain.html', {'blog_list': blog_all})
    else:
        return render(request, 'pubu/main.html', {'blog_list': blog_all})
#404页面
def page_not_found(request,exception):
    return render(request, 'pubu/../templates/404.html')
def rjkf(request):
    blog_all = MyBlog.objects.exclude(column_id=4)
    for i in range(len(blog_all)):
            blog_all[i].content=markdown.markdown( blog_all[i].content[0:260], extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
             ])
    blog_all=blog_all[::-1]
    total = request.headers
    # ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    # 调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    # 将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    if not mobile:
     return render(request, 'time/index2.html')
    else:
     return render(request, 'time/mobile.html')
def joinus(request):
    name= request.GET.get('name')
    Class=request.GET.get('Class')
    institute=request.GET.get('institute')
    number=request.GET.get('number')
    direction=request.GET.get('direction')
    student =Joinus()
    student.name=name
    student.Class=Class
    student.institute=institute
    student.number=number
    student.direction=direction
    student.save()
    return HttpResponse(json.dumps({
        "status":'success'
    }))
