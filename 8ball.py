from __future__ import absolute_import, division, print_function, unicode_literals
from sopel.module import commands, example, rule
import random

@commands('8', '8ball')
@example('.8 am I gay?')
def eightball(bot, trigger):
  """The magic 8ball knows all."""
  messages = [
    #Positive Replies (10)
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes — definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    # Ambiguous Bullshit Replies (5)
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    # Negative Replies (5)
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
  bot.say(random.choice(messages));
