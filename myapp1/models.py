from django.db import models
# Create your models here.

class ArticleColumn(models.Model):
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class fs(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    track_id=models.CharField(max_length=20)
    is_Delete=models.BooleanField(default=False,null=True)
class resiger(models.Model):
    uid=models.IntegerField
    pwd=models.CharField(max_length=20)
class new_resiger(models.Model):
    uid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
from django.db import models
from mdeditor.fields import MDTextField


class MyBlog(models.Model):
    title = models.CharField(u'标题',max_length=30)
    time=models.DateField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    likes=models.IntegerField(default=0)
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    content = MDTextField()
    def __str__(self):
        return  self.title
    class Meta:
        verbose_name = "我的博客"
        verbose_name_plural = verbose_name

class Joinus(models.Model):
    name = models.CharField(u'姓名', max_length=130)
    Class = models.CharField(u'班级', max_length=130)
    institute = models.CharField(u'学院', max_length=130)
    number=models.IntegerField(u'学号')
    direction=models.CharField(u'方向',default='不清楚',max_length=130)