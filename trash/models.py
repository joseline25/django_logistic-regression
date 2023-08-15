from django.db import models

# Create your models here.


class TrashBooking(models.Model):

    weather = (('Sunny', 'Sunny'), ('Rainy', 'Rainy'))
    days = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))

    date = models.DateField(auto_now=True)
    resident_id = models.IntegerField()
    weather = models.CharField(choices=weather, max_length=200)
    day_of_week = models.CharField(choices=days, max_length=200)
    previous_requests = models.IntegerField()
    public_holiday = models.IntegerField()
    trash_pickup_request = models.IntegerField()

# Note : we will load the data from trash_pickup_dataset.csv file

# the date format in the csv file is '%YYYY-%mm-%dd' like '2010-11-12'