from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import View

from cybersport.models import TournamentModel

from cybersport.models import *

# Create your views here.


class IndexView(ListView):
    template_name = 'cybersport/index.html'
    model = TournamentModel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournament_list'] = TournamentModel.objects.all()
        return context
    

class TournamentDetailView(View):
    def get(self, request, tournament_id=None):
        if tournament_id:
            
            tournament = TournamentModel.objects.get(id=tournament_id)
            command_list = tournament.tourn_command.all()

            context = {
                'name': tournament.tourn_name,
                'command_list': command_list,
            }
        
        return render(request, 'cybersport/tournament.html', context)
    

class CommandDetailView(View):
    def get(self, request, command_id=None):
        if command_id:
            
            command = CommandModel.objects.get(id=command_id)
            player_list = command.players.all()

            context = {
                'name': command.command_name,
                'player_list': player_list,
            }
        
        return render(request, 'cybersport/command.html', context)