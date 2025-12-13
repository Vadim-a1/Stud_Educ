from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Остальные пути уже в главном urls.py
]