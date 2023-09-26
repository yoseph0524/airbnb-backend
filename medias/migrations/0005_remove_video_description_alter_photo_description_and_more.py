# Generated by Django 4.2.5 on 2023-09-26 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_rename_event_end_experience_end_and_more'),
        ('medias', '0004_video_description_alter_photo_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='video',
            name='experience',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='experiences.experience'),
        ),
    ]