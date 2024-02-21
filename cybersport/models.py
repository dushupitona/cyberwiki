from django.db import models

# Create your models here.
class DisciplineModel(models.Model):
    discipline_image = models.ImageField(upload_to='media')
    discipline_name = models.CharField(max_length=64)

    def __str__(self):
        return self.discipline_name


class CommandModel(models.Model):
    command_image = models.ImageField(upload_to='media')
    command_name = models.CharField(max_length=64)
    command_location = models.CharField(max_length=64)
    command_total_winnings = models.IntegerField()
    command_creation_date = models.DateField()
    command_discipline_id = models.ForeignKey(to=DisciplineModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.command_name


class PlayerModel(models.Model):
    player_image = models.ImageField(upload_to='media')
    player_name = models.CharField(max_length=64)
    player_nickname = models.CharField(max_length=64)
    player_nationality = models.CharField(max_length=64)
    player_birth_day = models.DateField()
    player_position = models.IntegerField()
    player_total_winnings = models.IntegerField()
    player_discipline_id = models.ForeignKey(to=DisciplineModel, on_delete=models.CASCADE)
    player_command_id = models.ForeignKey(to=CommandModel, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.player_nickname


class TournamentModel(models.Model):
    tourn_image = models.ImageField(upload_to='media')
    tourn_name = models.CharField(max_length=64)
    tourn_type = models.CharField(max_length=64)
    tourn_location = models.CharField(max_length=64)
    tourn_prize_pool = models.IntegerField()
    tourn_start_date = models.DateField()
    tourn_end_date = models.DateField()
    tourn_discipline_id = models.ForeignKey(to=DisciplineModel, on_delete=models.CASCADE)
    tourn_tier = models.IntegerField()
    tourn_command = models.ManyToManyField(to=CommandModel) 

    def __str__(self):
        return self.tourn_name
