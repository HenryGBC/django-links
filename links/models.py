from django.db import models
from users.models import Profile
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'updated at')
    )

    class Meta:
        abstract = True



class Links(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.CharField(max_length=240)
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.url