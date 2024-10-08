from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.SmallIntegerField()
    