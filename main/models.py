from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activate = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_massages = models.BooleanField(default=True, verbose_name='Присылать оповещения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass
