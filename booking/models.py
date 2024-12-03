from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reservation_time = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.name


class UserProfile(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.Charfield(max_length15, blank=True, null=True)
    addresss = models.TextField(blank=True, null=True)

    def __str__(self): return self
