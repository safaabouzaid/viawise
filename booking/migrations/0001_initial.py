# Generated by Django 5.0.3 on 2024-04-15 08:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flights', '0019_rename_price_flight_price_flight'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=3)),
                ('date_of_birth', models.DateField()),
                ('passport_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('passenger_class', models.CharField(choices=[('Economy', 'Economy'), ('Business', 'Business'), ('First', 'First')], max_length=10, null=True)),
                ('trip_type', models.CharField(choices=[('OW', 'One Way'), ('RT', 'Round Trip')], default='OW', max_length=10)),
                ('status', models.CharField(choices=[('CNL', 'Canceled'), ('PPD', 'Postponed'), ('CMP', 'Completed')], default='PPD', max_length=50)),
                ('total_cost', models.DecimalField(decimal_places=5, max_digits=15, null=True)),
                ('outbound_flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outbound_bookings', to='flights.flight')),
                ('return_flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='return_bookings', to='flights.flight')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('Passenger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=15, null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('booking', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]