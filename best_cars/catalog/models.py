from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField(blank=True, null=True)
    body_type = models.CharField(max_length=20)
    power = models.IntegerField(default=100)
    year = models.IntegerField(default=1900)
    is_available = models.BooleanField(default=True)
