from django.db import models


class Sample(models.Model):
    """
    Check dev and prod setup
    """

    attachment = models.FileField()
