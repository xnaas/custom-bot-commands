from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import base64


@module.commands("b64e")
def base64_encode(bot, trigger):
    if not trigger.group(2):
        bot.reply("I need something to encode.")
        return

    encodedBytes = base64.b64encode(trigger.group(2).encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    bot.say(encodedStr)


@module.commands("b64d")
def base64_decode(bot, trigger):
    if not trigger.group(2):
        bot.reply("I need something to decode.")
        return

    try:
        decodedBytes = base64.b64decode(trigger.group(2).encode("utf-8"))
        decodedStr = str(decodedBytes, "utf-8")
        bot.say(decodedStr)
    except BaseException:
        bot.reply("I need real base64, fool.")
