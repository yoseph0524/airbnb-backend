# Generated by Django 4.2.5 on 2023-09-26 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0004_rename_end_experience_event_end_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='event_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='event_start',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='perk',
            name='description',
        ),
        migrations.AddField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='city',
            field=models.CharField(default='LA', max_length=80),
        ),
        migrations.AlterField(
            model_name='experience',
            name='country',
            field=models.CharField(default='US', max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='perk',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
