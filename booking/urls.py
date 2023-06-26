from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='booking'



urlpatterns = [
    path('BookingOnline' , views.BookingOnline , name='BookingOnline'),
    path('BookingOnline/outpatient_schedule' , views.outpatient_schedule , name='outpatient_schedule'),
]