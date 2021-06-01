from sopel import plugin
import random
import requests
import rule34

headers = {
    "User-Agent": "python/requests",
    "Content-Type": "application/json"
}


@plugin.commands("ass", "butt", "booty")
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


@plugin.commands("boobs", "tits", "titties")
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


@plugin.command("rboobs")
def reddit_boobs(bot, trigger):
    """Posts a random boob pic from Reddit. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "https://old.reddit.com/search.json"
        params = {
            "q": "(boobs OR boobies OR titties) AND nsfw:yes AND (site:reddit.com OR site:redgifs.com OR site:imgur.com)",
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
        bot.reply("This command is only usable in the #nsfw channel.")


@plugin.command("rass")
def reddit_ass(bot, trigger):
    """Posts a random ass pic from Reddit. #nsfw only."""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        url = "https://old.reddit.com/search.json"
        params = {
            "q": "(ass OR butt OR booty) AND nsfw:yes AND (site:reddit.com OR site:redgifs.com OR site:imgur.com)",
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
        bot.reply("This command is only usable in the #nsfw channel.")


r34 = rule34.Sync()
@plugin.commands("rule34", "r34")
@plugin.example(".rule34 rimuru_tempest")
def rule34_cmd(bot, trigger):
    """Search rule34.xxx by tags. You can type multiple words to chain together tags.
    Full Tag List: rule34.xxx/index.php?page=tags&s=list"""
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        search_term = trigger.group(2)

        if not search_term:
            bot.reply("I need some tags, bro!")
            return

        try:
            posts = r34.getImages(tags=search_term, randomPID=True)
            images = [(post.file_url) for post in posts]
            bot.say(random.choice(images))
        except TypeError:
            bot.reply("No results. Try refining your tags.")
    else:
        bot.reply("This command is only usable in the #nsfw channel.")
