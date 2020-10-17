from __future__ import absolute_import, division, print_function, unicode_literals
from sopel.module import commands, example, rule
import random

@commands('helloworld', 'hw')
@example('.helloworld')
def hw(bot, trigger):
  """Say hello to the world!"""
  bot.say('Hello, world!')

@commands('nod')
@example('.nod')
def nod(bot, trigger):
  """Nod."""
  bot.say('https://actionsack.com/img/trek/nod.gif')

@commands('spok')
@example('.spok')
def spok(bot, trigger):
  """Summon SPOK"""
  bot.say('https://actionsack.com/img/trek/spok.gif')  

@rule('^Hello(\?|!)$')
def hi(bot, trigger):
  bot.say('Hello, ' + trigger.nick + '!')

@rule('^(N|n)ice\.$')
def nice(bot, trigger):
  bot.say('Nice.')

@rule('^yeah!$')
def yeah(bot, trigger):
  bot.say('https://actionsack.com/img/misc/yeah!.gif')

@rule('.*retarded.*')
def retarded(bot, trigger):
  retard = ['https://actionsack.com/img/retard/catarded.png', 'https://actionsack.com/img/retard/retarded.gif', 'https://actionsack.com/img/retard/△.gif']
  bot.say(random.choice(retard))

@rule('rekt', '.*get\srekt.*')
def rekt(bot, trigger):
  rekt = ['https://actionsack.com/img/rekt/baseball.gif', 'https://actionsack.com/img/rekt/beachdive.mp4', 'https://actionsack.com/img/rekt/beachskillz.mp4', 'https://actionsack.com/img/rekt/bf1revenge.mp4', 'https://actionsack.com/img/rekt/bf1sniper.mp4', 'https://actionsack.com/img/rekt/blackman.mp4', 'https://actionsack.com/img/rekt/botw-sled.mp4', 'https://actionsack.com/img/rekt/bridgedive.mp4', 'https://actionsack.com/img/rekt/carcrash.gif', 'https://actionsack.com/img/rekt/gta-bike.mp4', 'https://actionsack.com/img/rekt/gta-flight.mp4', 'https://actionsack.com/img/rekt/gta-phone.mp4', 'https://actionsack.com/img/rekt/gta-post.mp4', 'https://actionsack.com/img/rekt/gta-rekt.mp4', 'https://actionsack.com/img/rekt/gta-stomp.gif', 'https://actionsack.com/img/rekt/jeep.gif', 'https://actionsack.com/img/rekt/leap!.mp4', 'https://actionsack.com/img/rekt/LOLOLOLOL.gif', 'https://actionsack.com/img/rekt/poolgirl.gif', 'https://actionsack.com/img/rekt/rekt.png', 'https://actionsack.com/img/rekt/running.gif', 'https://actionsack.com/img/rekt/skateit.mp4', 'https://actionsack.com/img/rekt/slammin.mp4', 'https://actionsack.com/img/rekt/smash.mp4', 'https://actionsack.com/img/rekt/sniped.mp4', 'https://actionsack.com/img/rekt/walkbot.mp4', 'https://actionsack.com/img/rekt/walkitoff.mp4', 'https://actionsack.com/img/rekt/watergun.mp4']
  bot.say(random.choice(rekt))

@rule('^420.*')
def fourtwenty(bot, trigger):
  fourtwozero = ['https://actionsack.com/img/420/birb.png', 'https://actionsack.com/img/420/champions.png', 'https://actionsack.com/img/420/claim.png', 'https://actionsack.com/img/420/coma.png', 'https://actionsack.com/img/420/comrade.png', 'https://actionsack.com/img/420/dr.png', 'https://actionsack.com/img/420/exp.png', 'https://actionsack.com/img/420/gravityfalls.png', 'https://actionsack.com/img/420/highnoon.gif', 'https://actionsack.com/img/420/highnoon.png', 'https://actionsack.com/img/420/lisa.png', 'https://actionsack.com/img/420/mowing.png', 'https://actionsack.com/img/420/old.png', 'https://actionsack.com/img/420/pikachu.png', 'https://actionsack.com/img/420/🍩.png', 'https://actionsack.com/img/420/pokemon.png', 'https://actionsack.com/img/420/realdanger.png', 'https://actionsack.com/img/420/sealab.png', 'https://actionsack.com/img/420/telluhwat.png', 'https://actionsack.com/img/420/thomas.png', 'https://actionsack.com/img/420/thomasrust.png', 'https://actionsack.com/img/420/timesheet.png', 'https://actionsack.com/img/420/toasted.gif', 'https://actionsack.com/img/420/toystory.png', 'https://actionsack.com/img/420/wednesday.png']
  bot.say(random.choice(fourtwozero))

@rule(':retardeyes:')
def retardeyes(bot, trigger):
  bot.say('https://cdn.discordapp.com/emojis/286222898836799488.png')

@rule('^thx.*')
def thx(bot, trigger):
  bot.say('https://actionsack.com/img/thx/thx.png')

@rule('^(thanks.*|thank\syou.*)')
def thanks(bot, trigger):
  thanks = ['https://actionsack.com/img/thx/h3h3.webm', 'https://actionsack.com/img/thx/t.hanks.mp4', 'https://actionsack.com/img/thx/thankyou.mp4']
  bot.say(random.choice(thanks))

@rule('^😢$')
def crying(bot, trigger):
  crying = ['https://actionsack.com/img/QQ/QQ001.gif', 'https://actionsack.com/img/QQ/QQ002.gif', 'https://actionsack.com/img/QQ/QQ003.gif', 'https://actionsack.com/img/QQ/QQ004.gif', 'https://actionsack.com/img/QQ/QQ005.gif']
  bot.say(random.choice(crying))

@rule('.*!xms.*')
def xms(bot, trigger):
  bot.say('https://app.getmetastream.com/join/0b2d5d7c15f53802b53d04adb28f7cb0be8b729a2b3010768456c60af35e0757')

@rule('.*📖.*')
def book(bot, trigger):
  book = ['https://actionsack.com/img/mike/📖/📖.gif', 'https://actionsack.com/img/mike/📖/📖.jpg', 'https://actionsack.com/img/mike/📖/📖+.jpg', 'https://actionsack.com/img/mike/📖/📖🐇.jpg']
  bot.say(random.choice(book))

@rule('^8D$')
def greg(bot, trigger):
  bot.say('Greg was never in IRC...')

@rule('^FOAD.*')
def foad(bot, trigger):
  bot.say('https://actionsack.com/img/misc/foad.png')
