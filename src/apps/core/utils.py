from django.utils import timezone


def get_now_datetime():
    return timezone.localtime(timezone.now())

