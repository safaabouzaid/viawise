# Generated by Django 5.0.3 on 2024-03-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_flightseatclass_is_reserved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightseatclass',
            name='seat_number',
            field=models.IntegerField(default=10),
        ),
    ]