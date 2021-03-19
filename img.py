from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, config
from sopel.config.types import StaticSection, ValidatedAttribute
import random
import requests


class ImgurSection(StaticSection):
    client_id = ValidatedAttribute("client_id", str)


def setup(bot):
    bot.config.define_section("imgur", ImgurSection)


def configure(config):
    config.define_section("imgur", ImgurSection)
    config.imgur.configure_setting("client_id", "imgur client id")


@module.commands("img")
@module.example(".img catgirl")
def img_search(bot, trigger):
    """Searches Imgur API and returns an image."""
    search_term = trigger.group(2)

    if not search_term:
        bot.say("I need something to search.")
        return

    client_id = bot.config.imgur.client_id
    headers = {
        "User-Agent": "python/requests",
        "Authorization": "Client-ID {}".format(client_id)
    }

    try:
        url = "https://api.imgur.com/3/gallery/search/top/all/1?q={}".format(search_term)
        result = requests.get(url, headers=headers).json()["data"][0]["link"]
        bot.say(result)
    except IndexError:
        bot.say("No results.")
