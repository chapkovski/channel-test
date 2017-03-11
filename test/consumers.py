# from channels import Group
import json
from channels.sessions import channel_session
from .models import Player
import random
from random import choice
from string import ascii_uppercase


def ws_message(message):
    jsonmessage = json.loads(message.content['text'])
    playerpk = str(jsonmessage['playerpk'])
    subsessionpk = str(jsonmessage['subsession'])
    what = str(jsonmessage['q'])
    myplayer = Player.objects.get(pk=playerpk,subsession=subsessionpk)
    setattr(myplayer, what,str(jsonmessage['whathappens']))
    myplayer.save()


def ws_connect(message):
    pass


def ws_disconnect(message):
    pass
