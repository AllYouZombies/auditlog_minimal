from auditlog.registry import auditlog
from django.db import models


class ChildSampleModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


auditlog.register(ChildSampleModel)
