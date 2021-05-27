from sopel import module
import os
import random


@module.commands("ym")
def yourmom(bot, trigger):
    file = os.path.join(os.path.dirname(__file__), "yourmom.txt")
    joke = random.choice(open(file).readlines())
    bot.say(joke)
