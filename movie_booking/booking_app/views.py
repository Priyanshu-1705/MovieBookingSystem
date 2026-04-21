from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Seat, Show, Booking, Ticket


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    shows = Show.objects.filter(movie=movie)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'shows': shows
    })


def seat_selection(request, id):
    show = get_object_or_404(Show, id=id)
    seats = Seat.objects.filter(show=show).order_by('seat_number')

    if request.method == "POST":
        selected_seats = request.POST.get('seats', '')
        selected_seats = [s for s in selected_seats.split(',') if s.strip()]

        if not selected_seats:
            return render(request, 'seat_selection.html', {
                'seats': seats,
                'show': show,
                'error': "Please select at least one seat"
            })

        booking = Booking.objects.create(
            user_name="Guest",
            show=show,
            total_amount=len(selected_seats) * 200
        )

        for seat_id in selected_seats:
            try:
                seat_id = int(seat_id)
            except:
                continue

            seat = Seat.objects.filter(id=seat_id).first()

            if not seat or seat.is_booked:
                continue

            seat.is_booked = True
            seat.save()

            Ticket.objects.create(
                booking=booking,
                seat=seat
            )

        return redirect('booking_success')

    return render(request, 'seat_selection.html', {
        'seats': seats,
        'show': show
    })


def booking_success(request):
    booking = Booking.objects.last()
    tickets = Ticket.objects.filter(booking=booking)

    return render(request, 'booking_success.html', {
        'booking': booking,
        'tickets': tickets
    })