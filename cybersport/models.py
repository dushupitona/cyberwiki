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
    player_current_role = models.CharField(max_length=64)
    player_total_winnings = models.IntegerField()
    player_discipline_id =models.ForeignKey(to=DisciplineModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_nickname


class TournamentModel(models.Model):
    tournament_image = models.ImageField(upload_to='media')
    tournament_name = models.CharField(max_length=64)
    tournament_type = models.CharField(max_length=64)
    tournament_location = models.CharField(max_length=64)
    tournament_prize_pool = models.IntegerField()
    tournament_start_date = models.DateField()
    tournament_end_date = models.DateField()
    tournament_discipline_id =models.ForeignKey(to=DisciplineModel, on_delete=models.CASCADE)
    tournament_tier = models.IntegerField()

    def __str__(self):
        return self.tournament_name


class PlayerCommandModel(models.Model):
    pc_player_id = models.ForeignKey(to=PlayerModel, on_delete=models.CASCADE)
    pc_command_id = models.ForeignKey(to=CommandModel, on_delete=models.CASCADE)


class TournamentCommandModel(models.Model):
    tc_tournament_id = models.ForeignKey(to=TournamentModel, on_delete=models.CASCADE)
    tc_command_id = models.ForeignKey(to=CommandModel, on_delete=models.CASCADE)