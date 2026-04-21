

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    description = models.TextField()

    poster = models.ImageField(upload_to='posters/', null=True, blank=True)  # ✅ ADD THIS

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    screen_number = models.IntegerField()

class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)