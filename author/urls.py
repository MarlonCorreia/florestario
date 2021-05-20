from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', views.AuthorView.as_view(), name='author_view')
]