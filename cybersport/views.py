from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView

from cybersport.models import TournamentModel

# Create your views here.


class IndexView(ListView):
    template_name = 'cybersport/index.html'
    model = TournamentModel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournament_list'] = TournamentModel.objects.all()
        return context