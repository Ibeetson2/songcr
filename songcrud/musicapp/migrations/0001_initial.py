# Generated by Django 4.1.2 on 2022-10-25 19:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date_released', models.DateField(default=datetime.date.today)),
                ('likes', models.IntegerField()),
                ('artist_id', models.IntegerField()),
                ('Artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.IntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]
