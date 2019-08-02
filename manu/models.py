from django.db import models

# Create your models here.
class Manu(models.Model):
    restname = models.CharField(max_length=200)
    itemname = models.CharField(max_length=200)
    quan = models.CharField(max_length=5)
    price = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images/')
    spec = models.CharField(max_length=500)



    def __str__(self):
        return self.restname
