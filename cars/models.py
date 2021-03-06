from django.db import models
from django.contrib.auth import get_user_model

from category_cars.models import Category


User = get_user_model()


class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    year = models.DateField()
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='cars', default='no_photo.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
