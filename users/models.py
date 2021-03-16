from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.DO_NOTHING)
    role = models.CharField(
        max_length=150,
        verbose_name=_(u'role person'))

    def __str__(self):
        return u'{0} '.format(
            self.id
        )
