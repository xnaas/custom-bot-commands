from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, config
from sopel.config.types import StaticSection, ValidatedAttribute
import random
import requests


class GoogleCSESection(StaticSection):
    api_key = ValidatedAttribute("api_key", str)


def setup(bot):
    bot.config.define_section("googlecse", GoogleCSESection)


def configure(config):
    config.define_section("googlecse", GoogleCSESection)
    config.imgur.configure_setting("api_key", "google cse api key")


@module.commands("img")
@module.example(".img catgirl")
def img_search(bot, trigger):
    """Uses DuckDuckGo Instant Answers API to query for an image.
    If that fails, fallsback to Google CSE."""
    search_term = trigger.group(2)

    if not search_term:
        bot.reply("I need something to search.")
        return

    params = {"q": search_term}

    url = "https://api.duckduckgo.com/?format=json&pretty=1"
    result = requests.get(url, params=params).json()["Image"]
    if not result:
        bot.reply("No image result.")
    else:
        bot.say("https://duckduckgo.com{}".format(result))

