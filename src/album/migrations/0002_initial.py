# Generated by Django 5.0.1 on 2024-02-06 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='song.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='featuring',
            field=models.ManyToManyField(blank=True, related_name='featuring', to='song.artist'),
        ),
    ]
