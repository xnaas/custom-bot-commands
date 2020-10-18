from __future__ import absolute_import, division, print_function, unicode_literals
from sopel.module import commands, example, rule
import random

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

@rule('^(Y|y)eah!$')
def yeah(bot, trigger):
  bot.say('https://actionsack.com/img/misc/yeah!.gif')

@rule('^retard.*')
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
  bot.say('https://w2g.tv/rooms/actionsack-csurhbl9dkwvwnk91a')

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

@rule('.*adapters.*')
def adapters(bot, trigger):
  adapters = ['https://actionsack.com/img/misc/adapters01.png', 'https://actionsack.com/img/misc/adapters02.png']
  bot.say(random.choice(adapters))

@rule('.*accident.*')
def accident(bot, trigger):
  bot.say('https://actionsack.com/img/misc/accident.png')

@rule('.*14nm.*')
def fourteennm(bot, trigger):
  bot.say('https://p.xnaas.info/zz-misc/14nm+++++.mp4')

@rule('^bait.*')
def bait(bot, trigger):
  bait = ['https://actionsack.com/img/bait/404bait.png', 'https://actionsack.com/img/bait/all-bait.gif', 'https://actionsack.com/img/bait/b8.png', 'https://actionsack.com/img/bait/bai--what.png', 'https://actionsack.com/img/bait/bait-g.gif', 'https://actionsack.com/img/bait/bait-krunk.jpg', 'https://actionsack.com/img/bait/bait-pole.png', 'https://actionsack.com/img/bait/bait-sim.png', 'https://actionsack.com/img/bait/bait-therapy.png', 'https://actionsack.com/img/bait/bait.gif', 'https://actionsack.com/img/bait/bait.png', 'https://actionsack.com/img/bait/bait001.jpg', 'https://actionsack.com/img/bait/bait002.png', 'https://actionsack.com/img/bait/bait003.jpg', 'https://actionsack.com/img/bait/bait004.jpg', 'https://actionsack.com/img/bait/bait005.jpg', 'https://actionsack.com/img/bait/bait006.png', 'https://actionsack.com/img/bait/bait007.png', 'https://actionsack.com/img/bait/bait008.png', 'https://actionsack.com/img/bait/bait009.jpg', 'https://actionsack.com/img/bait/bait010.jpg', 'https://actionsack.com/img/bait/bait011.jpg', 'https://actionsack.com/img/bait/bait012.jpg', 'https://actionsack.com/img/bait/bait013.jpg', 'https://actionsack.com/img/bait/bait014.jpg', 'https://actionsack.com/img/bait/bait015.jpg', 'https://actionsack.com/img/bait/bait016.jpg', 'https://actionsack.com/img/bait/bait017.png', 'https://actionsack.com/img/bait/bait018.png', 'https://actionsack.com/img/bait/bait019.png', 'https://actionsack.com/img/bait/bait020.jpg', 'https://actionsack.com/img/bait/bait021.jpg', 'https://actionsack.com/img/bait/bait022.png', 'https://actionsack.com/img/bait/bait023.jpg', 'https://actionsack.com/img/bait/bait024.jpg', 'https://actionsack.com/img/bait/bait025.png', 'https://actionsack.com/img/bait/bait026.png', 'https://actionsack.com/img/bait/bait027.png', 'https://actionsack.com/img/bait/baitkakke.jpg', 'https://actionsack.com/img/bait/baitku.png', 'https://actionsack.com/img/bait/baitnado.jpg', 'https://actionsack.com/img/bait/baito.png', 'https://actionsack.com/img/bait/changed-bait.jpg', 'https://actionsack.com/img/bait/chosen-bait.png', 'https://actionsack.com/img/bait/debait.png', 'https://actionsack.com/img/bait/hq-bait.jpg', 'https://actionsack.com/img/bait/MBGA.jpg', 'https://actionsack.com/img/bait/mikes-bait.jpg', 'https://actionsack.com/img/bait/poke-bait.png', 'https://actionsack.com/img/bait/teach-bait.jpg', 'https://actionsack.com/img/bait/whose-bait.jpg', 'https://actionsack.com/img/bait/wtf-bait.jpg', 'https://actionsack.com/img/bait/']
  bot.say(random.choice(bait))

@rule('.*backhand.*')
def backhand(bot, trigger):
  bot.say('https://actionsack.com/img/misc/backhand.mp4')

@rule('^😠$')
def angryeyes(bot, trigger):
  bot.say('https://actionsack.com/img/misc/angryeyes.gif')

@rule('.*alot.*')
def alot(bot, trigger):
  bot.say('https://actionsack.com/img/alot/')

@rule('.*♿.*')
def handicap(bot, trigger):
  bot.say('https://actionsack.com/img/♿/♿.mp4')

@rule('.*⤵️.*')
def down(bot, trigger):
  bot.say('https://actionsack.com/img/mike/down.gif')

@rule('^\.\.\.$')
def dotdotdot(bot, trigger):
  bot.say('...')

@rule('^\.dz$')
def deeznutz(bot, trigger):
  bot.say(sopel.formatting.bold('DEEZ NUTZ!'))

@rule('^\s\/lenny$')
def lenny(bot, trigger):
  lenny = ['https://actionsack.com/img/lenny/lenny-anime.gif', 'https://actionsack.com/img/lenny/lenny-crazy.mp4', 'https://actionsack.com/img/lenny/lenny-spiral.gif']
  bot.say(random.choice(lenny))

@rule('^(P|p)ranked!')
def prank(bot, trigger):
  prank = ['https://actionsack.com/img/prank/prank01.png', 'https://actionsack.com/img/prank/prank02.png']
  bot.say(random.choice(prank))

@rule('^\?\?\?$')
def que(bot, trigger):
  bot.say('https://actionsack.com/img/misc/¿¿¿.png')

@rule('^\\\o/$')
def handsup(bot, trigger):
  bot.say('\\o/')

@rule('^¯\\\_\(ツ\)_\/¯')
def shrug(bot, trigger):
  bot.say('¯\\_(ツ)_/¯')

@rule('^🦏$')
def rhino(bot, trigger):
  bot.say('https://actionsack.com/img/🦏/🦏.gif')

@rule('^🧀$')
def cheese(bot, trigger):
  bot.say('https://actionsack.com/img/🧀/🧀.mp4')

@rule('^🦄$')
def unicorn(bot, trigger):
  bot.say('https://actionsack.com/img/🦄/🦄.jpg')

@rule('^🙃$')
def upsidedown(bot, trigger):
  bot.say('🙃')

@rule('^(🖕|🖕🏻|🖕🏼|🖕🏽|🖕🏾|🖕🏿)$')
def fuckyouback(bot, trigger):
  bot.say('Fuck you, ' + trigger.nick + '!')

@rule('^👏$')
def clap(bot, trigger):
  bot.say('👏🏻👏🏼👏🏽👏🏾👏🏿')

@rule('^👍$')
def thumbsup(bot, trigger):
  bot.say('👍🏻👍🏼👍🏽👍🏾👍🏿')

@rule('^👋$')
def wave(bot, trigger):
  bot.say('👋🏻👋🏼👋🏽👋🏾👋🏿')
