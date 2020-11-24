from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import requests

@module.commands("dad", "dadjoke", "dj")
def dadjoke(bot, trigger):
  """Posts a dad joke."""
  url = "https://icanhazdadjoke.com/"
  dad_joke = requests.get(url, headers={"Accept": "application/json"}).json()['joke']
  bot.say(dad_joke)
