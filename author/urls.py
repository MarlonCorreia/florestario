from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthorList.as_view(), name='author_list'),
    path('<int:pk>', views.AuthorView.as_view(), name='author_view')
]