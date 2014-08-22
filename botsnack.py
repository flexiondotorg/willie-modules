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
     
RESPONSE = ['ta :)', '=D', 'schweet!', 'thanks :)', 'cheers!', 'Yum!']
@module.commands('botsnack')
def botsnack(bot, trigger):
    bot.say(choice(RESPONSE))


