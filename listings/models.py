from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    listing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/%Y/%m/&d')

    def __str__(self):
        return self.name
