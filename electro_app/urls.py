from django.urls import path
from electro_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('bookings', views.bookings, name="bookings"),
    path('appointment', views.appointment, name="appointment"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
    path('logins', views.logins, name="logins"),
    path('regs', views.regs, name="regs"),
    path('show/<ID>', views.show, name="show"),
    path('delete_items/<ID>', views.delete_items, name="delete_items"),
    path('reviews', views.reviews, name="reviews"),
    path('delete_reviews/<ID>', views.delete_reviews, name="delete_reviews"),
    path('subscrib', views.subscrib, name="subscrib"),
]