from sopel import plugin, config
from sopel.config.types import StaticSection, ValidatedAttribute
import json
import random
import requests


class GooglecseSection(StaticSection):
    api_key = ValidatedAttribute("api_key", str)
    engine_id = ValidatedAttribute("engine_id", str)


def setup(bot):
    bot.config.define_section("googlecse", GooglecseSection)


def configure(config):
    config.define_section("googlecse", GooglecseSection)
    config.googlecse.configure_setting("api_key", "google cse api key")
    config.googlecse.configure_setting("engine_id", "search engine id")


@plugin.command("img")
@plugin.example(".img catgirl")
def img_search(bot, trigger):
    """Uses DuckDuckGo Instant Answers API to query for an image.
    If that fails, fallsback to Google CSE."""
    search_term = trigger.group(2)

    if not search_term:
        bot.reply("I need something to search.")
        return

    ddg_params = {
        "q": search_term,
        "format": "json",
        "pretty": "1"
    }
    ddg_url = "https://api.duckduckgo.com/"

    try:
        ddg_result = requests.get(
            ddg_url, params=ddg_params).json()["Image"]
        if not ddg_result:
            google_headers = {"Accept": "application/json"}
            google_params = {
                "cx": bot.config.googlecse.engine_id,
                "c2coff": "1",
                "cr": "countryUS",
                "num": "1",
                "safe": "active",
                "searchType": "image",
                "siteSearch": "www.pinterest.com,lookaside.fbsbx.com,memegenerator.net",
                "siteSearchFilter": "e",
                "prettyPrint": "true",
                "alt": "json",
                "q": search_term,
                "key": bot.config.googlecse.api_key}
            google_url = "https://customsearch.googleapis.com/customsearch/v1"
            google_result = requests.get(
                google_url,
                params=google_params,
                headers=google_headers).json()["items"][0]["link"]
            bot.say(google_result)
        else:
            bot.say("https://duckduckgo.com{}".format(ddg_result))
    except json.decoder.JSONDecodeError:
        bot.reply("Bad image search.")
    except KeyError:
        bot.reply("No results.")


@plugin.command("rimg")
@plugin.example(".rimg catgirl")
def rimg_search(bot, trigger):
    """Does a random image search using a Google CSE."""
    search_term = trigger.group(2)

    if not search_term:
        bot.reply("I need something to search.")
        return

    google_headers = {"Accept": "application/json"}
    google_params = {
        "cx": bot.config.googlecse.engine_id,
        "c2coff": "1",
        "cr": "countryUS",
        "num": "10",
        "safe": "active",
        "searchType": "image",
        "siteSearch": "www.pinterest.com,lookaside.fbsbx.com,memegenerator.net",
        "siteSearchFilter": "e",
        "prettyPrint": "true",
        "alt": "json",
        "q": search_term,
        "key": bot.config.googlecse.api_key}
    google_url = "https://customsearch.googleapis.com/customsearch/v1"

    try:
        google_results = requests.get(
            google_url,
            params=google_params,
            headers=google_headers).json()["items"]
        image_link = random.choice(google_results)["link"]
        bot.say(image_link)
    except KeyError:
        bot.reply("No results.")
