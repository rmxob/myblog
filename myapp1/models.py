from django.db import models

# Create your models here.
class fs(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    track_id=models.CharField(max_length=20)
    is_Delete=models.BooleanField(default=False,null=True)

class resiger(models.Model):
    uid=models.IntegerField(max_length=20)
    pwd=models.CharField(max_length=20)
class new_resiger(models.Model):
    uid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
from django.db import models
from mdeditor.fields import MDTextField   # 必须导入

class MyBlog(models.Model):
    '''博客管理'''
    title = models.CharField(max_length=30)
    list = models.CharField(max_length=30)
    content = MDTextField()    # 注意为MDTextField()

    def __str__(self):
        return self.__doc__ + "title->" + self.title

    class Meta:
        verbose_name = "博客发布"
        verbose_name_plural = verbose_name

# from tinymce.models import HTMLFiled
# class Text(model.Model):
#
class MyBlog1(models.Model):
    '''博客管理'''
    title = models.CharField(max_length=30)
    list = models.CharField(max_length=30)
    content = MDTextField()    # 注意为MDTextField()
    img=models.CharField(max_length=100)
    def __str__(self):
        return self.__doc__ + "title->" + self.title

    class Meta:
        verbose_name = "博客发布"
        verbose_name_plural = verbose_name