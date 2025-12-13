# book/urls.py (ваш главный и единственный файл маршрутов)
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from textbook import views

urlpatterns = [
    # Админка (если нужна)
    path('admin/', admin.site.urls),
    
    # Главная страница
    path('',views.index, name='index'),
    
    # Страница лекций 
    path('lectures/', views.lectures, name='lectures'),

    path('tests/',views.tests, name='tests'),

    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    
    path('lab/', views.lab, name='lab'),
]

# Обслуживание медиафайлов в режиме разработки (для PDF)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)