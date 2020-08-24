from django.contrib import admin

# Register your models here.
from . import models

from .models import MyBlog,ArticleColumn
admin.site.register(MyBlog)