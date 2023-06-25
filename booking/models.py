from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Clinics(models.Model):
    name=models.CharField(max_length=60)
    available=models.BooleanField(default=False,verbose_name='Available For Outpatient')

    class Meta:
        verbose_name = _("clinics")
        verbose_name_plural = _("clinics")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("clinics_detail", kwargs={"pk": self.pk})


class Booking(models.Model):
    clinics=models.ForeignKey(Clinics,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.CharField(max_length=500)
    
    
    
    
    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return self.username + ' ==> ' + str(self.clinics) + ' ==> ' + self.phonenumber

    # def get_absolute_url(self):
    #     return reverse("booking_detail", kwargs={"pk": self.pk})

class WorkDay(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Outpatient_schedule(models.Model):
    clinics=models.ForeignKey(Clinics,on_delete=models.CASCADE)
    floor=models.CharField(max_length=30)
    workdays=models.ManyToManyField(WorkDay, blank=True, related_name='work_days')

    class Meta:
        verbose_name = _("Outpatient_schedule")
        verbose_name_plural = _("Outpatient_schedules")

    def __str__(self):
        return f"{self.clinics} - {self.floor} - {self.workdays}"

    # def get_absolute_url(self):
    #     return reverse("Outpatient_schedule_detail", kwargs={"pk": self.pk})
