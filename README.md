# MovieBookingSystem
🎬 Movie Booking System

A full-stack web application built using Django that allows users to browse movies, select show timings, choose seats, and book tickets seamlessly.

🚀 Features
🎥 View available movies
🕒 Check show timings
🎟️ Select seats dynamically
💰 Real-time price calculation
✅ Booking confirmation system
⚠️ Prevents double seat booking
🧑‍💻 Admin panel for managing movies, shows, and bookings
🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite
Other: Django ORM, Admin Panel
⚙️ Project Workflow
User views movies on the homepage
Selects a movie
Chooses available show timings
Selects seats
Confirms booking
Gets booking confirmation
🧠 Concepts Used
Software Development Life Cycle (SDLC)
ER Diagram & Class Diagram
High Cohesion & Low Coupling
Database Relationships (Foreign Keys)
MVC Architecture (Django MVT pattern)
📂 Database Models
Movie → Stores movie details
Show → Stores show timings
Seat → Manages seat availability
Booking → Stores booking information
Ticket → Links seats with booking
🔒 Key Functionalities
Seat availability tracking
Prevention of duplicate bookings
Dynamic seat selection
Real-time price update
▶️ How to Run
git clone <your-repo-link>
cd movie_booking
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
🔐 Admin Panel
http://127.0.0.1:8000/admin/

Use admin to:

Add Movies
Add Shows
Manage Seats

🚀 Future Improvements
User authentication (login/signup)
Online payment integration
Seat locking system
Multi-theatre support
Responsive UI improvements
👨‍💻 Author

Priyanshu Gangwar
B.Tech CSE Student
