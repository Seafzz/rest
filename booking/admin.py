from django.contrib import admin
from .models import Reservation, UserProfile

# Register your models here
admin.site.register(Reservation)
admin.site.register(UserProfile)
