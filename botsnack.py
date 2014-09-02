# coding=utf8
"""
botsnack.py - botsnack module for willie
Copyright 2014, infirit <infirit@gmail.com>
Licensed under the Eiffel Forum License 2.
     
http://willie.dfbta.net
"""
     
from __future__ import unicode_literals
from willie import module
from random import choice
     
RESP = ('ta :)', '=D', 'schweet!', 'thanks :)', 'cheers!', 'Yum!')
RESP_NICK = (
    '%(receiver)s, here is a snack from your friendly neighbourhood bot. Enjoy the bits!',
    '%(sender)s, why are you giving away my snacks? %(receiver)s enjoy!',
    '%(sender)s, get your own snacks!',
    '%(receiver)s, %(sender)s is giving you one of my snacks, enjoy. But I\'m not liking it.')

@module.commands('botsnack')
def botsnack(bot, trigger):
    group = trigger.group(2).strip() if trigger.group(2) else ''
    if group and not group.lower() == bot.nick:
        receiver = trigger.group(2).strip()
        sender = trigger.nick
        nicks = {'sender': sender, 'receiver': receiver}
        bot.say(choice(RESP_NICK) % nicks)
    else:
        bot.say(choice(RESP))
