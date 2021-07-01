from sopel import plugin, formatting
import requests


@plugin.commands("nextmcu", "mcunext")
def next_mcu(bot, trigger):
    """Info on the next MCU release."""
    url = "https://whenisthenextmcufilm.com/api"
    try:
        r = requests.get(url)
        days_until = str(r.json()["days_until"])
        media_title = r.json()["title"]
        media_type = r.json()["type"]
        bot.say(
            "Up next in the MCU is the {} '{}'. It will be out in {} days.".format(
                media_type,
                formatting.italic(media_title),
                formatting.bold(days_until)))
    except:
        bot.reply("Error reaching API, probably.")
