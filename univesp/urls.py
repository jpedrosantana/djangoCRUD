from django.urls import path, include
from django.contrib import admin
from . import views

#app_name = 'univesp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cadastrar, name='cadastrar'),
    path('alunos/', views.index, name='index'),
    path('alterar/<int:id>/', views.alterar, name='alterar'),
    path('delete/<int:id>/', views.delete, name='delete'),
]