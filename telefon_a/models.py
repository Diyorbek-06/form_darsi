from django.db import models

# Create your models here.

class Phone(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ishlatilingan_vaqt = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Phone'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) "