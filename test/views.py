from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    template_name = 'test/Introduction.html'
    form_model = models.Player
    # we are passing the fields with questions to the template
    form_fields = ['q_{}'.format(i) for i in range(1, Constants.num_qs+1)]


page_sequence = [
    Introduction,
]
