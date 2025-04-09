from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('entrar/', views.entrar, name='entrar'),
    path('hierarquia/', views.hierarquia, name='hierarquia'),
    path('calendario/', views.calendario, name='calendario'),
    path('banhos/', views.banhos, name='banhos'),
    path('ervas/', views.ervas, name='ervas'),
]
