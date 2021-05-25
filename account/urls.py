from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('sign-up/', views.RegisterAccountView.as_view(), name='register_view'),
    path('login/', obtain_auth_token, name='login_view')
]