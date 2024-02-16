from datetime import datetime, timedelta

from core.exceptions import InvalidConfirmationCodeException, IsBlockException, \
    IsExpiredException, SmsNotFoundException
from core.http.models import SmsConfirm
from core.http.tasks import SendConfirm


class SmsService:
    @staticmethod
    def send_confirm(phone):
        # TODO: Deploy this change when deploying -> code = random.randint(1000, 9999)
        code = 1111
        sms_confirm, status = SmsConfirm.objects.get_or_create(phone=phone,
                                                               defaults={
                                                                   "code": code
                                                               })

        sms_confirm.sync_limits()

        if sms_confirm.resend_unlock_time is not None:
            expired = sms_confirm.interval(sms_confirm.resend_unlock_time)
            exception = IsBlockException(
                f"Resend blocked, try again in {expired}", expired)
            raise exception

        sms_confirm.code = code
        sms_confirm.try_count = 0
        sms_confirm.resend_count += 1
        sms_confirm.phone = phone
        sms_confirm.expired_time = datetime.now() + timedelta(
            seconds=SmsConfirm.SMS_EXPIRY_SECONDS)
        sms_confirm.resend_unlock_time = datetime.now() + timedelta(
            seconds=SmsConfirm.SMS_EXPIRY_SECONDS)
        sms_confirm.save()

        SendConfirm.delay(phone, code)
        return True

    @staticmethod
    def check_confirm(phone, code):
        sms_confirm = SmsConfirm.objects.filter(phone=phone).first()

        if sms_confirm is None:
            raise SmsNotFoundException("Invalid confirmation code")

        sms_confirm.sync_limits()

        if sms_confirm.is_expired():
            raise IsExpiredException("Time for confirmation has expired")

        if sms_confirm.is_block():
            expired = sms_confirm.interval(sms_confirm.unlock_time)
            raise IsBlockException(f"Try again in {expired}")

        if sms_confirm.code == code:
            sms_confirm.delete()
            return True

        sms_confirm.try_count += 1
        sms_confirm.save()

        raise InvalidConfirmationCodeException("Invalid confirmation code")
