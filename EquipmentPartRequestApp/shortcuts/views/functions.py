

def send_notification( title, message, device_id=None, **kwargs):
    from fcm_django.models import FCMDevice
    if device_id:
        device = FCMDevice.objects.get(device_id__exact=device_id)
        if device:
            device.send_message(
                title=title,
                data={"KEY": message}
            )
    else:
        devices = FCMDevice.objects.all()
        if devices:
            for device in devices:
                device.send_message(
                    title=title,
                    data={"KEY": message}
                )


def record_notification(title, message, creator, **kwargs):
    from ...models.notification.models import NotificationModel
    NotificationModel.objects.create(
        title=title,
        message=message,
        created_by=creator
    )

