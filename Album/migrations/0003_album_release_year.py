# Generated by Django 3.2.6 on 2021-08-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0002_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
