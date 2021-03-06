from django.db import models

# Create your models here.
class Movement(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    remark = models.TextField(
        null=True,
        blank=True,
    )    