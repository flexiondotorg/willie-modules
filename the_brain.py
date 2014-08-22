# coding=utf8
"""
brain.py - The brain for willie
Copyright 2014, Martin Wimpress <code@flexion.org>
Licensed under the Eiffel Forum License 2.
     
http://willie.dfbta.net
"""
     
from __future__ import unicode_literals
from willie.tools import Nick
from willie.module import rule, example
import random
import re
import time
import cleverbot

cb = cleverbot.Cleverbot()

def setup(bot):
    random.seed()

@rule('(.*)')
@example('Willie, you have beautiful eyes.')
def chatter(bot, trigger):
    """ A simple chatter bot """

    msg = trigger.group(1).strip()

    channel = trigger.sender
    pm = False
    addressed = False

    # Is this a PM?
    if channel.startswith("#"):
        pm = False
	time_to_think = 6
    else:
        pm = True
        time_to_think = 3

    # If this is not a PM, is the bot being directly addressed?
    if not pm:
        # Compare without trailing punctuation when being addressed.
        msg_without_punctuation = msg.rstrip('?:!.,;')
        if msg.startswith(bot.nick) or msg_without_punctuation.endswith(bot.nick):
   	    addressed = True

    # Remove the bot nick from the message.
    msg_without_nick = msg.replace(bot.nick, "", 1).lstrip(':,').strip()

    # Ignore commands.
    if msg_without_nick.startswith('.'):
        return

    # Ignore verbs for other interactive modules.
    for ignore in ['reload', 'help', 'tell', 'ask', 'ping']:
        if msg_without_nick.startswith(ignore):
            return

    # Only chat when in PM or being addressed in a channel.
    if pm or addressed:
        human = random.uniform(0, time_to_think)
        time.sleep(human)
        reply = cb.ask(msg_without_nick.encode('UTF-8'))
        response = re.sub('(?i)cleverbot', bot.nick, reply)
        if pm:
            bot.say(response)
        else:
            bot.reply(response)
    elif bot.nick in msg:
        human = random.uniform(0, time_to_think)
        time.sleep(human)
        respond = ['My ears are burning.', 'Don\'t think I can\'t hear you.',
                   'Talk *to* me, not about me.', 'I hear you!',
                   'Talking about me behind my back again?']
        bot.say(random.choice(respond))
    else:
        # If we arrive here, do nothing.
	return
