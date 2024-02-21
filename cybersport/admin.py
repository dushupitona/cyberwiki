from django.contrib import admin

from cybersport.models import *

# Register your models here.

@admin.register(PlayerModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_nickname', 'player_name']


@admin.register(DisciplineModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['discipline_name']


@admin.register(CommandModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['command_name', 'command_discipline_id']


@admin.register(TournamentModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['tourn_name', 'tourn_type', 'tourn_tier', 'tourn_start_date']
