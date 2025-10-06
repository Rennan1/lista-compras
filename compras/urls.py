"""
URL configuration for lista_compras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_item/', views.adicionar_item, name='adicionar_item'),
    path('editar_item/<int:item_id>/', views.editar_item, name='editar_item'),
    path('excluir_item/<int:item_id>/', views.excluir_item, name='excluir_item'),
    path('adicionar_carrinho/<int:item_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover_carrinho/<int:item_id>/', views.remover_carrinho, name='remover_carrinho'),
]
