from django.urls import path
from .views import trash_booking_list, messy_trash_list

urlpatterns = [
    path('api/trash_booking/', trash_booking_list, name='trash_booking'),
    path('api/messy_trash_booking/', messy_trash_list, name='messy_trash_booking'),
]
