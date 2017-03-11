from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from django import forms

author = 'Filipp Chapkovskii, UZH'

doc = """
Channels example
"""


class Constants(BaseConstants):
    name_in_url = 'channel_test'
    players_per_group = None
    num_rounds = 1
    num_qs = 10


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



class Player(BasePlayer):
    pass



for i in range(1,Constants.num_qs+1):
    Player.add_to_class("q_{}".format(i),
                        models.CharField(
            verbose_name="Question number {}".format(i),
            widget=forms.TextInput(attrs={'class': 'form-control inputs ',
                                            'required': 'required',
                                            'autofocus': 'autofocus', })
        ))
