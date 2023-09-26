# Generated by Django 4.2.5 on 2023-09-26 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_rename_end_experience_event_end_and_more'),
        ('medias', '0003_alter_photo_file_alter_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='video',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='experiences.experience'),
        ),
    ]