# Generated by Django 4.2.2 on 2023-06-24 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries_complaints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiries',
            name='phonenumber',
            field=models.CharField(max_length=20, verbose_name='phonenumber'),
        ),
    ]