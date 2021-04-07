from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import requests


@module.commands("dad", "dadjoke", "dj")
def dadjoke(bot, trigger):
    """Posts a dad joke."""
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    try:
        dad_joke = requests.get(url, headers=headers).json()['joke']
        bot.say(dad_joke)
    except BaseException:
        bot.reply("Error reaching API, probably.")
