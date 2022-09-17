from django.db import models

# Create your models here.

class CHUBBY(models.Model):
    restaurant = models.CharField(max_length=30, default="Paradise")
    food = models.CharField(max_length=20, default="Biryani")
    place = models.CharField(max_length=20, default="Secunderabad")
    cost = models.IntegerField(default=399)
    rating = models.DecimalField(default=4.5, max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.food + ", " + self.restaurant
