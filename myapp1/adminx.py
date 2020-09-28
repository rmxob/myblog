# 在当前子应用中创建adminx.py，添加如下代码
# 轮播图
import xadmin
from xadmin import views
from .models import MyBlog,ArticleColumn
class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "rmxob"  # 设置站点标题
    site_footer = ""  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
xadmin.site.register(views.CommAdminView, GlobalSettings)

class BolgAdminModel(object):
    # 控制列表展示的字段 设置默认展示字段
    # 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
    search_fields = ['id']
    # 可以进行过滤操作的列，对于分类、性别、状态
    list_filter = ['column']
    list_export = ['xls', 'csv', 'json']
    # 控制是否显示书签功能，False表示关闭
    show_bookmarks = True
xadmin.site.register(MyBlog,BolgAdminModel)