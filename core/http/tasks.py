from celery import shared_task
from django.utils.translation import gettext as _

from core.services.sms_service import SendService
from core.utils.console import Console


@shared_task
def SendConfirm(phone, code):
    try:
        service: SendService = SendService()
        service.send_sms(phone, _("Sizning Tasdiqlash ko'dingiz: %(code)s") % {
            'code': code})
        Console.success(
            "Success: {phone}-{code}".format(phone=phone, code=code))
    except Exception as e:
        Console.error("Error: {phone}-{code}\n\n{error}".format(phone=phone, code=code, error=e))
