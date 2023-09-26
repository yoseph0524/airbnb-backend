# Generated by Django 4.2.5 on 2023-09-26 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_booking_experience_alter_booking_room_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='host_approval_state',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('denied', 'Denied')], default='pending', max_length=15),
        ),
        migrations.AddField(
            model_name='booking',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]