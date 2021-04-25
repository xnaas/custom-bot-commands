from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import requests


@module.commands("insult")
def insult(bot, trigger):
    """Insults another user."""
    url = "https://evilinsult.com/generate_insult.php"
    params = {
        "lang": "en",
        "type": "json"
    }
    target = trigger.group(3)

    if target == bot.nick:
        bot.reply("Nice try, retard.")
        return

    if not target:
        bot.reply("I need someone to insult, dipshit.")
        return

    try:
        insult = requests.get(url, params=params).json()['insult']
        bot.say("{}: {}".format(target, insult))
    except BaseException:
        bot.reply("Error reaching API, probably.")
