from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import random
import requests

@module.commands("ass")
def ass_api(bot, trigger):
  """Posts a random ass pic. NSFW, obviously."""
  url = "http://api.obutts.ru/butts/%s" %random.randint(0, 8286)
  ass_preview = requests.get(url).json()[0]['preview']
  bot.say("http://media.obutts.ru/%s" %ass_preview)

@module.commands("boobs")
def boobs_api(bot, trigger):
  """Posts a random boob pic. NSFW, obviously."""
  url = "http://api.oboobs.ru/boobs/%s" %random.randint(0, 14620)
  boobs_preview = requests.get(url).json()[0]['preview']
  bot.say("http://media.oboobs.ru/%s" %boobs_preview)
