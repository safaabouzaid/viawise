# Generated by Django 5.0.3 on 2024-05-01 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_policyagency_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_type', models.CharField(blank=True, choices=[('modify', 'Modify'), ('cancel', 'Cancel'), ('offers', 'Offers'), ('cancel_without_payment', 'Cancel Without Payment')], max_length=100, null=True)),
                ('percentage', models.DecimalField(decimal_places=5, max_digits=5)),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
            ],
        ),
    ]
