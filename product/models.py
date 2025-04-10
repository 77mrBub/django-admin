from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# Create your models here.
