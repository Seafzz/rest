from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reservation_time = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.name

