from sopel import plugin, formatting
import requests


@plugin.command("nextmcu")
@plugin.output_prefix("[MCU] ")
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
    except BaseException:
        bot.reply("Error reaching API, probably.")


@plugin.command("next4mcu")
@plugin.output_prefix("[MCU] ")
def next4_mcu(bot, trigger):
    """Info on the next MCU release."""
    url = "https://whenisthenextmcufilm.com/api"
    try:
        # 1st Request
        r1 = requests.get(url)

        # 1st Next Item
        days_until_1 = str(r1.json()["days_until"])
        media_title_1 = r1.json()["title"]
        media_type_1 = r1.json()["type"]
        # 2nd Next Item
        days_until_2 = str(r1.json()["following_production"]["days_until"])
        media_title_2 = r1.json()["following_production"]["title"]
        media_type_2 = r1.json()["following_production"]["type"]
        release_date_2 = r1.json()["following_production"]["release_date"]

        # 2nd Request
        date_for_r2 = {"date": release_date_2}
        r2 = requests.get(url, params=date_for_r2)

        # 3rd Next Item
        days_until_3 = str(r2.json()["days_until"])
        media_title_3 = r2.json()["title"]
        media_type_3 = r2.json()["type"]
        # 4th Next Item
        days_until_4 = str(r2.json()["following_production"]["days_until"])
        media_title_4 = r2.json()["following_production"]["title"]
        media_type_4 = r2.json()["following_production"]["type"]

        bot.say("Here are the next 4 upcoming MCU items:")
        bot.say("Immediately up next is the {} '{}'. It will be out in {} days.".format(
            media_type_1, formatting.italic(media_title_1), formatting.bold(days_until_1)))
        bot.say("After that will be the {} '{}'. It will be out in {} days.".format(
            media_type_2, formatting.italic(media_title_2), formatting.bold(days_until_2)))
        bot.say("After that will be the {} '{}'. It will be out in {} days.".format(
            media_type_3, formatting.italic(media_title_3), formatting.bold(days_until_3)))
        bot.say("Finally, after that is the {} '{}'. It will be out in {} days.".format(
            media_type_4, formatting.italic(media_title_4), formatting.bold(days_until_4)))
    except BaseException:
        bot.reply("Error reaching API, probably.")
