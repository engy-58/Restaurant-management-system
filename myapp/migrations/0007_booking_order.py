# Generated by Django 5.0.6 on 2024-05-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_booking_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order',
            field=models.CharField(default='', max_length=1000),
        ),
    ]