from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import random
import requests

@module.commands("ass")
def ass_api(bot, trigger):
  """Posts a random ass pic. #nsfw only."""
  if trigger.is_privmsg or trigger.sender == "#nsfw":
    url = "http://api.obutts.ru/butts/0/1/random"
    ass_id = str(requests.get(url).json()[0]["id"])
    bot.say("http://media.obutts.ru/butts/%s.jpg" %ass_id.zfill(5))
  else:
    bot.say("This command is only usable in the #nsfw channel.")

@module.commands("boobs")
def boobs_api(bot, trigger):
  """Posts a random boobs pic. #nsfw only."""
  if trigger.is_privmsg or trigger.sender == "#nsfw":
    url = "http://api.oboobs.ru/boobs/0/1/random"
    boobs_id = str(requests.get(url).json()[0]["id"])
    bot.say("https://media.oboobs.ru/boobs/%s.jpg" %boobs_id.zfill(5))
  else:
    bot.say("This command is only usable in the #nsfw channel.")
