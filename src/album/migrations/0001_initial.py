# Generated by Django 5.0.1 on 2024-02-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fa', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='songs/cover_image/')),
                ('release_date', models.DateField()),
                ('track_items', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
    ]