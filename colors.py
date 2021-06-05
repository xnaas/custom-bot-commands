"""
Source: https://github.com/xnaas/sopel-color-text
Forked and heavily modified from: https://github.com/sopel-irc/sopel-rainbow
"""
from sopel import plugin, formatting
from sopel.config import types
import itertools
import random
import unicodedata


COLOR_SCHEMES = {
    'rainbow': [4, 7, 8, 3, 12, 2, 6],
    'usa': [4, 0, 2],
    'commie': [4, 8],
    'spooky': [8, 7, 0],
}
SCHEME_ERRORS = {
    'rainbow': "I can't make a rainbow out of nothing!",
    'usa': "I can't distribute FREEDOM out of nothing!",
    'commie': "I need text to commie-ize!",
    'spooky': "I need text to spookify!",
}


@plugin.commands('rainbow', 'usa', 'commie', 'spooky')
def rainbow_cmd(bot, trigger):
    """Make text colored. Options are "rainbow", "usa", "commie", and "spooky"."""
    text = formatting.plain(trigger.group(2))
    scheme = trigger.group(1).lower()

    if not text:
        try:
            msg = SCHEME_ERRORS[scheme]
        except KeyError:
            msg = "How did you do that?!"
        bot.reply(msg)
        return

    try:
        colors = COLOR_SCHEMES[scheme]
    except KeyError:
        # not possible to reach this at time of writing, but who knows?
        # mistakes happen when updating stuff that needs to be changed in parallel
        bot.reply("I don't know what color sequence to use for '{}'!".format(scheme))
        return

    color_cycle = itertools.cycle(colors)

    bot.say(
        ''.join(
            char if unicodedata.category(char) == 'Zs'
            else formatting.color(char, next(color_cycle))
            for char in text
        )
    )
