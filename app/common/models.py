from django.db import models


class Base(models.Model):
    is_use = models.BooleanField(default=True)
    is_del = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
