from rest_framework.authtoken import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]