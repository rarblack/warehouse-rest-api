from django.http import HttpResponse
from pyfcm import FCMNotification

from . import models


def fcm_insert(request):
    token = request.GET.get("fcm_token", '')
    a = models.FCMModel(fcm_token=token)
    a.save()
    return HttpResponse(token)


def send_notifications(request):
    path_to_fcm = "https://fcm.googleapis.com"
    server_key = 'insert your server keys here'
    reg_id = models.FCMModel.objects.all()[0].fcm_token #quick and dirty way to get that ONE fcmId from table
    message_title = "Zeo Learn"
    message_body = "Hi john, Zeo learn Rocks!"
    result = FCMNotification(api_key=server_key).notify_single_device(registration_id=reg_id, message_title=message_title, message_body=message_body)
    return HttpResponse(result)
