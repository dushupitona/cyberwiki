# Generated by Django 5.0.2 on 2024-02-21 02:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_image', models.ImageField(upload_to='media')),
                ('discipline_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CommandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_image', models.ImageField(upload_to='media')),
                ('command_name', models.CharField(max_length=64)),
                ('command_location', models.CharField(max_length=64)),
                ('command_total_winnings', models.IntegerField()),
                ('command_creation_date', models.DateField()),
                ('command_discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cybersport.disciplinemodel')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_image', models.ImageField(upload_to='media')),
                ('player_name', models.CharField(max_length=64)),
                ('player_nickname', models.CharField(max_length=64)),
                ('player_nationality', models.CharField(max_length=64)),
                ('player_birth_day', models.DateField()),
                ('player_position', models.IntegerField()),
                ('player_total_winnings', models.IntegerField()),
                ('player_command_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cybersport.commandmodel')),
                ('player_discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cybersport.disciplinemodel')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tourn_image', models.ImageField(upload_to='media')),
                ('tourn_name', models.CharField(max_length=64)),
                ('tourn_type', models.CharField(max_length=64)),
                ('tourn_location', models.CharField(max_length=64)),
                ('tourn_prize_pool', models.IntegerField()),
                ('tourn_start_date', models.DateField()),
                ('tourn_end_date', models.DateField()),
                ('tourn_tier', models.IntegerField()),
                ('tourn_command', models.ManyToManyField(to='cybersport.commandmodel')),
                ('tourn_discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cybersport.disciplinemodel')),
            ],
        ),
    ]
