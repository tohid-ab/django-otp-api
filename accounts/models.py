import random, string, uuid
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from api.sms_sender import kavenegar_token_send
from django.utils import timezone
# Create your models here.


class PhoneNumberUser(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    pass


class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        time_c = timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,
            created__lte=time_c,
            created__gte=time_c-timedelta(seconds=120),
        ).exists()


def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return ''.join(digits)


class OTPManager(models.Manager):

    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)

    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)

    def generate(self, data):
        otp = self.model(receiver=data['receiver'])
        otp.save(using=self._db)
        kavenegar_token_send(otp)
        return otp


class OTPRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    receiver = models.CharField(max_length=50, verbose_name='شماره تلفن همراه',)
    password = models.CharField(max_length=4, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = OTPManager()

    class Meta:
        ordering = ['-created']
