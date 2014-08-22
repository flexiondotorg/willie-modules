"""
pinky.py - Simple reflexs and reactions
Copyright 2009-2011, Michael Yanovich, yanovich.net
          2014 Martin Wimpress <code@flexion.org>
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""
from willie.module import rule, priority, rate
import random
import time


def setup(bot):
    random.seed()


def pause_for_thought(delay):
    randtime = random.uniform(0, delay)
    time.sleep(randtime)

        
@rule('(haha|hehe|lol|Lol|LOL|rofl|ROFL)$')
@priority('high')
def f_lol(bot, trigger):
    respond = ['haha', 'lol', 'hehe', 'rofl', 'hoho', 'LOL', 'ROFL', ':-D', ':-)']
    pause_for_thought(1)
    bot.say(random.choice(respond))


@rule('([Dd]amn it|[Hh]eh|[Hh]uh|wtf|WTF|[Hh]mm)*$')
@priority('high')
def f_heh(bot, trigger):
    respond = ['Hmm', 'Tricky', 'Beats me', 'Google it', 'I feel your pain']
    pause_for_thought(1)
    bot.say(random.choice(respond))


@rule('^\s*(([Bb]+([Yy]+[Ee]+(\s*[Bb]+[Yy]+[Ee]+)?)|[Ss]+[Ee]{2,}\s*[Yy]+[Aa]+|[Oo]+[Uu]+)|cya|ttyl|[Gg](2[Gg]|[Tt][Gg]|([Oo]{2,}[Dd]+\s*([Bb]+[Yy]+[Ee]+|[Nn]+[Ii]+[Gg]+[Hh]+[Tt]+)))\s*(!|~|.)*)$')
@priority('high')
def f_bye(bot, trigger):
    word = ['Bye', 'Bye bye', 'See you', 'Until next time', 'Good bye', 'Have a nice day', 'Come back soon', 'See ya', 'Later', 'Missing you already']
    symbol = ['.', '!', ' :-)', ' :-D', ' ;-)']
    respond = random.choice(word) + ' ' + trigger.nick + random.choice(symbol)
    pause_for_thought(2)
    bot.say(respond)


#@rule('^\s*(([Hh]+([AaEe]+[Ll]+[Oo]+|[Ii]+)+\s*(all)?)|[Yy]+[Oo]+|[Aa]+[Ll]+)\s*(!+|\?+|~+|.+|[:;][)DPp]+)*$')
#@priority('high')
#def f_hello(bot, trigger):
#    word = ['Yo', 'Hey', 'Greetings', 'Hi', 'Hello', 'Welcome', 'How do you do', 'Time appropriate greetings']
#    symbol = ['.', '!', ' :-)', ' :-D', ' ;-)']
#    respond = random.choice(word) + ' ' + trigger.nick + random.choice(symbol)
#    pause_for_thought(2)
#    bot.say(respond)

if __name__ == '__main__':
    print __doc__.strip()
