from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, config
from sopel.config.types import StaticSection, ValidatedAttribute
import requests


class ImgurSection(StaticSection):
    client_id = ValidatedAttribute("client_id", str)


def setup(bot):
    bot.config.define_section("imgur", ImgurSection)


def configure(config):
    config.define_section("imgur", ImgurSection)
    config.imgur.configure_setting("client_id", "imgur client id")


@module.commands("imgur")
@module.example(".imgur catgirl")
def imgur_search(bot, trigger):
    """Searches Imgur API and returns an image."""
    search_term = trigger.group(2)

    if not search_term:
        bot.reply("I need something to search.")
        return

    client_id = bot.config.imgur.client_id
    headers = {"Authorization": "Client-ID {}".format(client_id)}
    params = {"q": search_term}

    try:
        url = "https://api.imgur.com/3/gallery/search/top/all/1"
        result = requests.get(url, params=params, headers=headers).json()["data"][0]["link"]
        bot.say(result)
    except IndexError:
        bot.reply("No results.")
