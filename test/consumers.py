# from channels import Group
import json
from channels.sessions import channel_session
from .models import Player
import random
from random import choice
from string import ascii_uppercase


def ws_message(message):
    print("REPLY:::", message.reply_channel)
    message.reply_channel.send({
        "text": json.dumps({
            "join": 'str(room.id)',
            "title": 'room.title',
        }),
    })
    # obtaining the message content
    jsonmessage = json.loads(message.content['text'])
    # taking some fields from it like player's id
    playerpk = str(jsonmessage['playerpk'])
    subsessionpk = str(jsonmessage['subsession'])
    # the question id is here:
    what = str(jsonmessage['q'])
    # we find the player with this pk and (just in case) the subsession number
    myplayer = Player.objects.get(pk=playerpk,subsession=subsessionpk)
    # we set the field (from what) to the value of input (stored in whathappens)
    setattr(myplayer, what,str(jsonmessage['whathappens']))
    # and save the instance
    myplayer.save()


def ws_connect(message):
    pass


def ws_disconnect(message):
    pass
