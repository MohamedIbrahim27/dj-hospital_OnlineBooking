from django.contrib import admin
from.models import *
# Register your models here.


class OutpatientScheduleAdmin(admin.ModelAdmin):
    list_display = ('clinics', 'floor', 'display_workdays')

    def display_workdays(self, obj):
        return ", ".join(str(workday) for workday in obj.workdays.all())

    display_workdays.short_description = 'Workdays'

admin.site.register(Clinics)
admin.site.register(Booking)
admin.site.register(Outpatient_schedule,OutpatientScheduleAdmin)
admin.site.register(WorkDay)
