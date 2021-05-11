from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import random
import requests

headers = {
    "User-Agent": "python/requests",
    "Content-Type": "application/json"
}


@module.commands("ass", "butt", "booty")
def ass_api(bot, trigger):
    """Posts a random ass pic. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "http://api.obutts.ru/butts/0/1/random"
        try:
            ass_preview = requests.get(url).json()[0]["preview"]
            ass_img = ass_preview.replace("_preview", "")
            bot.say("http://media.obutts.ru/{}".format(ass_img))
        except BaseException:
            bot.reply("Error reaching API, probably.")
    else:
        bot.reply("This command is only usable in the #nsfw channel.")


@module.commands("boobs", "tits")
def boobs_api(bot, trigger):
    """Posts a random boobs pic. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "http://api.oboobs.ru/boobs/0/1/random"
        try:
            boobs_preview = requests.get(url).json()[0]["preview"]
            boobs_img = boobs_preview.replace("_preview", "")
            bot.say("https://media.oboobs.ru/{}".format(boobs_img))
        except BaseException:
            bot.reply("Error reaching API, probably.")
    else:
        bot.reply("This command is only usable in the #nsfw channel.")


@module.commands("rboobs")
def reddit_boobs(bot, trigger):
    """Posts a random boob pic from Reddit. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "https://old.reddit.com/search.json"
        params = {
            "q": "(boobs OR titties) AND nsfw:yes AND (site:reddit.com OR site:redgifs.com OR site:imgur.com)",
            "restrict_sr": "",
            "include_over_18": "on",
            "sort": "top",
            "t": "day",
            "type": "link",
            "limit": "100"}
        rboobs_img = requests.get(url, params=params, headers=headers).json()[
            "data"]["children"][random.randrange(100)]["data"]["url"]
        bot.say(rboobs_img)
    else:
        bot.say("This command is only usable in the #nsfw channel.")


@module.commands("rass")
def reddit_ass(bot, trigger):
    """Posts a random ass pic from Reddit. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "https://old.reddit.com/search.json"
        params = {
            "q": "(ass OR butt) AND nsfw:yes AND (site:reddit.com OR site:redgifs.com OR site:imgur.com)",
            "restrict_sr": "",
            "include_over_18": "on",
            "sort": "top",
            "t": "day",
            "type": "link",
            "limit": "100"}
        rass_img = requests.get(url, params=params, headers=headers).json()[
            "data"]["children"][random.randrange(100)]["data"]["url"]
        bot.say(rass_img)
    else:
        bot.say("This command is only usable in the #nsfw channel.")
