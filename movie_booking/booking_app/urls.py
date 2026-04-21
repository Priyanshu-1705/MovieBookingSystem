from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/<int:id>/seats/', views.seat_selection, name='seat_selection'),
    path('success/', views.booking_success, name='booking_success'),
]