from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from textbook import views
from accounts.views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Главная страница
    path('', views.index, name='index'),
    
    # Учебные материалы
    path('lectures/', views.lectures, name='lectures'),
    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('tests/', views.tests, name='tests'),
    path('lab/', views.lab, name='lab'),
    
    # Аутентификация
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),  # для регистрации
    path('accounts/', include('django.contrib.auth.urls')),  # остальные маршруты (сброс пароля и т.д.)
]

# Обслуживание медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)