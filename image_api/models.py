from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="media")


