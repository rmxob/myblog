from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path,include
import myapp1
from myapp1 import views,urls
from django.conf.urls.static import static
from django.conf import settings
# urlpatterns = [path('admin/', admin.site.urls), path('index/', views.index), ]
import xadmin
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(myapp1.urls)),
    path(r'mdeditor/', include('mdeditor.urls')),
    path(r'xadmin/', xadmin.site.urls),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

