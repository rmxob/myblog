from django.apps import AppConfig


class Myapp1Config(AppConfig):
    name = 'xob'
# 子应用/apps.py
class HomeConfig(AppConfig):
    name = 'home'
    verbose_name = '我的首页'

# __init__.py
default_app_config = "home.apps.HomeConfig"