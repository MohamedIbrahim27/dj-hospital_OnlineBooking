# Generated by Django 4.2.2 on 2023-06-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_workday_remove_outpatient_schedule_workdays_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinics',
            name='available',
            field=models.BooleanField(default=False, verbose_name='Available For Outpatient'),
        ),
    ]
