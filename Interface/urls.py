from django.contrib import admin
from django.urls import path
from . import views, settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
