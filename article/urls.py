from django.urls import path
from article import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),  # name参数可以反向解析url
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail')
]
