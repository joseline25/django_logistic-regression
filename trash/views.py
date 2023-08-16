from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime, date

# to import the table in db and use in pandas

import pandas as pd
import sqlite3


from .models import TrashBooking, MessyTrashBooking

# Create your views here.


# connection to the database : from database to pandas

connexion = sqlite3.connect("db.sqlite3")
cursor = connexion.cursor()

sql = pd.read_sql_query("SELECT * FROM trash_trashbooking", connexion)
messy_sql = pd.read_sql_query(
    "SELECT * FROM trash_messytrashbooking", connexion)

df = pd.DataFrame(sql, columns=["id", "date", "resident_id", "weather",
                  "day_of_week", "previous_requests", "public_holiday", "trash_pickup_request"])

messy_df = pd.DataFrame(sql, columns=["id", "date", "resident_id", "temperature", "weather",
                                      "day_of_week", "previous_requests", "public_holiday", "trash_pickup_request"])


# we need later to do from pandas to database

def trash_booking_list(request):
    data = TrashBooking.objects.all().values()
    return JsonResponse(list(data), safe=False)


# get every entries from messy_trash_dataset

def messy_trash_list(request):
    data = MessyTrashBooking.objects.all().values()
    print(messy_df)
    return JsonResponse(list(data), safe=False)
