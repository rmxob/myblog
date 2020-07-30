from django.contrib import admin
from django.urls import path,include
import myapp1
from myapp1 import views,urls
from django.conf.urls.static import static
from django.conf import settings
# urlpatterns = [path('admin/', admin.site.urls), path('index/', views.index), ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(myapp1.urls)),
    path(r'mdeditor/', include('mdeditor.urls')),
]
