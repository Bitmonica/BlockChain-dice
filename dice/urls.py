"""robot URL Configuration
"""
from django.conf.urls import url

from django.urls import path
from dice.views import home, ajax_bet, ajax_get_tabulky
from dice.views import get_clock, get_game_abi, get_game_contract


urlpatterns = [
    # common views
    url(r'^$', home, name='home'),
    # ajax
    url(r'^ajax/bet/$', ajax_bet, name='ajax_bet'),
    url(r'^ajax/tabulky/$', ajax_get_tabulky, name='ajax_get_tabulky'),
    # bytecode, abi, clock
    url(r'^abi$', get_game_abi, name='get_game_abi'),
    url(r'^contract$', get_game_contract, name='get_game_contract'),
    url(r'^clock$', get_clock, name='get_clock'),
]
