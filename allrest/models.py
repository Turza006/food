from django.db import models

# Create your models here.
class Allrest(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
