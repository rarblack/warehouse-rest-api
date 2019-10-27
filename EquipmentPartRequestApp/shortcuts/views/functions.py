from django.shortcuts import get_object_or_404


def send_notification(title, message, device_id=None, **kwargs):
    from fcm_django.models import FCMDevice

    def to_single_device(device_id):
        device = get_object_or_404(
            FCMDevice,
            device_id=device_id
        )
        if device:
            try:
                device.send_message(
                    title=title,
                    body=message,
                    data={"KEY": message}
                )
            except ValueError:
                raise ValueError("Notification couldn't be sent to the device")

    def to_all_devices():
        devices = FCMDevice.objects.all()
        if devices:
            for device in devices:
                device.send_message(
                    title=title,
                    body=message,
                    data={"KEY": message}
                )

    if device_id:
        to_single_device(device_id)

    else:
        to_all_devices()


def record_notification(request_obj, title, message, creator, **kwargs):
    from ...models.notification.models import NotificationModel
    NotificationModel.objects.create(
        request=request_obj,
        title=title,
        message=message,
        created_by=creator
    )

