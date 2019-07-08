from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^api-token-auth/', obtain_auth_token),
    path('hello/', views.HelloView.as_view(), name='hello'),
]