from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.reservation_date}"
