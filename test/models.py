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


class MyFormField(forms.CharField):
    def __init__(self,rightanswer=None,*args, **kwargs):
        self.rightanswer = rightanswer
        super(MyFormField, self).__init__(*args,  **kwargs)
class MyOwnField(models.CharField):
    rightanswer = None
    def __init__(self,*args, **kwargs):
        self.rightanswer=kwargs.pop('rightanswer', None)
        super(MyOwnField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': MyFormField,
                    'rightanswer': self.rightanswer,
                    }
        defaults.update(kwargs)
        return super().formfield(**defaults)


# we create 10 questions in player model
for i in range(1, Constants.num_qs+1):
    digit1 = random.randint(1,10)
    digit2 = random.randint(1,10)

    Player.add_to_class("q_{}".format(i),MyOwnField(
            rightanswer='hellow',
            verbose_name="Question number {}".format(i),
            widget=forms.TextInput(attrs={'class': 'form-control inputs ',
                                            'required': 'required',
                                            'autofocus': 'autofocus', })
        ))
