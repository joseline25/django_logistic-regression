from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime, date

from .models import TrashBooking

# Create your views here.


# get all the trash booking from the database to build the model

def trash_booking_list(request):
    data = TrashBooking.objects.all().values()
    return JsonResponse(list(data), safe=False)
