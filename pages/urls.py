from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'template_name': 'pages/index.html'}, name='pages_home'),
    path('categorie/<str:categorie_alias>/', views.show_category, 
         {'template_name': 'pages/categorie.html'}, name='pages_categorie'),
    path('ajouter_categorie/', views.ajouter_categorie, 
         {'template_name': 'pages/categorie_add.html'}, name='pages_categorie_add'),
    path('article/<str:article_alias>/', views.show_article, 
         {'template_name': 'pages/article.html'}, name='pages_article'),
]