from django.urls import path
from . import views


urlpatterns = [
    # the address targetted at the MainActivity.java file. It was the destination where Volley has to send data
    path(r'insert/', views.fcm_insert, name='insert'),

    # for sending the notification
    path(r'send/notification/', views.send_notifications, name='send_notification')
]