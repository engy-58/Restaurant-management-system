# Generated by Django 5.0.6 on 2024-05-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporting',
            name='table_id',
            field=models.IntegerField(default=-1),
        ),
    ]
