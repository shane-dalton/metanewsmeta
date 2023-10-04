from django.db import models

# Create your models here.
from django.utils import timezone


class BaseModel(models.Model):
    pass


class TimeStampable(BaseModel):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TimeStampable, self).save(*args, **kwargs)