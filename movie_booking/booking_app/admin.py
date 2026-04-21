

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib import admin

admin.site.site_header = "🎬 MovieHub Admin"
admin.site.site_title = "MovieHub Dashboard"
admin.site.index_title = "Welcome to MovieHub Admin Panel"
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Ticket)