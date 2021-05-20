from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', views.ArticleView.as_view(), name='article_view')
]