# Generated by Django 4.2.2 on 2023-06-26 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='site_name',
        ),
    ]
