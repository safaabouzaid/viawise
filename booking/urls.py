from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserBookingsAPIView
from . import views

urlpatterns = [
path('make_booking/', views.make_booking, name='create_booking'),
path('modify_booking/', views.modify_booking, name='modify_booking'),
path('cancel_booking/', views.cancel_booking, name='cancel_booking'),
path('user-bookings/', UserBookingsAPIView.as_view(), name='user-bookings'),
path('make_payment/', views.make_payment, name='make_payment'),
path('user-booking/', UserBookingsAPIView.as_view(), name='user-bookings'),
#path('send_notification/', views.send_notification, name='send_notification'),
path('load_seed_data/', views.load_seed_data, name='load_seed_data'),

]
