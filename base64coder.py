from sopel import module
import base64


@module.commands("b64e")
@module.example(".b64e I love you.")
def base64_encode(bot, trigger):
    """Encodes a message into base64."""
    if not trigger.group(2):
        bot.reply("I need something to encode.")
        return

    encodedBytes = base64.b64encode(trigger.group(2).encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    bot.say(encodedStr)


@module.commands("b64d")
@module.example(".b64d V293ISBNdWNoIHNlY3JldC4=")
def base64_decode(bot, trigger):
    """Decodes a base64 string."""
    if not trigger.group(2):
        bot.reply("I need something to decode.")
        return

    try:
        decodedBytes = base64.b64decode(trigger.group(2).encode("utf-8"))
        decodedStr = str(decodedBytes, "utf-8")
        bot.say(decodedStr)
    except:
        bot.reply("I need real base64, fool.")
