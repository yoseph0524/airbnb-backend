# Generated by Django 4.2.5 on 2023-09-26 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_about_alter_user_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True),
        ),
    ]
