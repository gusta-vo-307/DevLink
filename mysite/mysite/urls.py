# mysite/urls.py
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('sobre/', views.sobre_site, name='sobre_site'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    path('contato/', views.contato, name='contato'),
]
