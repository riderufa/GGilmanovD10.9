from django.db import models
from PIL import Image

# Create your models here.
class Producer(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CarModel(models.Model):
    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer, blank=True, null=True, on_delete=models.SET_NULL, related_name="carmodels")

    def __str__(self):
        return self.title

class Color(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="cars")
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cars")
    year = models.IntegerField()
    description = models.TextField()
    transmission = models.CharField(max_length=50, choices=[('A', 'automatic'), ('M', 'manual'), (None, '')], blank=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, related_name="cars")
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)

    def __str__(self):
        return "{} {} {}".format(self.producer, self.car_model, self.year)

    def save(self):
        super().save()
        
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 100 or img.width > 100:
                output_size = (100, 100)
                img.thumbnail(output_size)
                img.save(self.image.path)

