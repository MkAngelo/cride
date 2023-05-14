"""Ride model admin"""

# Django
from django.contrib import admin
from django.http import HttpResponse, response

# Models
from cride.circles.models import Circle
from cride.rides.models import Ride

# Utilities
from django.utils import timezone
from datetime import datetime, timedelta

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = (
        'offered_by',
        'offered_in',
        'available_seats',
        'departure_location',
        'departure_date',
        'arrival_date',
        'arrival_location'
    )
