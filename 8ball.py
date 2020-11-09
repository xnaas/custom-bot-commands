import sopel
from sopel.module import commands, example, rule
import random

@commands('8')
@example('.8 am I gay?')
def eightball(bot, trigger):
  """The magic 8ball knows all."""
  messages = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "God says no", "Very doubtful", "Outlook not so good"]
  bot.say(random.choice(messages));
