from django.contrib.auth.models import User
from django.db import models

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reservation_time = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.name




class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=15, blank=True, null=True) 
    address = models.TextField(blank=True, null=True) 
    
    def __str__(self): 
        return self.user.username
