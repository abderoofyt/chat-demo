# Generated by Django 4.1.7 on 2023-03-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_one', models.CharField(max_length=255)),
                ('player_two', models.CharField(max_length=255)),
                ('current_player', models.CharField(max_length=255)),
                ('board', models.CharField(default='         ', max_length=9)),
            ],
        ),
    ]
