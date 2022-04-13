from django.db import models

# Create your models here.
class Measurement(models.Model):
    """Model definition for Measurement."""

    # TODO: Define fields here
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Measurement."""

        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'

    def __str__(self):
        """Unicode representation of Measurement."""
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"

    
