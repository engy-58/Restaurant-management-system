# Generated by Django 5.0.6 on 2024-05-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bill',
            field=models.IntegerField(default=0),
        ),
    ]