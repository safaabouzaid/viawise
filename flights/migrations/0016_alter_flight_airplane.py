# Generated by Django 5.0.3 on 2024-04-11 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0015_flight_airplane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Airplane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.airplane'),
        ),
    ]