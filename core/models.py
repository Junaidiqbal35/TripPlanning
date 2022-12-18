from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class TripPlace(models.Model):
    trip_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=255)
    number_of_days_trip = models.SmallIntegerField()
    place_image = models.ImageField(upload_to='tripPlace')
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse('trip_detail_view', kwargs={'pk': self.pk})


class Activity(models.Model):
    place = models.ForeignKey(TripPlace, on_delete=models.CASCADE, related_name='place_activity')
    activity_place_name = models.CharField(max_length=255)
    activity_place_description = models.TextField()
    activity_place_image = models.ImageField(upload_to='activityPlaces')

    def __str__(self):
        return self.activity_place_name

# class TripFlight(models.Model):
#     departure_time = models.TimeField()
#     arrival_time = models.TimeField()
#     departure_time = models.TimeField()
