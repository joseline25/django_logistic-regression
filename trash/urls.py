from django.urls import path
from .views import trash_booking_list

urlpatterns = [
    path('api/trash_booking/', trash_booking_list, name='trash_booking'),
]
