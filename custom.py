from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, formatting
import random
import unicodedata

### Section Exists for "judge" command only ###
# Remove when dropping support for Sopel < 7.1
if hasattr(formatting, 'plain'):
  clean = formatting.plain
else:
  clean = lambda t: t
### Section Exists for "judge" command only ###

@module.commands("nod")
def nod(bot, trigger):
  """Nod."""
  bot.say("https://actionsack.com/img/trek/nod.webp")

@module.commands("spok")
def spok(bot, trigger):
  """Summon SPOK into chat."""
  bot.say("https://actionsack.com/img/trek/spok.webp")

@module.commands("cube")
def trek_cube(bot, trigger):
  bot.say("https://actionsack.com/img/trek/cube.webp")

@module.rule(r"^Hello(\?|!)$")
def hi(bot, trigger):
  bot.say("Hello, {}!".format(trigger.nick))

@module.rule(r"^(Nice\.)(\s$|$)")
def nice(bot, trigger):
  bot.say(trigger.group(1))

@module.rule(r"^(This\sis\sThe\sWay\.)($|\s$)")
def theway(bot, trigger):
  bot.say(trigger.group(1))

@module.rule(r"^(It\sis\sknown\.)(\s$|$)")
def itisknown(bot, trigger):
  bot.say(trigger.group(1))

@module.rule("^yeah!$")
def yeah(bot, trigger):
  bot.say("https://actionsack.com/img/misc/yeah!.webp")

@module.rule("^retard.*")
def retarded(bot, trigger):
  retard = [
    "https://actionsack.com/img/retard/catarded.webp",
    "https://actionsack.com/img/retard/retarded.webp",
    "https://actionsack.com/img/retard/△.webp"
  ]
  bot.say(random.choice(retard))

@module.rule(".*rekt.*")
def rekt(bot, trigger):
  rekt = [
    "https://actionsack.com/img/rekt/baseball.gif",
    "https://actionsack.com/img/rekt/beachdive.mp4",
    "https://actionsack.com/img/rekt/beachskillz.gif",
    "https://actionsack.com/img/rekt/bf1revenge.mp4",
    "https://actionsack.com/img/rekt/bf1sniper.mp4",
    "https://actionsack.com/img/rekt/blackman.gif",
    "https://actionsack.com/img/rekt/botw-sled.gif",
    "https://actionsack.com/img/rekt/calligraphy.mp4",
    "https://actionsack.com/img/rekt/carcrash.gif",
    "https://actionsack.com/img/rekt/dive.gif",
    "https://actionsack.com/img/rekt/ForHonor.webm",
    "https://actionsack.com/img/rekt/gta-bike.mp4",
    "https://actionsack.com/img/rekt/gta-bounce.mp4",
    "https://actionsack.com/img/rekt/gta-cop.mp4",
    "https://actionsack.com/img/rekt/gta-flight.mp4",
    "https://actionsack.com/img/rekt/gta-gas.mp4",
    "https://actionsack.com/img/rekt/gta-phone.mp4",
    "https://actionsack.com/img/rekt/gta-post.mp4",
    "https://actionsack.com/img/rekt/gta-rekt.mp4",
    "https://actionsack.com/img/rekt/gta-stomp.gif",
    "https://actionsack.com/img/rekt/gta-walkitoff.mp4",
    "https://actionsack.com/img/rekt/jeep.gif",
    "https://actionsack.com/img/rekt/leap.gif",
    "https://actionsack.com/img/rekt/LOLOLOLOL.gif",
    "https://actionsack.com/img/rekt/poolgirl.gif",
    "https://actionsack.com/img/rekt/pubg-redzone.mp4",
    "https://actionsack.com/img/rekt/rekt.png",
    "https://actionsack.com/img/rekt/running.gif",
    "https://actionsack.com/img/rekt/skateit.mp4",
    "https://actionsack.com/img/rekt/slammin.gif",
    "https://actionsack.com/img/rekt/smash.mp4",
    "https://actionsack.com/img/rekt/sniped.mp4",
    "https://actionsack.com/img/rekt/walkbot.gif",
    "https://actionsack.com/img/rekt/watergun.gif",
    "https://w.wiki/n9f"
  ]
  bot.say(random.choice(rekt))

@module.rule("^420.*")
def fourtwenty(bot, trigger):
  fourtwozero = [
    "https://actionsack.com/img/420/attacks.webp",
    "https://actionsack.com/img/420/birb.webp",
    "https://actionsack.com/img/420/champions.webp",
    "https://actionsack.com/img/420/chinarocket.webp",
    "https://actionsack.com/img/420/claim.webp",
    "https://actionsack.com/img/420/coma.webp",
    "https://actionsack.com/img/420/commits.webp",
    "https://actionsack.com/img/420/comrade.webp",
    "https://actionsack.com/img/420/crewdragon.webp",
    "https://actionsack.com/img/420/doc.webp",
    "https://actionsack.com/img/420/dr.webp",
    "https://actionsack.com/img/420/exp.webp",
    "https://actionsack.com/img/420/gravityfalls.webp",
    "https://actionsack.com/img/420/highnoon-a.webp",
    "https://actionsack.com/img/420/highnoon.webp",
    "https://actionsack.com/img/420/lisa.webp",
    "https://actionsack.com/img/420/mowing.webp",
    "https://actionsack.com/img/420/old.webp",
    "https://actionsack.com/img/420/pikachu.webp",
    "https://actionsack.com/img/420/🍩.webp",
    "https://actionsack.com/img/420/pokemon.webp",
    "https://actionsack.com/img/420/realdanger.webp",
    "https://actionsack.com/img/420/replacements.webp",
    "https://actionsack.com/img/420/sealab.webp",
    "https://actionsack.com/img/420/telluhwat.webp",
    "https://actionsack.com/img/420/thomas.webp",
    "https://actionsack.com/img/420/thomasrust.webp",
    "https://actionsack.com/img/420/timesheet.webp",
    "https://actionsack.com/img/420/toasted.webp",
    "https://actionsack.com/img/420/toystory.webp",
    "https://actionsack.com/img/420/wednesday.webp"
  ]
  bot.say(random.choice(fourtwozero))

@module.rule(".*:retardeyes:.*")
def retardeyes(bot, trigger):
  bot.say("https://cdn.discordapp.com/emojis/286222898836799488.png")

@module.rule("^thx.*")
def thx(bot, trigger):
  bot.say("https://actionsack.com/img/thx/thx.png")

@module.rule(r"^(thanks|thank\syou).*")
def thanks(bot, trigger):
  thanks = [
    "https://actionsack.com/img/thx/h3h3.webm",
    "https://actionsack.com/img/thx/t.hanks.mp4",
    "https://actionsack.com/img/thx/thankyou.mp4"
  ]
  bot.say(random.choice(thanks))

@module.rule("^😢$")
@module.commands("cry")
def crying(bot, trigger):
  """Bot will reply with a crying GIF or emoticon.
  Can also be summoned by sending a message that is only the 😢 emoji."""
  crying = [
    "https://actionsack.com/img/QQ/QQ000.webp",
    "https://actionsack.com/img/QQ/QQ001.webp",
    "https://actionsack.com/img/QQ/QQ002.webp",
    "https://actionsack.com/img/QQ/QQ003.webp",
    "https://actionsack.com/img/QQ/QQ004.webp",
    "https://actionsack.com/img/QQ/QQ005.webp",
    "https://actionsack.com/img/QQ/QQ006.webp",
    "https://actionsack.com/img/QQ/QQ007.webp",
    "ಥ_ಥ",
    "＞︿＜",
    "＞﹏＜",
    "X﹏X",
    "T_T"
  ]
  bot.say(random.choice(crying))

@module.rule(".*!pat(?!ch).*")
@module.commands("pat")
def pat(bot, trigger):
  pat_gifs = [
    "https://actionsack.com/img/pat/00.gif",
    "https://actionsack.com/img/pat/01.gif",
    "https://actionsack.com/img/pat/02.gif",
    "https://actionsack.com/img/pat/03.gif",
    "https://actionsack.com/img/pat/04.gif",
    "https://actionsack.com/img/pat/05.gif"
  ]
  bot.say(random.choice(pat_gifs))

@module.rule(r".*cry\sme\sa\sriver.*")
def cryriver(bot, trigger):
  bot.say("https://actionsack.com/img/QQ/QQ007.webp")

@module.rule(".*!(xms|bge).*")
def xms(bot, trigger):
  bot.say("w2g.tv/rooms/actionsack-csurhbl9dkwvwnk91a")

@module.rule(".*📖.*")
def book(bot, trigger):
  book = [
    "https://actionsack.com/img/mike/📖/📖.gif",
    "https://actionsack.com/img/mike/📖/📖.jpg",
    "https://actionsack.com/img/mike/📖/📖+.jpg",
    "https://actionsack.com/img/mike/📖/📖🐇.jpg"
  ]
  bot.say(random.choice(book))

@module.rule("^8D$")
def greg(bot, trigger):
  bot.say("Greg was never in IRC...")

@module.rule("^grimm$")
def grim(bot, trigger):
  bot.say("Probably still showering with his sister to this day...")

@module.rule("^FOAD.*")
def foad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/foad.png")

@module.rule(".*adapters.*")
def adapters(bot, trigger):
  adapters = [
    "https://actionsack.com/img/adapters/00.webp",
    "https://actionsack.com/img/adapters/01.webp",
    "https://actionsack.com/img/adapters/02.webp"
  ]
  bot.say(random.choice(adapters))

@module.rule(r".*accident\W")
def accident(bot, trigger):
  bot.say("https://actionsack.com/img/misc/accident.webp")

@module.rule(".*14nm.*")
def fourteennm(bot, trigger):
  bot.say("https://actionsack.com/img/misc/14nm+++++.mp4")

@module.rule(".*bait.*")
def bait(bot, trigger):
  bait = [
    "https://actionsack.com/img/bait/404bait.png",
    "https://actionsack.com/img/bait/all-bait.gif",
    "https://actionsack.com/img/bait/b8.png",
    "https://actionsack.com/img/bait/bai--what.png",
    "https://actionsack.com/img/bait/bait-g.gif",
    "https://actionsack.com/img/bait/bait-krunk.jpg",
    "https://actionsack.com/img/bait/bait-pole.png",
    "https://actionsack.com/img/bait/bait-sim.png",
    "https://actionsack.com/img/bait/bait-therapy.png",
    "https://actionsack.com/img/bait/bait.gif",
    "https://actionsack.com/img/bait/bait.png",
    "https://actionsack.com/img/bait/bait001.jpg",
    "https://actionsack.com/img/bait/bait002.png",
    "https://actionsack.com/img/bait/bait003.jpg",
    "https://actionsack.com/img/bait/bait004.jpg",
    "https://actionsack.com/img/bait/bait005.jpg",
    "https://actionsack.com/img/bait/bait006.png",
    "https://actionsack.com/img/bait/bait007.png",
    "https://actionsack.com/img/bait/bait008.png",
    "https://actionsack.com/img/bait/bait009.jpg",
    "https://actionsack.com/img/bait/bait010.jpg",
    "https://actionsack.com/img/bait/bait011.jpg",
    "https://actionsack.com/img/bait/bait012.jpg",
    "https://actionsack.com/img/bait/bait013.jpg",
    "https://actionsack.com/img/bait/bait014.jpg",
    "https://actionsack.com/img/bait/bait015.jpg",
    "https://actionsack.com/img/bait/bait016.jpg",
    "https://actionsack.com/img/bait/bait017.png",
    "https://actionsack.com/img/bait/bait018.png",
    "https://actionsack.com/img/bait/bait019.png",
    "https://actionsack.com/img/bait/bait020.jpg",
    "https://actionsack.com/img/bait/bait021.jpg",
    "https://actionsack.com/img/bait/bait022.png",
    "https://actionsack.com/img/bait/bait023.jpg",
    "https://actionsack.com/img/bait/bait024.jpg",
    "https://actionsack.com/img/bait/bait025.png",
    "https://actionsack.com/img/bait/bait026.png",
    "https://actionsack.com/img/bait/bait027.png",
    "https://actionsack.com/img/bait/baitkakke.jpg",
    "https://actionsack.com/img/bait/baitku.png",
    "https://actionsack.com/img/bait/baitnado.jpg",
    "https://actionsack.com/img/bait/baito.png",
    "https://actionsack.com/img/bait/changed-bait.jpg",
    "https://actionsack.com/img/bait/chosen-bait.png",
    "https://actionsack.com/img/bait/debait.png",
    "https://actionsack.com/img/bait/hq-bait.jpg",
    "https://actionsack.com/img/bait/MBGA.jpg",
    "https://actionsack.com/img/bait/mikes-bait.jpg",
    "https://actionsack.com/img/bait/poke-bait.png",
    "https://actionsack.com/img/bait/teach-bait.jpg",
    "https://actionsack.com/img/bait/whose-bait.jpg",
    "https://actionsack.com/img/bait/wtf-bait.jpg"
  ]
  bot.say(random.choice(bait))

@module.rule(".*backhand.*")
def backhand(bot, trigger):
  bot.say("https://actionsack.com/img/misc/backhand.mp4")

@module.rule("^😠$")
def angryeyes(bot, trigger):
  bot.say("https://actionsack.com/img/misc/angryeyes.webp")

@module.rule(".*alot.*")
def alot(bot, trigger):
  bot.say("https://actionsack.com/img/alot/")

@module.rule(".*♿.*")
def handicap(bot, trigger):
  bot.say("https://actionsack.com/img/♿/♿.mp4")

@module.rule(".*⤵️.*")
def down(bot, trigger):
  bot.say("https://actionsack.com/img/mike/down.gif")

@module.rule(r"^\.\.\.$")
def dotdotdot(bot, trigger):
  bot.say("...")

@module.rule(r".*deez\snutz.*")
@module.commands("dz")
def deeznutz(bot, trigger):
  """Can also be triggered with "deez nutz" anywhere in a message."""
  deez_nutz = [
    formatting.bold("DEEZ NUTZ!"),
    "https://actionsack.com/img/nutz/aldeez.webp",
    "https://actionsack.com/img/nutz/dd.webp",
    "https://actionsack.com/img/nutz/grandma.webp",
    "https://actionsack.com/img/nutz/prez.webp",
    "https://actionsack.com/img/nutz/wood.webp"
  ]
  bot.say(random.choice(deez_nutz))

@module.commands("lenny", "rlenny")
def rlenny(bot, trigger):
  """Sends a random ( ͡° ͜ʖ ͡°) variation...or a GIF/MP4!"""
  rlenny = [
    "https://actionsack.com/img/lenny/anime.gif",
    "https://actionsack.com/img/lenny/crazy.mp4",
    "https://actionsack.com/img/lenny/spiral.gif",
    "( ͡° ͜ʖ ͡°)",
    "(☭ ͜ʖ ☭)",
    "( ° ͜ʖ °)",
    "(⟃ ͜ʖ ⟄) ",
    "( ‾ ʖ̫ ‾)",
    "( ͡° ʖ̯ ͡°)",
    "ʕ ͡° ʖ̯ ͡°ʔ",
    "( ͡° ل͜ ͡°)",
    "( ͡o ͜ʖ ͡o)",
    "( ͡◉ ͜ʖ ͡◉)",
    "( ͡☉ ͜ʖ ͡☉)",
    "ʕ ͡° ͜ʖ ͡°ʔ",
    "( ͡ᵔ ͜ʖ ͡ᵔ )",
    "¯\_( ͡° ͜ʖ ͡°)_/¯"
  ]
  bot.say(random.choice(rlenny))

@module.commands("shrug")
def shrugc(bot, trigger):
  bot.say("¯\\_(ツ)_/¯")

@module.commands("tableflip", "tflip")
def tableflip(bot, trigger):
  bot.say("(╯°□°）╯︵ ┻━┻")

@module.rule(r".*\(╯°□°）╯︵ ┻━┻.*")
def unflip(bot, trigger):
  bot.say("┬─┬﻿ ノ( ゜-゜ノ) — Please respect tables, {}.".format(trigger.nick))

@module.rule("^pranked!$")
def prank(bot, trigger):
  prank = [
    "https://actionsack.com/img/prank/prank01.png",
    "https://actionsack.com/img/prank/prank02.png"
  ]
  bot.say(random.choice(prank))

@module.rule(r"^\?{3,}$")
def que(bot, trigger):
  bot.say("https://actionsack.com/img/misc/¿¿¿.webp")

@module.rule(r"^\\o/$")
def handsup(bot, trigger):
  bot.say("\\o/")

@module.rule(r"^¯\\\_\(ツ\)_\/¯(\s$|$)")
def shrug(bot, trigger):
  bot.say("¯\\_(ツ)_/¯")

@module.rule(".*🦏.*")
def rhino(bot, trigger):
  bot.say("https://actionsack.com/img/🦏/🦏.webp")

@module.rule(".*🧀.*")
def cheese(bot, trigger):
  bot.say("https://actionsack.com/img/🧀/🧀.mp4")

@module.rule(".*🦄.*")
def unicorn(bot, trigger):
  bot.say("https://actionsack.com/img/🦄/🦄.webp")

@module.rule("^🙃$")
def upsidedown(bot, trigger):
  bot.say("🙃")

@module.rule("^🖕(|🏻|🏼|🏽|🏾|🏿)$")
def fuckyouback(bot, trigger):
  bot.say("Fuck you, {}!".format(trigger.nick))

@module.rule("^👏$")
def clap(bot, trigger):
  bot.say("👏🏻👏🏼👏🏽👏🏾👏🏿")

@module.rule("^👍$")
def thumbsup(bot, trigger):
  bot.say("👍🏻👍🏼👍🏽👍🏾👍🏿")

@module.rule("^👎$")
def thumbsdown(bot, trigger):
  bot.say("👎🏻👎🏼👎🏽👎🏾👎🏿")

@module.rule("^👌$")
def okhand(bot, trigger):
  bot.say("👌🏻👌🏼👌🏽👌🏾👌🏿")

@module.rule("^👋$")
def wave(bot, trigger):
  bot.say("👋🏻👋🏼👋🏽👋🏾👋🏿")

@module.rule("^🖖$")
def vulcansalute(bot, trigger):
  bot.say("🖖🏻🖖🏼🖖🏽🖖🏾🖖🏿")

@module.rule("^💪$")
def muscle(bot, trigger):
  bot.say("💪🏻💪🏼💪🏽💪🏾💪🏿")

@module.rule("^🤞$")
def crossed(bot, trigger):
  bot.say("🤞🏻🤞🏼🤞🏽🤞🏾🤞🏿")

@module.rule(".*(🌎|🌍|🌏).*")
def earthchan(bot, trigger):
  bot.say("https://actionsack.com/img/🌎/water.png")

@module.rule("^🐉$")
def dragon(bot, trigger):
  bot.say("https://p.xnaas.info/dragon.gif")

@module.rule("^🏈$")
def football(bot, trigger):
  football = [
    "D'Marcus Williums",
    "T.J. Juckson",
    "T'varisuness King",
    "Jackmerius Tacktheritrix",
    "D'Squarius Green, Jr.",
    "Dan Smith",
    "The Player Formerly Known as Mousecop",
    "Ibrahim Moizoos",
    "D'Isiah T. Billings-Clyde",
    "D'Jasper Probincrux III",
    "Leoz Maxwell Jilliumz",
    "Javaris Jamar Javarison-Lamar",
    "Davoin Shower-Handel",
    "Hingle McCringleberry",
    "L'Carpetron Dookmarriot",
    "J'Dinkalage Morgoone",
    "Xmus Jaxon Flaxon-Waxon",
    "Saggitariutt Jefferspin",
    "D'Glester Hardunkichud",
    "Swirvithan L'Goodling-Splatt",
    "Quatro Quatro",
    "Ozamataz Buckshank",
    "Beezer Twelve Washingbeard",
    "Shakiraquan T.G.I.F. Carter",
    "X-Wing @Aliciousness",
    "Sequester Grundelplith M.D.",
    "Scoish Velociraptor Maloish",
    "T.J. A.J. R.J. Backslashinfourth V",
    "Eeeee Eeeeeeeee",
    "Donkey Teeth",
    "Torque [Construction Noise] Lewith",
    "Tyroil Smoochie-Wallace"
  ]
  bot.say(random.choice(football))

@module.rule(".*🍍(|\s)🍕.*")
def sin(bot, trigger):
  bot.say("This is a sin.")

@module.rule(".*xfiles.*")
def xfiles(bot, trigger):
  bot.say("Did you know that the X-Files is going to have 6 new episodes this summer on FOX, Aegisfate?")

@module.rule(".*triggered.*")
def triggered(bot, trigger):
  triggered = [
    "https://actionsack.com/img/triggered/beaker.webp",
    "https://actionsack.com/img/triggered/triggered.webp",
    "https://actionsack.com/img/triggered/feek.webp"
  ]
  bot.say(random.choice(triggered))

@module.rule(r".*to\sbe\sfair.*")
def tobefair(bot, trigger):
  bot.say("https://actionsack.com/img/videos/tobefair.webm")

@module.rule(r".*stop\sbeing\spoor.*")
def stopbeingpoor(bot, trigger):
  bot.say("https://actionsack.com/img/misc/stopbeingpoor.jpg")

@module.rule(".*!tb.*")
@module.commands("tb")
def tb(bot, trigger):
  """Spout technobabble."""
  tb = [
    "When you account for the nm offset variable, the difference between 32-bit and 64-bit CPUs really only matters when calculating differential sub-routine pipeline algorithms.",
    "high 32-bit TOS encrypted voIP",
    "remote access through TeamSpeak",
    "if you reboot it may cement the command scripts that the virus is using to distribute DDOS variants",
    "When the biometrics of the boot sector exceeds the buffer cache then clock-cycles reroute to the LAN thus creating  a load balancing markup stack.",
    "I'll start on a GUI in Visual Basic to backtrack the mainframe.",
    "You can use the ps commands to redirect you to the home directory provided you used the subversion syntax correctly.",
    "The Internet is like water in pipes: when one pipe gets cut the Internet pressure drops because it is leaking uncontrollably from the open pipe. The Internet through WiFi, however, is like a swimming pool. If you open a hole in the building or pool the wifi starts flooding out and the wifi starts to lower. That's the reasoning behind revolving doors. Since they're compartmentalized, the building loses a smaller, fixed amount of internet per entry/exit, which reduces costs and allows more consistency for planning an office's WiFi needs.",
    "I JSON SQL DBs all the time!",
    "Lol you a pussyyyyy when I pull your IP address I'm gonna take your account then you gonna have to make a new account bc you cant get it back",
    "Can't leave without your processor? Clone it! You can copy the processor operating code wirelessly with a sniffer device.",
    "Then they do a triple worm blue cobalt IP hack.",
    "That's how the hacking's done. Satellite telemetry.",
    "SECURITY UPDATES CAUSE AUTISM. WON'T SOMEBODY THINK OF THE CHILDREN???",
    "The asymmetrical phase splitter is offline. We need to compensate for the gravimetric charge imbalance by re-routing power through the electron plasma injector port.",
    "Overheating weak partitions inverts the critical protocols.",
    "Higher numbered ports are always faster, because they travel nearer the outside of the wire, and the 'skin effect' means that that type of transmission is more reliable. So port 80 is going to be slower. If you want to connect with a very fast speed, you might want to try port 3389. This is why when you connect to port 22 you're probably only going to get some kind of text interface, if you connect to port 80 you might get some images along with it, and if you connect to port 3389, you'll get to see and interact with the whole operating system.",
    "That's a node brainer!",
    "Laptops generally don't need to take as many breaks/pauses as desktops, so they don't need that key. Sometimes, the larger laptops like yours w/ a numpad will have it, but only if the laptop hasn't worked out in a while, and gets winded easily.",
    "In order to hack a laptop's battery you need to initiate a GET request from an HTML page then use CSS to parse the DOS command XPLDBTRY.EXE that will make the battery's cooling fail, and then explode.",
    "Atlas Seeds contain zonally-shifted quasi-stellar substrate. WARNING: do not allow matrix to commune with this dimensional space.",
    "Sending packets is reserved to level 1337 hackers only. If you really want to do this you would need to bypass the FireWire's mainframe on your computer. Then you would need to encrypt and enumerate the firewall of whatever server you are trying to send the packet to. Then you would need to exploit the server's hypervisor root code to overflow the VGA interface. After that, all you need to do is code a VPN in Visual Basic and you should be able to do it without any problems.",
    "You should rebuild the kernel but only after rebooting your router. It gets a bit tricky with the buttons 'cause you need to press ctrl + alt + printscreen for 5 seconds and at the same time the reset button on your router. Last time I used my hands for the keyboard and reached for the router with one foot and managed to send the packet, although I also installed a firewall on Winamp and now I can only play Nickelback songs.",
    "Yeah but quantum info extraction was patched by the NSA last month, you gotta entangle the data stream to a local area network loop now.",
    "Don't worry, you'll just need to use a Raspberry Pi to enable four-factor authentication VPN firewalls and he won't be able to get into the mainframe!",
    "Uh oh, his friend is good with Linux! Better watch out! He might grep into your sudoers file and DDoS your hard drive!",
    "We reverse engineered Amazo's operating system and whipped up a virus to wipe his CPU.",
    "He's got a better grasp on Python 6 malware encryption than anybody at the DEO.",
    "I don't want to say the computer is old, but its IP address was 1.",
    "Are you coding in SQL or Java?",
    "Your UI is open-source JPEGs you got from MP3s off the web.",
    "Software running slow? Just decompile it!",
    "The secondary gyrodyne relays of the propulsion field intermatrix have depolarized!",
    "The Enterprise computer system is controlled by three primary main processing cores, cross-linked with a redundant melacortz ramistat. Fourteen kiloquad interface modules. The core element is based on an FTL nanoprocessor with twenty five bilateral kelilactirals, with twenty of those being slaved into the primary heisenfram terminal.",
    "Shunt plasma from the buzzard collectors into the Heisenberg compensators in order to generate sufficient tachyon emissions to disperse neutrino buildup around the warp core, thereby establishing a static warp bubble!",
    "Nanogel. It acts as a quantum transducer.",
    "Don’t forget to move your mouse counter clockwise to reverse the logging process.",
    "But since their cryptographic protocols use poly-phasic entagled waveforms, cracking a code set would take half a century.",
    "If I can just overclock the UNIX django, I can BASIC the DDOS root. Damn. No Dice. But wait...if I disencrypt their kilobytes with a backdoor handshake then...jackpot!"
  ]
  bot.say(random.choice(tb), max_messages=2)

@module.commands("jolly")
@module.rate(server=43200)
def jolly(bot, trigger):
  """Nothing tops The Jolly Rancher story.
  Server-wide rate limit of once every 12 hours."""
  bot.say("Nothing tops the Jolly Rancher story.")
  bot.say("Steve and his girlfriend Samantha went off to college in August. She went to Florida State, he went to Penn. So, she decides to fly to PA to visit him. He was really happy to see her so he decided to give her some oral action.")
  bot.say("He had done this numerous times before and he always enjoyed doing it...but for some reason, this time, she smelled really horrible, and she tasted even worse. He didn't want to offend her though because he hadn't seen her in months...so he put a Jolly Rancher in his mouth to cover it up, even though it didn't do much to help.")
  bot.say("In the course of eating her out, he accidentally pushed the candy inside of her... and stuck a finger in to grab it out. He took it out, and put it back into his mouth and bit it. Only...it wasn't the Jolly Rancher.")
  bot.say("It was a nodule of gonorrhea.")
  bot.say("As in, the blister-like structure that gonorrhea makes filled with diseased pus was the size of a fucking Jolly Rancher and the poor guy BIT it. I guess it was really dark in the room. He freaked out and started vomiting all over the place when it exploded in his mouth...")
  bot.say("He demanded to know what was going on, turns out she had cheated on him at a club like, the first week of college, and fucked some random guy and the stupid bitch had no clue what was wrong with her. She noticed a strange smell though.")
  bot.say("So now, Steve is freaking out that he now has gonorrhea of the mouth and God knows what else.")

@module.commands("hg")
def hg(bot, trigger):
  """I've got the highground now!"""
  bot.say("https://actionsack.com/img/misc/highground.jpg")

@module.rule(".*!fgr.*")
@module.commands("fgr")
def fgr(bot, trigger):
  """Family Guy reference!!!!!
  Can also be triggered with '!fgr' anywhere in a message."""
  fgr = [
    "https://actionsack.com/img/fgr/gay.jpg",
    "https://actionsack.com/img/fgr/gears.jpg",
    "https://actionsack.com/img/fgr/hang.gif",
    "https://actionsack.com/img/fgr/stewie-gun.jpg"
  ]
  bot.say(random.choice(fgr))

@module.rule(".*!adr.*")
@module.commands("adr")
def adr(bot, trigger):
  """American Dad reference!
  Can also be triggered with '!adr' anywhere in a message."""
  bot.say("https://actionsack.com/img/fgr/ADR.jpg")

@module.rule(".*!csr.*")
@module.commands("csr")
def csr(bot, trigger):
  """Cleveland Show reference!
  Can also be triggered with '!csr' anywhere in a message."""
  bot.say("https://actionsack.com/img/fgr/CSR.jpg")

@module.commands("aegislive")
def aegislive(bot, trigger):
  """Aegisfate's YouTube livestream link."""
  bot.say("https://youtube.com/user/mac2486/live")

# === NSFW Commands ===
@module.rule(".*!!banebread.*")
def banebread(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/banebread.png")

@module.rule(".*!!bread.*")
def bread(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/🍞.png")

@module.rule(".*!!datascii.*")
def datascii(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/datascii.gif")

@module.rule(".*!!dickaroo.*")
def dickaroo(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/dickaroo.gif")

@module.rule(".*!!fgr.*")
def fgrnsfw(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/chris-in-brian.png")

@module.rule(".*!!ghostbabies.*")
def ghostbabies(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/ghostbabies.gif")

@module.rule(".*!!gimp.*")
def gimp(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/gimp.gif")

@module.rule(".*!!nazi.*")
def nazi(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/nazi.gif")

@module.rule(".*!!ponies.*")
def ponies(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/ponies.mp4")

@module.rule(".*!!jordan.*")
def jordan(bot, trigger):
  jordan = [
    "https://actionsack.com/img/jordan/ddosvariants.png",
    "https://actionsack.com/img/jordan/littledick.png"
  ]
  bot.say(random.choice(jordan))
# === NSFW Commands ===

@module.rule("^!b8$")
def beight(bot, trigger):
  bot.say("steam://install/567090")

@module.rule(".*!kristen.*")
def kristen(bot, trigger):
  kristen = [
    "https://actionsack.com/img/kristen/chainsmokers.png",
    "https://actionsack.com/img/kristen/keith.png",
    "https://actionsack.com/img/kristen/pidgey.png",
    "https://actionsack.com/img/kristen/pins.png",
    "https://actionsack.com/img/kristen/racist.png",
    "https://actionsack.com/img/kristen/rekt.png",
    "https://actionsack.com/img/kristen/repost.png",
    "https://actionsack.com/img/kristen/top.png"
  ]
  bot.say(random.choice(kristen))

@module.rule(r"^Tasian\sloves\spickles\.($|\s)")
def tasianpickles(bot, trigger):
  bot.say("https://actionsack.com/img/tasian/pickles.webp")

@module.rule(".*!asg.*")
@module.commands("asg")
def allsystemsgo(bot, trigger):
  """Can also be triggered with "!asg" anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/asg.webp")

@module.rule(".*murica.*")
@module.commands("america")
def murica(bot, trigger):
  """Summons Freedom™ into chat.
  Can also be triggered with 'murica' anywhere in a message."""
  murica = [
    "https://actionsack.com/img/murica/clapping.mp4",
    "https://actionsack.com/img/murica/kiss.gif",
    "https://actionsack.com/img/murica/knockknock.gif",
    "https://actionsack.com/img/murica/freedomaf.mp4"
  ]
  bot.say(random.choice(murica))

@module.rule(".*!knock.*")
@module.commands("knock")
def knock(bot, trigger):
  """RP: America knocks on your door...
  Can also be triggered with '!knock' anywhere in a message."""
  bot.say("https://actionsack.com/img/murica/knockknock.gif")

@module.commands("pledge")
@module.rate(channel=5400)
def pledge(bot, trigger):
  """Say the United States Pledge of Allegiance.
  Channel-wide rate-limit of 90 minutes."""
  bot.say("I pledge allegiance to the flag of the United States of America. Thank you very very much for letting us little kids live here. It really really was nice of you. You didn't have to do it. And it's really not creepy to have little little kids mindlessly recite this anthem every day and pledge their life to a government before theyre old enough to really think about what they're saying.")
  bot.say("This is not a form of brainwashing. This is not a form of brainwashing. This is not a form of brainwashing.")
  bot.say("This is really the greatest country in the whole world. All the other countries suck. And if this country ever goes to go to war, as its often wont to do, I promise to help go and kill all the other country's kids.")
  bot.say("God bless Johnson & Johnson. God bless GE. God bless Citigroup.")

@module.rule(".*mushkin.*")
@module.rate(channel=900)
def mushkin(bot, trigger):
  bot.say("Hey xnaas and feek, did you know that Mushkin announced a 4TB SSD for $500 at CES 2016 and never fuckin' delivered? How neat is that?")

@module.commands("mirai")
def mirai(bot, trigger):
  """Gone but not forgotten, noble soviet bear."""
  bot.say("https://actionsack.com/img/putin/🐻.mp4")

@module.rule(".*!putin.*")
@module.commands("putin")
def putin(bot, trigger):
  """Posts a Putin meme of some sort.
  Can also be triggered with '!putin' anywhere in a message."""
  putin = [
    "https://actionsack.com/img/putin/dance.mp4",
    "https://actionsack.com/img/putin/pigeon.mp4",
    "https://actionsack.com/img/putin/ritz.gif",
    "https://actionsack.com/img/putin/🐻.mp4"
  ]
  bot.say(random.choice(putin))

@module.commands("aidsclub")
def aidsclub(bot, trigger):
  """Welcome to the club, loser."""
  bot.say("https://actionsack.com/img/misc/aidsclub.webp")

@module.rule(".*!barometer.*")
@module.commands("barometer")
def barometer(bot, trigger):
  bot.say("https://actionsack.com/img/misc/barometer.webp")

@module.rule(r"^Oh,\syou!$")
def ohyou(bot, trigger):
  bot.say("https://actionsack.com/img/misc/Oh,you!.jpg")

@module.rule(".*!battletoad.*")
@module.commands("battletoad")
def battletoad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/battletoad.mp4")

@module.rule(".*!beaker.*")
@module.commands("beaker")
def beaker(bot, trigger):
  bot.say("https://actionsack.com/img/misc/beaker.mp4")

@module.rule(".*!bomb.*")
@module.commands("bomb")
def bomb(bot, trigger):
  """Bombs Japan again... :/
  Can also be triggered with '!bomb' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/bomb.mp4")

@module.rule(".*!broden.*")
@module.commands("broden")
def broden(bot, trigger):
  bot.say("https://actionsack.com/img/misc/broden.mp4")

@module.rule(r".*mikey\sbikey.*")
def mikeybikey(bot, trigger):
  bot.say("https://actionsack.com/img/as/mikeybikey.png")

@module.rule(r".*meal\swith\sit.*")
def mealwithit(bot, trigger):
  bot.say("https://actionsack.com/img/deal/mealwithit.webp")

@module.rule(r".*deal\swith\sit.*")
def dealwithit(bot, trigger):
  deal = [
    "https://actionsack.com/img/deal/brule.webp",
    "https://actionsack.com/img/deal/coolkid.webp",
    "https://actionsack.com/img/deal/hippo.mp4",
    "https://actionsack.com/img/deal/mealwithit.webp",
    "https://actionsack.com/img/deal/spider.webp",
    "https://actionsack.com/img/deal/squirtle.webp",
    "https://actionsack.com/img/deal/tf2.webp"
  ]
  bot.say(random.choice(deal))

@module.rule(".*!mindjack.*")
def mindjack(bot, trigger):
  bot.say("https://actionsack.com/img/misc/mindjack.png")

@module.commands("doge")
def doge(bot, trigger):
  """Doge memes! (There's not very many...)"""
  doge = [
    "https://actionsack.com/img/doge/batdoge.webp",
    "https://actionsack.com/img/doge/dogemine.webp",
    "https://actionsack.com/img/doge/skeledoge.webp"
  ]
  bot.say(random.choice(doge))

@module.rule(".*!dogemine.*")
def dogemine(bot, trigger):
  bot.say("https://actionsack.com/img/doge/dogemine.webp")

@module.rule(".*!skeledoge.*")
def skeledoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/skeledoge.webp")

@module.rule(".*!batdoge.*")
def batdoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/batdoge.webp")

@module.rule(r".*slow\sdown.*")
def slowdown(bot, trigger):
  bot.say("https://www.youtube.com/watch?v=fJdqw-JzW08")

@module.require_admin
@module.commands("smmcb", "smd")
def smmcb(bot, trigger):
  bot.say("https://actionsack.com/img/misc/smmcb.gif")

@module.rule("^(noice)$")
def noice(bot, trigger):
  bot.say(trigger.group(1))

@module.rule(".*sockbot.*")
def sockbot(bot, trigger):
  sockbot = [
    "https://actionsack.com/img/sockbot/headsortails.png",
    "https://actionsack.com/img/sockbot/knife.png",
    "https://actionsack.com/img/sockbot/L337.png",
    "https://actionsack.com/img/sockbot/phone.png",
    "Gone, but not forgotten.",
    "Good riddance to Discord, but RIP Sockbot. 😢"
  ]
  bot.say(random.choice(sockbot))

@module.rule(".*!brony.*")
@module.commands("brony")
def brony(bot, trigger):
  bot.say("https://actionsack.com/img/mike/brony.png")

@module.rule("^banned.*")
def banned(bot, trigger):
  banned = [
    "https://actionsack.com/img/banned/beetlejuice.mp4",
    "https://actionsack.com/img/banned/carryon.png",
    "https://actionsack.com/img/banned/clapping.gif",
    "https://actionsack.com/img/banned/hammer00.webp",
    "https://actionsack.com/img/banned/hammer01.webp",
    "https://actionsack.com/img/banned/hanging.gif",
    "https://actionsack.com/img/banned/samuel.gif",
    "https://actionsack.com/img/banned/slapbeavis.gif",
    "https://actionsack.com/img/banned/slap.gif",
    "https://actionsack.com/img/banned/tasian.gif",
    "https://actionsack.com/img/banned/trash.png",
    "https://actionsack.com/img/banned/trump.gif",
    "https://actionsack.com/img/banned/voodoo.png",
    "https://actionsack.com/img/banned/xbox.png",
    "https://actionsack.com/img/banned/xnaas.gif"
  ]
  bot.say(random.choice(banned))

@module.rule(".*boycott.*")
def boycott(bot, trigger):
  bot.say("https://actionsack.com/img/misc/boycott.webp")

@module.rule(".*censor.*")
def censor(bot, trigger):
  censor = [
    "https://actionsack.com/img/censored/bunny.webp",
    "https://actionsack.com/img/censored/censored.webp",
    "https://actionsack.com/img/censored/eyesored.webp",
    "https://actionsack.com/img/censored/fox.webp",
    "https://actionsack.com/img/censored/fren.webp",
    "https://actionsack.com/img/censored/nose.webp",
    "https://actionsack.com/img/censored/spider.webp",
    "https://actionsack.com/img/censored/tasian.webp"
  ]
  bot.say(random.choice(censor))

@module.rule("^(P|B|Ch|D|S|W)ing!$")
def pingpong(bot, trigger):
  bot.say("{}ong!".format(trigger.group(1)))

@module.rule("^Marco!$")
def marcopolo(bot, trigger):
  bot.say("Polo!")

@module.rule("^(W)ee!$")
def marcopolo(bot, trigger):
  bot.say("{}oo!".format(trigger.group(1)))

@module.rule(".*!work.*")
@module.commands("work")
def worktoday(bot, trigger):
  """I don't really wanna do the work today..."""
  bot.say("https://actionsack.com/img/videos/work.webm")

@module.rule(".*stbyn.*")
def stbyn(bot, trigger):
  bot.say("Sucks to be you, {}!".format(formatting.italic("nerd")))

@module.rule(".*🥓.*")
def bacon(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🥓.mp4")

@module.rule(".*🍜.*")
def soupbowl(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍜.mp4")

@module.rule(".*🍞.*")
def breadchan(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍞.png")

@module.rule(".*🎅(|🏻|🏼|🏽|🏾|🏿).*")
def santa(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎅.png")

@module.rule(".*🎧.*")
def headphones(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎧.png")

@module.rule(r".*fuck\syou(?!r).*")
def fuckyou(bot, trigger):
  fuckyou = [
    "https://actionsack.com/img/fuck/you/airline.webp",
    "https://actionsack.com/img/fuck/you/anime.mp4",
    "https://actionsack.com/img/fuck/you/ape.webp",
    "https://actionsack.com/img/fuck/you/aquaman.webp",
    "https://actionsack.com/img/fuck/you/arrow.webp",
    "https://actionsack.com/img/fuck/you/bb8.webp",
    "https://actionsack.com/img/fuck/you/bird.webp",
    "https://actionsack.com/img/fuck/you/bot.webp",
    "https://actionsack.com/img/fuck/you/buzz.webp",
    "https://actionsack.com/img/fuck/you/card.webp",
    "https://actionsack.com/img/fuck/you/climb.webp",
    "https://actionsack.com/img/fuck/you/compilation.webp",
    "https://actionsack.com/img/fuck/you/cutout.webp",
    "https://actionsack.com/img/fuck/you/deaf.webp",
    "https://actionsack.com/img/fuck/you/deer.webp",
    "https://actionsack.com/img/fuck/you/driving.webp",
    "https://actionsack.com/img/fuck/you/drums.webp",
    "https://actionsack.com/img/fuck/you/enthusiastic.webp",
    "https://actionsack.com/img/fuck/you/faoy.webp",
    "https://actionsack.com/img/fuck/you/friday.webp",
    "https://actionsack.com/img/fuck/you/fuku.webp",
    "https://actionsack.com/img/fuck/you/fur.webp",
    "https://actionsack.com/img/fuck/you/godzilla.webp",
    "https://actionsack.com/img/fuck/you/goldenboye.webp",
    "https://actionsack.com/img/fuck/you/grow.webp",
    "https://actionsack.com/img/fuck/you/h3h3.webp",
    "https://actionsack.com/img/fuck/you/hook.webp",
    "https://actionsack.com/img/fuck/you/jacket.webp",
    "https://actionsack.com/img/fuck/you/juliemao.webp",
    "https://actionsack.com/img/fuck/you/kraken.webp",
    "https://actionsack.com/img/fuck/you/loop.webp",
    "https://actionsack.com/img/fuck/you/marvel.webp",
    "https://actionsack.com/img/fuck/you/peaceamongworlds.webp",
    "https://actionsack.com/img/fuck/you/pigeon.webp",
    "https://actionsack.com/img/fuck/you/pocket.webp",
    "https://actionsack.com/img/fuck/you/pocketcat.webp",
    "https://actionsack.com/img/fuck/you/ragnarok.webp",
    "https://actionsack.com/img/fuck/you/rudy.webp",
    "https://actionsack.com/img/fuck/you/samuel.webp",
    "https://actionsack.com/img/fuck/you/samueltransparent.webp",
    "https://actionsack.com/img/fuck/you/sayan.webp",
    "https://actionsack.com/img/fuck/you/skating.webp",
    "https://actionsack.com/img/fuck/you/space_invader.webp",
    "https://actionsack.com/img/fuck/you/square.webp",
    "https://actionsack.com/img/fuck/you/tommydoor.webp",
    "https://actionsack.com/img/fuck/you/trumpet.webp",
    "https://actionsack.com/img/fuck/you/westworld.webp",
    "https://actionsack.com/img/fuck/you/ww-mib.webp",
    "https://actionsack.com/img/fuck/you/☂.webp"
  ]
  bot.say(random.choice(fuckyou))

@module.rule(r".*(gfy(?!c)|go\sfuck\syourself).*")
def gfy(bot, trigger):
  gfy = [
    "https://actionsack.com/img/fuck/urself/01_Two_Feet-Go_Fuck_Yourself.opus",
    "https://actionsack.com/img/fuck/urself/anime.webp",
    "https://actionsack.com/img/fuck/urself/arms.webp",
    "https://actionsack.com/img/fuck/urself/disney.webp",
    "https://actionsack.com/img/fuck/urself/doggo.webp",
    "https://actionsack.com/img/fuck/urself/gay.webp",
    "https://actionsack.com/img/fuck/urself/gfy.webp",
    "https://actionsack.com/img/fuck/urself/rugrats.webp",
    "https://actionsack.com/img/fuck/urself/science.webp"
  ]
  bot.say(random.choice(gfy))

@module.rule(r"^What\sthe\sfuck\?$")
def wtfquestion(bot, trigger):
  bot.say("https://actionsack.com/img/wtf/wtf¿.gif")

@module.rule(r"^What\sthe\sfuck!$")
def wtfexclamation(bot, trigger):
  bot.say("https://actionsack.com/img/wtf/wtfh3h3.mp4")

@module.rule("^Fuck!$")
def fuckexclamation(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuck!.webp")

@module.rule(r"^Fuck\syeah!$")
def fuckyeah(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuckyeah!.webp")

@module.rule(r".*fuck\severything.*")
def fuckeverything(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuckeverything.webp")

@module.rule(".*ftge.*")
def ftge(bot, trigger):
  ftge = [
    "https://actionsack.com/img/fuck/ftge-a.webp",
    "https://actionsack.com/img/fuck/ftge.webp"
  ]
  bot.say(random.choice(ftge))

@module.rule(r".*fooled\syou.*")
def fooledyou(bot, trigger):
  bot.say("https://actionsack.com/img/misc/fooled.png")

@module.rule(r".*fite\sme.*")
def fiteme(bot, trigger):
  fiteme = [
    "https://actionsack.com/img/fite/cat.gif",
    "https://actionsack.com/img/fite/phones.gif",
    "https://actionsack.com/img/fite/🌮.gif"
  ]
  bot.say(random.choice(fiteme))

@module.rule(r"^Found\sout\sI\'m\sgay(|\.|\s)$")
@module.rate(server=21600)
def fagexclamation(bot, trigger):
  bot.say("You're gay. Hey poofta. You're a homo. You're a homo you faggot. Go suck a dick. Go suck a real big dick. Get those dick so far in your mouth that the dick's right there, you got 'em all the way, smashing the back of your throat, balls right there, bangin' on your chin. That's how much I want you to suck dick. Oi. This is me. Pretending to be you. Fist-fuckin' another man in the asshole. Just fist-fuckin' the god-givin' shit out of him. I bet you like that so much you'd like to get fist-fucked while you're doing it. Just getting fist-fucked while you're fist-fuckin' someone else. While you're at it chuck in another one. Just fist-fuckin' two strange men, getting your asshole fist-fucked with someone you just met on Grinder. I bet you wish these were dicks. I bet you wish these were big floppy dicks. You're in a big forest of dicks. Getting dicks all over ya. Covering yourself in cum. Loving cum. Can I suck your dick? Can I suck your dick and then kiss you? Kiss you square on the mouth and then fuck you? Scratch that. Can we make love? Can we make love in my bedroom and then maybe if we connect on more than just a physical level, I'll take you out, I'll introduce you to my mum and my dad and my little sister Jennifer, she's really cool. She's into Goosebumps at the moment. And then maybe we can all go out for dinner together. And they'll really like you because of your cool taste in music and your wonderful dress sense. And then maybe, after confronting their initial misguided preconceptions, my family will come to respect our love for its tangibility. And they'll reject it because of bias or religious and political agendas of hate that have been weaved through the social fabric of hundreds and hundreds of years. FAGGOT!!!", max_messages=6)

@module.rule(".*fags.*")
def fags(bot, trigger):
  bot.say("https://actionsack.com/img/faggot/fags.png")

@module.rule(".*fag(?!s).*")
def faggot(bot, trigger):
  faggot = [
    "https://actionsack.com/img/faggot/faggot.gif",
    "https://actionsack.com/img/faggot/oh.gif",
    "https://actionsack.com/img/faggot/urafaget.png",
    "Faggot!",
    "(/¯◡ ‿ ◡)/¯ ~~~~ Abracadabra, you're a faggot!"
  ]
  bot.say(random.choice(faggot))

@module.rule("^Gay!$")
def gayexclamation(bot, trigger):
  gayexclamation = [
    "https://actionsack.com/img/gay/gay!.webp",
    "https://actionsack.com/img/gay/gayshit.webp"
  ]
  bot.say(random.choice(gayexclamation))

@module.rule(r".*everything's\sfucked.*")
def everythingsfucked(bot, trigger):
  bot.say("https://actionsack.com/img/misc/everythingsfucked.gif")

@module.rule(r"^o\sshit.*")
def datboi(bot, trigger):
  oshit = [
    "https://actionsack.com/img/oshit/8ball.png",
    "https://actionsack.com/img/oshit/actorboi.gif",
    "https://actionsack.com/img/oshit/bikeboi.gif",
    "https://actionsack.com/img/oshit/boistory3.png",
    "https://actionsack.com/img/oshit/busboi.png",
    "https://actionsack.com/img/oshit/darksouls.png",
    "https://actionsack.com/img/oshit/datboi.gif",
    "https://actionsack.com/img/oshit/deadboi.gif",
    "https://actionsack.com/img/oshit/edgy.png",
    "https://actionsack.com/img/oshit/fallen.png",
    "https://actionsack.com/img/oshit/fancy.png",
    "https://actionsack.com/img/oshit/fastboi.gif",
    "https://actionsack.com/img/oshit/fellow.png",
    "https://actionsack.com/img/oshit/ghostboi.png",
    "https://actionsack.com/img/oshit/greninja.png",
    "https://actionsack.com/img/oshit/haramboi.png",
    "https://actionsack.com/img/oshit/IRL.png",
    "https://actionsack.com/img/oshit/iWish.png",
    "https://actionsack.com/img/oshit/jewboi.png",
    "https://actionsack.com/img/oshit/komradboi.png",
    "https://actionsack.com/img/oshit/lasthope.png",
    "https://actionsack.com/img/oshit/milkshake.png",
    "https://actionsack.com/img/oshit/mortyboi.png",
    "https://actionsack.com/img/oshit/movie.png",
    "https://actionsack.com/img/oshit/newboi.png",
    "https://actionsack.com/img/oshit/news.png",
    "https://actionsack.com/img/oshit/objectionboi.png",
    "https://actionsack.com/img/oshit/origin.gif",
    "https://actionsack.com/img/oshit/pajamaboi.png",
    "https://actionsack.com/img/oshit/playboi.png",
    "https://actionsack.com/img/oshit/poolboi.png",
    "https://actionsack.com/img/oshit/poster.png",
    "https://actionsack.com/img/oshit/realluke.png",
    "https://actionsack.com/img/oshit/reasons.png",
    "https://actionsack.com/img/oshit/sexboi.png",
    "https://actionsack.com/img/oshit/shiningboi.png",
    "https://actionsack.com/img/oshit/starwars.png",
    "https://actionsack.com/img/oshit/suicideboi.png",
    "https://actionsack.com/img/oshit/sweater.png",
    "https://actionsack.com/img/oshit/teamboi.png",
    "https://actionsack.com/img/oshit/towers.png",
    "https://actionsack.com/img/oshit/trumpboi.png",
    "https://actionsack.com/img/oshit/warriorboi.png",
    "https://actionsack.com/img/oshit/wat.png",
    "https://actionsack.com/img/oshit/woodwork.png"
  ]
  bot.say(random.choice(oshit))

@module.commands("spl")
def smitepro(bot, trigger):
  """YouTube and Twitch links for the Smite Pro League stream."""
  bot.say("YT: youtube.com/user/smitegame/live | Twitch: twitch.tv/smitegame")

@module.rule(".*!xmas.*")
@module.commands("xmas")
def xmassong(bot, trigger):
  """The only good Christmas song.
  Can also be triggered with '!xmas' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/xmas.webm")

@module.rule(".*!swat.*")
@module.commands("swat")
def swat(bot, trigger):
  """Summon SWAT into chat.
  Can also be triggered with '!swat' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/SWAT.mp4")

@module.rule(".*(▫|◽|◻|⬜|▪|◾|◼|⬛|🟥|🟧|🟨|🟩|🟦|🟪|🟫).*")
def square(bot, trigger):
  bot.say("https://actionsack.com/img/videos/square.mp4")

@module.commands("dblflip")
def dblflip(bot, trigger):
  """Flip two tables...at the same time!"""
  bot.say("┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻")

@module.rule(r".*bite\sme.*")
@module.require_chanmsg
def bitesback(bot, trigger):
  bot.action("bites {}".format(trigger.nick))

@module.rule("^Bye!$")
def byebye(bot, trigger):
  bot.say("https://actionsack.com/img/misc/BYE!.webp")

@module.commands("cb")
def clickbait(bot, trigger):
  """Post clickbait into chat."""
  clickbait = [
    "10 celebrities you didn't know were transgender! #11 will shock you!",
    "Was it an alien or something?! Can't wait to find out!",
    "When you read these 19 shocking food facts, you'll never want to eat again!",
    "Think this is a normal shed? Just wait until you see what's inside...",
    "She puts her toilet brush under the seat. Why? It's genius!",
    "Fifty Shades of Grey: #36 took my breath away!",
    "These scientists **TRIPLED** a Janitors IQ! The result will break your heart.",
    "How freeing an escaped convict turned this little boy into a MILLIONAIRE!",
    "What This Man Learned From Having Sex With 365 Guys In One Year"
  ]
  bot.say(random.choice(clickbait))

@module.rule(".*COVID19!.*")
def windofgod(bot, trigger):
  bot.say("https://actionsack.com/img/videos/windofgod.webm")

@module.rule(".*crossfit.*")
def crossfit(bot, trigger):
  bot.say("https://actionsack.com/img/videos/crossfit.webm")

@module.rule("^dang$")
def dang(bot, trigger):
  bot.say("https://actionsack.com/img/misc/dang.jpg")

@module.commands("dbc")
def dbc(bot, trigger):
  """Post a Dragonbro Chi comic."""
  dbc = [
    "https://actionsack.com/img/dbc/dbc01.png",
    "https://actionsack.com/img/dbc/dbc02.png",
    "https://actionsack.com/img/dbc/dbc03.png",
    "https://actionsack.com/img/dbc/dbc04.png",
    "https://actionsack.com/img/dbc/dbc07.png",
    "https://actionsack.com/img/dbc/dbc08.png",
    "https://actionsack.com/img/dbc/dbc09.png",
    "https://actionsack.com/img/dbc/dbc10.png"
  ]
  bot.say(random.choice(dbc))

@module.rule(r"^Deus\svult!$")
def deusvult(bot, trigger):
  bot.say("https://actionsack.com/img/videos/deusvult.webm")

@module.rule(".*fake!.*")
@module.commands("fake")
def fake(bot, trigger):
  """For when something is super fake.
  Can also be triggered with 'fake!' anywhere in a message."""
  fake = [
    "https://actionsack.com/img/fake/faux.png",
    "https://actionsack.com/img/fake/kazoo.gif"
  ]
  bot.say(random.choice(fake))

@module.rule(".*!erect.*")
@module.commands("erect")
def erect(bot, trigger):
  """Classic Krieger GIF.
  Can also be triggered with '!erect' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/erect.gif")

@module.rule(".*GOAT!.*")
@module.commands("goat")
def goat(bot, trigger):
  """Greatest of all time!
  Can also be triggered with 'GOAT!' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/GOAT.webm")

@module.rule("^hackers$")
@module.commands("hackers")
def hackers(bot, trigger):
  """Summons the world's two greatest hackers.
  Can also be summoned without the preceeding period/full stop."""
  bot.say("https://actionsack.com/img/as/hackers.png")

@module.rule("^hue.*")
def hue(bot, trigger):
  hue = [
    "https://actionsack.com/img/hue/bots.gif",
    "https://actionsack.com/img/hue/bus.gif",
    "https://actionsack.com/img/hue/cat.gif",
    "https://actionsack.com/img/hue/combo.gif",
    "https://actionsack.com/img/hue/drhue.gif",
    "https://actionsack.com/img/hue/drhueves.gif",
    "https://actionsack.com/img/hue/horse.gif",
    "https://actionsack.com/img/hue/huemanatee.gif",
    "https://actionsack.com/img/hue/hueppo.gif",
    "https://actionsack.com/img/hue/jellyfish.gif",
    "https://actionsack.com/img/hue/kitten.gif",
    "https://actionsack.com/img/hue/mike.gif",
    "https://actionsack.com/img/hue/owls.gif",
    "https://actionsack.com/img/hue/sdc.gif"
  ]
  bot.say(random.choice(hue))

@module.rule(r"^I am the machine\.(\s$|$)")
def iamthemachine(bot, trigger):
  bot.say("https://www.youtube.com/watch?v=8PAtFsJY5q0")

@module.rule(r".*I\scan't\seven.*", r".*I'm\sliterally\scan't\seven.*")
def icanteven(bot, trigger):
  bot.say("https://actionsack.com/img/videos/icanteven.webm")

@module.rule(r"^I\sship\s(it|that).*")
def ishipit(bot, trigger):
  bot.say("https://actionsack.com/img/misc/fedex.webp")

@module.rule(".*idgaf.*")
def idgaf(bot, trigger):
  idgaf = [
    "https://actionsack.com/img/idgaf/20thcentury.webp",
    "https://actionsack.com/img/idgaf/nophux.webp"
  ]
  bot.say(random.choice(idgaf))

@module.rule(r".*hugh\smungus.*")
def hughmungus(bot, trigger):
  bot.say("https://actionsack.com/img/videos/hughmungus.webm")

@module.rule(".*IMDABES.*")
def imdabes(bot, trigger):
  bot.say("https://actionsack.com/img/videos/IMDABES.webm")

@module.rule(".*!JPEG.*")
@module.commands("jpeg")
def jpeg(bot, trigger):
  """Do I look like I know what a JPEG is?
  Can also be triggered with '!JPEG' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/JPEG.webm")

@module.rule(".*!kazoo.*")
@module.commands("kazoo")
def kazoo(bot, trigger):
  """Kaaazzzzoooooooooo!!!
  Can also be triggered with '!kazoo' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/kazoo.webm")

@module.rule(r"^kill\sme.*")
def killme(bot, trigger):
  killme = [
    "https://actionsack.com/img/misc/killme-bulb.png",
    "https://actionsack.com/img/misc/killme-char.png",
    "https://actionsack.com/img/misc/killme-pika.png"
  ]
  bot.say(random.choice(killme))

@module.rule(r".*((?<!\w)k(y|m)s(?!\w)|kill\syourself).*")
def kys(bot, trigger):
  kys = [
    "https://actionsack.com/img/kys/deals.png",
    "https://actionsack.com/img/kys/elmo.mp4",
    "https://actionsack.com/img/kys/gta.mp4",
    "https://actionsack.com/img/kys/hang.png",
    "https://actionsack.com/img/kys/howto.png",
    "https://actionsack.com/img/kys/iGuess.png",
    "https://actionsack.com/img/kys/ike.png",
    "https://actionsack.com/img/kys/kys.png",
    "https://actionsack.com/img/kys/mike-pepe.png",
    "https://actionsack.com/img/kys/mike.png",
    "https://actionsack.com/img/kys/music.gif",
    "https://actionsack.com/img/kys/ohhai.gif",
    "https://actionsack.com/img/kys/pasta.png",
    "https://actionsack.com/img/kys/pepe.png",
    "https://actionsack.com/img/kys/peter-joe.mp4",
    "https://actionsack.com/img/kys/peter.mp4",
    "https://actionsack.com/img/kys/puft.mp4",
    "https://actionsack.com/img/kys/tried.png",
    "https://actionsack.com/img/kys/wendys.png",
    "https://actionsack.com/img/kys/window.gif",
    "https://lostallhope.com/"
  ]
  bot.say(random.choice(kys))

@module.rule(".*!music.*")
def listentomusic(bot, trigger):
  bot.say("https://actionsack.com/img/kys/music.gif")

@module.rule(r"^oh\shai.*")
def ohhai(bot, trigger):
  bot.say("https://actionsack.com/img/kys/ohhai.gif")

@module.rule(".*legal!.*")
@module.commands("legal")
def legal(bot, trigger):
  """100% totally legal!
  Can also be triggered with 'legal!' anywhere in a message."""
  legal = [
    "https://actionsack.com/img/misc/👍LEGAL👍.mp4",
    "https://actionsack.com/img/misc/🕺LEGAL🕺.mp4"
  ]
  bot.say(random.choice(legal))

@module.commands("judge")
@module.require_chanmsg
def judge(bot, trigger):
  """Judge someone or something."""
  judges = [
    "not guilty! https://actionsack.com/img/misc/not-guilty.png",
    "guilty! https://actionsack.com/img/misc/guilty.png"
  ]
  text = clean(trigger.group(2) or '')

  if not text:
    try:
      msg = "I need someone or something to judge!"
    except KeyError:
      msg = "How did you do that?!"
    bot.reply(msg)
    return module.NOLIMIT
  bot.say("{} is {}".format(trigger.group(2), random.choice(judges)))

@module.rule(r"^wat($|\W)")
def wat(bot, trigger):
  wat = [
    "https://actionsack.com/img/wat/3wats.webp",
    "https://actionsack.com/img/wat/65wat.webp",
    "https://actionsack.com/img/wat/emma.webp",
    "https://actionsack.com/img/wat/filming.webp",
    "https://actionsack.com/img/wat/gigawat.webp",
    "https://actionsack.com/img/wat/holdwat.webp",
    "https://actionsack.com/img/wat/hwat02.webp",
    "https://actionsack.com/img/wat/inthebutt.webp",
    "https://actionsack.com/img/wat/jabba.webp",
    "https://actionsack.com/img/wat/jaja.webp",
    "https://actionsack.com/img/wat/jjwat.webp",
    "https://actionsack.com/img/wat/konichiwat.webp",
    "https://actionsack.com/img/wat/olde.webp",
    "https://actionsack.com/img/wat/police.webp",
    "https://actionsack.com/img/wat/slipwat.webp",
    "https://actionsack.com/img/wat/space.webp",
    "https://actionsack.com/img/wat/subwat.webp",
    "https://actionsack.com/img/wat/swat.webp",
    "https://actionsack.com/img/wat/watchdogs.webp",
    "https://actionsack.com/img/wat/watduel.webp",
    "https://actionsack.com/img/wat/waterworld.webp",
    "https://actionsack.com/img/wat/wathusky.webp",
    "https://actionsack.com/img/wat/watif.webp",
    "https://actionsack.com/img/wat/watinthehat.webp",
    "https://actionsack.com/img/wat/watislove.webp",
    "https://actionsack.com/img/wat/watmouth.webp",
    "https://actionsack.com/img/wat/wat.webp",
    "https://actionsack.com/img/wat/watshake.webp",
    "https://actionsack.com/img/wat/watwatwatwat.webp",
    "https://actionsack.com/img/wat/wow.webp"
  ]
  bot.say(random.choice(wat))

@module.rule(".*✝.*")
def praisejesus(bot, trigger):
  bot.say("Praise Jesus!")

@module.rule(r".*jesus\schrist.*")
def jesuschrist(bot, trigger):
  bot.say("Praise Him!")

@module.rule(r".*Windows\s10.*")
@module.commands("w10")
def windowsten(bot, trigger):
  """Windows 10 bad.
  Can also be triggered with 'Windows 10' anywhere in a message."""
  w10 = [
    "https://actionsack.com/img/W10/game.png",
    "https://actionsack.com/img/W10/pubg.webm",
    "https://actionsack.com/img/W10/stuck.png",
    "https://actionsack.com/img/W10/updates.webm"
  ]
  bot.say(random.choice(w10))

@module.rule(".*!wizard.*", ".*wazard.*")
@module.commands("wizard")
def wazard(bot, trigger):
  """Hagrid tells you what you are.
  Can also be triggered with '!wizard' or 'wazard' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/wazard.mp4")

@module.rule(".*wow!.*")
@module.commands("wow")
def wow(bot, trigger):
  """Wow! — Can also be triggered with 'wow!' anywhere in a message."""
  wow = [
    "https://actionsack.com/img/wow/corrupt.webp",
    "https://actionsack.com/img/wow/wow!!.mp4",
    "https://actionsack.com/img/wow/wow.webp"
  ]
  bot.say(random.choice(wow))

@module.rule(".*whoa.*")
def whoa(bot, trigger):
  bot.say("https://actionsack.com/img/misc/whoa.webp")

@module.rule(r".*wew\slad.*", ".*wew!.*")
@module.commands("wew")
def wew(bot, trigger):
  """wew lad! — Can also be triggered with 'wew!' or 'wew lad' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/wew.webp")

@module.rule(r"^(uh\.\.\.|uh{2,})$")
def uhh(bot, trigger):
  uhh = [
    "https://actionsack.com/img/uh/uh01.webp",
    "https://actionsack.com/img/uh/uh02.webp",
    "https://actionsack.com/img/uh/uh03.webp",
    "https://actionsack.com/img/uh/uh04.webp",
    "https://actionsack.com/img/uh/uhbytes.webp"
  ]
  bot.say(random.choice(uhh))

@module.rule(".*!!twerk.*")
def twerk(bot, trigger):
  twerkit = [
    "https://actionsack.com/img/twerk/ash.gif",
    "https://actionsack.com/img/twerk/nose.gif"
  ]
  bot.say(random.choice(twerkit))

@module.rule(r".*swiggity\sswooty.*")
def swiggityswooty(bot, trigger):
  swiggity = [
    "https://actionsack.com/img/swiggityswooty/birb.gif",
    "https://actionsack.com/img/swiggityswooty/fatman.gif"
  ]
  bot.say(random.choice(swiggity))

@module.rule(r".*praise\sthe\ssun.*")
@module.commands("praise")
def praisethesun(bot, trigger):
  """Praise the Sun!
  Can also be triggered with 'praise the sun' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/praisethesun.webm")

@module.rule(".*#spam.*")
def spam(bot, trigger):
  bot.say("https://actionsack.com/img/misc/spam.png")

@module.rule(".*!son.*")
@module.commands("son")
def son(bot, trigger):
  """Posts a "don't talk to me or my son" meme/image.
  Can also be triggered with "!son" anywhere in a message."""
  son = [
    "https://actionsack.com/img/son/acnh.webp",
    "https://actionsack.com/img/son/chiefs.webp",
    "https://actionsack.com/img/son/doggos.webp",
    "https://actionsack.com/img/son/halo.webp",
    "https://actionsack.com/img/son/subs.webp",
    "https://actionsack.com/img/son/teslas.webp",
    "https://actionsack.com/img/son/wieners.webp"
  ]
  bot.say(random.choice(son))

@module.rule("^sh{2,}$")
def shh(bot, trigger):
  shhh = [
    "https://actionsack.com/img/shh/clouds.jpg",
    "https://actionsack.com/img/shh/eardrums.mp4",
    "https://actionsack.com/img/shh/ninjagaiden.png",
    "https://actionsack.com/img/shh/stfub.mp4",
    "https://actionsack.com/img/shh/tlou.jpg"
  ]
  bot.say(random.choice(shhh))

@module.rule(r".*sex\srobot.*")
def sexrobot(bot, trigger):
  bot.say("https://actionsack.com/img/misc/sexrobot.gif")

@module.rule(".*!stickers.*")
@module.commands("stickers")
def stickers(bot, trigger):
  """Well-known fact: each sticker on your car adds 5 horsepower.
  Can also be triggered with '!stickers' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/stickers.gif")

@module.commands("shaved")
def shaved(bot, trigger):
  """xnaas' beautiful shaved leg circa 2011."""
  bot.say("https://actionsack.com/img/xnaas/shaved.webp")

@module.rule(".*!rimshot.*")
@module.commands("rimshot")
def rimshot(bot, trigger):
  """Replies with a 'rimshot' GIF.
  Can also be triggered with '!rimshot' anywhere in a message."""
  rim_shot = [
    "https://actionsack.com/img/rimshot/effects.gif",
    "https://actionsack.com/img/rimshot/fgr.gif",
    "https://actionsack.com/img/rimshot/mlp.gif",
    "https://actionsack.com/img/rimshot/rimshot.gif"
  ]
  bot.say(random.choice(rim_shot))

@module.rule(".*!newhouse.*")
@module.commands("newhouse")
def newhouse(bot, trigger):
  """Can also be triggered with '!newhouse' anywhere in a message."""
  bot.say("https://actionsack.com/img/fecktk/newhouse.webp")

@module.rule(".*!drone.*")
@module.commands("drone")
def drone(bot, trigger):
  """Summons a drone into chat.
  Can also be summoned with '!drone' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/drone.webm")

@module.rule(".*!cage.*")
@module.commands("cage")
def nickcage(bot, trigger):
  """Summons Nicolas Cage into chat.
  Can also be summoned with '!cage' anywhere in a message."""
  nick_cage = [
    "https://actionsack.com/img/cage/scream.webp",
    "https://actionsack.com/img/cage/side-to-side.webp",
    "https://actionsack.com/img/cage/wink.webp"
  ]
  bot.say(random.choice(nick_cage))

@module.rule(".*!va.*")
@module.commands("va")
@module.rate(user=900)
def voiceactor(bot, trigger):
  """Quote (or pic!) of a #RealVoiceActor.
  Can only be triggered once per 15 minutes per user.
  Can also be triggered with '!va' anywhere in a message."""
  voice_actor = [
    "You are a pathetic worm... Fight for your scraps... Take your pics haha. I am a true artist and someone that crushes vermin like you in my path. You are a fake and a child with no comprehension of skill nor talent. You are weak... Just like so many... I am pleasure to work with... Unless you cross me or treat me like dirt... Then you will feel my fury... You should have been nice... Now you pay... I am not a pushover... haha... I can make your soul cry and beg for mercy... I am tired of you jerks... I will fight back... Every time...",
    "Give me a break! You guys think you have some freaking special talent that deserves all this damn nonrecognition?! You guys want to get paid to sell and just SPEAK these god damn advertisements! I hate that side of this business! Real voice ACTING is art, it is all the animation and film, it is video games!",
    "It is now a flooded market with all these people who do not have any idea what TRUE ACTING/TALENT is!!! Go do your commercial selling adverts... You can have them... You and your boring ass advertisements are not what makes great voice acting! The true pros are chameleons that shift into new voices and attitudes. You think you can attack me and not feel my sting back!? ACTORS are like gods! We have to convey a true sense of identity.",
    "A real actor has to change emotions and have skills to modulate/shift the voice as elegantly as singers do... I have a large 3 octave vocal range... I also have pitch and tone control too. I worked for it...",
    "Haha, I guess you are right... I HATE doing commercials... I fucking hate them... I rather be able to do 100+ animation and game characters then sell damn cars and products any day... Keep your stupid adverts promos and spots... Seeing how many of you fight over them is sad... I have real talent. Fighting for the scraps of a radio commercial is pathetic.",
    "Now I see why Troy Baker is so arrogant too... You types bring it out in the people with REAL talent. Having the rarest vocal chords, a 3 octave singing range and a good tone is WHAT makes someone good at voice acting... Practicing and having the gift of tricking people into thinking you ARE the character... It takes Range, control, tones, colors, emotions... You have no idea how much YOU lack compared to those such as I...",
    "Maybe the business itself is just stupid now... Keep your stupid 30 secs of voice demo reels... THEY SHOW NOTHING... If you people could really act and convey deep emotions... You would show those off... I know you would.. I also know you would show off all your voices if you had them... Not many can do 100+ variations of characters and tones/pitches/etc...I will stick with my unique approaches... You can all copy each other... Eventually the agents will seek NEW talent with something special and different. you can keep your 30sec-1min demo reels too... I will be the maverick and lead the innovation people like you fail to respect...I rather show some meat on the steak I am selling... keep your 5-6 goofy cartoon voices that EVERYONE does identical and copies! I will keep my rich and detailed characters that are superior. Your attacks did nothing to me... Heh... Your words only gave me strength to carry on... The right agents will see my talents and my determinations... As well as my self-respect/pride... Then they will reap the rewards while you and your kind fight for scraps...",
    "This industry used to filter out those that just wanted an easy job where they spoke and got paid for little to nothing special other than talking... Now its a mess... I challenge anyone to do as many character voices as me... My determination is nothing short of a amazing... By the way... I have no upper teeth either... No denture... Nothing on top to speak as you can so easily... My road is hard but I relish in it's challenge! Yet, the fates can not stop me... I learned to speak almost 99% as good as you all regardless... I cannot be stopped. So... I really have better things to do now, like revel in my craft.",
    "I am pleasure to work with... Unless you cross me or treat me like dirt... Then you will feel my fury... You should have been nice... Now you pay... I am not a pushover... haha... I can make your soul cry and beg for mercy... I am tired of you jerks... I will fight back... Every time... Give me a break! You guys think you have some freaking special talent that deserves all this damn nonrecognition?! You guys want to get paid to sell and just SPEAK these god damn advertisements! I hate that side of this business! Real voice ACTING is art, it is all the animation and film, it is video games!",
    "Yes. I take singing seriously... I used to tonedeaf and have slaved over the oven of dedication for 7 years.",
    "Damn... Why can't people just communicate without being dicks?! This happened before and then I had to unleash all my force upon that stupid fool too! I will not let people talk down to me. Those days are... gone...",
    "I have blonde hair and blue eyes... I was born November 18... Char was born November 17... Has blonde hair... Blue eyes... So... Yes... Char Aznable is my hero... That is not real... Freaking humans are nothing like the citizens of Zeon...",
    "I have nothing to hide. I am not afraid of being naked... Do you think I care what you think of me... I say what I want and I am the person... I am... I could care less what people think of me... I know I have talent and the attacks and doubts people throw my way are just lies and inabilities to see my greatness...",
    "Thank you... This is a nice comment... Maybe these stupid insects and take notes and learn what real hospitality is!?",
    "I am sick of attackers and now I fight back... Years and years I was quiet... Not... This... Time... I am so sick of people that are LESS than human! Just be fucking nice and I wont bring out my soulcrusher! Is that too much to ask?! I feel like I am in some stupid episode of PUNKED!",
    "My animation reel is good. You cannot fool me... You cannot weaken my defenses here... I acted those characters all on the fly and made up the scripts on the fly too... I think they are exceptional... Imagine when I actually TRY to make the proper reels... Why must I keep explaining myself to you narrow minded fools?! I can be such a wonderful and charming man... Yet, now you have made me into the dragon!",
    "https://actionsack.com/img/misc/'voiceactor'.png"
  ]
  bot.say(random.choice(voice_actor), max_messages=3)

@module.rule(".*!baby.*")
@module.commands("baby")
def baby(bot, trigger):
  """Posts an image of GIF involving babies.
  WARNING: not a cutesy command.
  Can also be triggered with '!baby' anywhere in a message."""
  baby_pics = [
    "https://actionsack.com/img/baby/inflammable.gif",
    "https://actionsack.com/img/baby/man.png",
    "https://actionsack.com/img/baby/prayfor.png",
    "https://actionsack.com/img/baby/rolling.gif",
    "https://actionsack.com/img/baby/spider.gif"
  ]
  bot.say(random.choice(baby_pics))

@module.rule(".*boom!.*")
@module.commands("boom")
def boom(bot, trigger):
  """BOOM! — Can also be triggered with 'boom!' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/boom.webp")

@module.rule(".*burn!.*")
def burn(bot, trigger):
  bot.say("https://w.wiki/n9f")

@module.rule(".*bustin'.*")
@module.commands("bustin")
def bustin(bot, trigger):
  """Bustin' makes me feel good!
  Can also be triggered with "bustin'" anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/bustin.webm")

@module.rule(r".*(?<!s)canned(?!\sair).*")
def canned(bot, trigger):
  bot.say("https://actionsack.com/img/misc/canned.gif")

@module.rule(r".*consider(\s|ed\s)this.*")
def consider(bot, trigger):
  bot.say("https://actionsack.com/img/misc/consider.webp")

@module.rule(".*congraturaisins.*")
def congraturaisins(bot, trigger):
  bot.say("https://actionsack.com/img/misc/congraturaisins.png")

@module.rule(".*cowabunga.*")
def cowabunga(bot, trigger):
  bot.say("https://actionsack.com/img/misc/cowabunga.png")

@module.rule(".*correct!.*")
def correcthorse(bot, trigger):
  bot.say("https://actionsack.com/img/misc/correct!.gif")

@module.rule(".*centaur.*")
def centaur(bot, trigger):
  bot.say("https://actionsack.com/img/misc/centaur.png")

@module.rule(".*(!dance|dance!).*")
@module.commands("dance")
def dance(bot, trigger):
  """Posts a dancing GIF.
  Can also be triggered with 'dance!' or '!dance' anywhere in a message."""
  dance_gifs = [
    "https://actionsack.com/img/dance/arms.gif",
    "https://actionsack.com/img/dance/arthur.gif",
    "https://actionsack.com/img/dance/bunny.gif",
    "https://actionsack.com/img/dance/frankie.gif",
    "https://actionsack.com/img/dance/gijoe.gif",
    "https://actionsack.com/img/dance/guy.gif",
    "https://actionsack.com/img/dance/jontron.gif",
    "https://actionsack.com/img/dance/skeleton.gif"
  ]
  bot.say(random.choice(dance_gifs))

@module.commands("doomanimal")
def doomanimal(bot, trigger):
  """Posts "DOOMANIMAL" video by @andmish."""
  bot.say("https://actionsack.com/img/videos/DOOMANIMAL.webm")

@module.commands("doomcrossing")
def doomcrossing(bot, trigger):
  """Posts "DOOM CROSSING: Eternal Horizons" by The Chalkeaters feat. Natalia Natchan."""
  bot.say("https://actionsack.com/img/videos/DOOMCROSSING.webm")

@module.rule(r".*doom\sguy.*")
def doomguy(bot, trigger):
  bot.say("https://actionsack.com/img/misc/doomguy.webp")

@module.rule(".*grapist.*")
def grapist(bot, trigger):
  bot.say("https://actionsack.com/img/misc/grapist.gif")

@module.rule(r".*it\swas\sme(?!ant).*")
def itwasme(bot, trigger):
  me_dio = [
    "https://actionsack.com/img/dio/dva.png",
    "https://actionsack.com/img/dio/sombra.png",
    "https://actionsack.com/img/dio/trumpva.gif"
  ]
  bot.say(random.choice(me_dio))

@module.rule(r"^god\sbless\s(.*)")
def godbless(bot, trigger):
  bot.action("blesses {}".format(trigger.group(1)))

@module.rule(r".*hail\ssatan!.*")
def hailsatan(bot, trigger):
  hail_satan = [
    "https://actionsack.com/img/satan/mii.webm",
    "https://actionsack.com/img/satan/pooh.mp4"
  ]
  bot.say(random.choice(hail_satan))

@module.rule(r".*have\sa\sseat.*")
def haveaseat(bot, trigger):
  bot.say("https://actionsack.com/img/misc/haveaseat.gif")

@module.rule(".*(jews|✡️|✡).*")
def jews(bot, trigger):
  jew_pics = [
    "https://actionsack.com/img/jews/blame.webp",
    "https://actionsack.com/img/jews/donate.webp"
  ]
  bot.say(random.choice(jew_pics))

@module.rule("^k$")
def kay(bot, trigger):
  kk = [
    "k",
    "👌",
    "👌🏻",
    "👌🏼",
    "👌🏽",
    "👌🏾",
    "👌🏿",
    "👌🏻👌🏼👌🏽👌🏾👌🏿",
    "🆗",
    "https://actionsack.com/img/k/kermit.mp4",
    "https://actionsack.com/img/k/seuss.mp4",
    "https://actionsack.com/img/k/shirt.mp4",
    "https://actionsack.com/img/k/snow.mp4",
    "https://actionsack.com/img/k/VHS.mp4",
    "https://actionsack.com/img/k/vldlk.gif"
  ]
  bot.say(random.choice(kk))

@module.rule(".*!words.*")
def words(bot, trigger):
  # Requested by Aegisfate on 2020-11-19
  bot.say("https://actionsack.com/img/misc/words.webp")

@module.rule(".*kiki.*")
def kiki(bot, trigger):
  kiki = [
    "https://actionsack.com/img/kiki/sauce.png",
    "https://actionsack.com/img/kiki/snoop.png",
    formatting.monospace('[4:44 PM] Kiki: U sound so far right now'),
    "I S M A E L  C H I A  T O R R E S"
  ]
  bot.say(random.choice(kiki))

@module.rule(r".*major\sspoiler.*")
def majorspoiler(bot, trigger):
  bot.say("https://actionsack.com/img/misc/spoiler.png")

@module.rule(".*!navy.*")
@module.commands("navy")
@module.rate(server=21600)
def navyseal(bot, trigger):
  """Posts the infamous Navy Seal copypasta...or you get a cat GIF/MP4 version.
  Server-wide rate limit of once per 6 hours.
  Can also be triggered with '!navy' anywhere in a message."""
  navy_seal = [
    "https://actionsack.com/img/misc/navyseal.mp4",
    "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little ''clever'' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
  ]
  bot.say(random.choice(navy_seal), max_messages=4)

@module.rule(".*racist.*")
def racist(bot, trigger):
  racists = [
    "https://actionsack.com/img/racist/birds.gif",
    "https://actionsack.com/img/racist/blackmexican.gif",
    "https://actionsack.com/img/racist/fall.gif",
    "https://actionsack.com/img/racist/nelson.gif",
    "https://actionsack.com/img/racist/prettyracist.mp4",
    "https://actionsack.com/img/racist/racist.mp4",
    "https://actionsack.com/img/racist/shake.gif",
    "https://actionsack.com/img/racist/wash.png"
  ]
  bot.say(random.choice(racists))

@module.rule(".*niggers.*")
def niggers(bot, trigger):
  niggers = [
    "https://actionsack.com/img/racist/nig/cana.png",
    "https://actionsack.com/img/racist/nig/kan.png",
    "https://actionsack.com/img/racist/nig/kristen.png",
    "https://actionsack.com/img/racist/nig/naggers.gif",
    "https://actionsack.com/img/racist/nig/welfare.png"
  ]
  if trigger.is_privmsg or trigger.sender == "#nsfw":
    bot.say(random.choice(niggers))

@module.rule(r".*pasta\sdisasta.*")
def pastadisasta(bot, trigger):
  bot.say("https://actionsack.com/img/🍝/disasta.webm")

@module.rule(r".*(?<!his)panic!.*")
def panic(bot, trigger):
  panic_room = [
    "https://actionsack.com/img/panic/00.webp",
    "https://actionsack.com/img/panic/01.webp",
    "https://actionsack.com/img/panic/02.webp",
    "https://actionsack.com/img/panic/03.webp",
    "https://actionsack.com/img/panic/04.webp",
    "https://actionsack.com/img/panic/05.webp",
    "https://actionsack.com/img/panic/06.webp"
  ]
  bot.say(random.choice(panic_room))

@module.rule(r".*my\sbrand.*")
def mybrand(bot, trigger):
  bot.say("https://actionsack.com/img/videos/MY_BRAND!.webm")

@module.rule(".*!nms.*")
def nms(bot, trigger):
  no_mans_sky = [
    "https://actionsack.com/img/nms/ice.png",
    "https://actionsack.com/img/nms/legit.gif",
    "https://actionsack.com/img/nms/mike.png"
  ]
  bot.say(random.choice(no_mans_sky))

@module.rule(r"^(nice|sick)\sgif.*")
def sickgif(bot, trigger):
  bot.say("https://actionsack.com/img/misc/sickgif.gif")

@module.rule("^nerd!$")
def nerd(bot, trigger):
  bot.say("https://actionsack.com/img/misc/nerd!.gif")

@module.rule(".*neat!.*")
def neat(bot, trigger):
  neat = [
    "https://actionsack.com/img/neat/anime.gif",
    "https://actionsack.com/img/neat/bender01.gif",
    "https://actionsack.com/img/neat/bender02.gif",
    "https://actionsack.com/img/neat/bender03.gif",
    "https://actionsack.com/img/neat/ffcat.png",
    "https://actionsack.com/img/neat/neat.mp4",
    "https://actionsack.com/img/neat/spiderman.gif",
    "https://actionsack.com/img/neat/stare.gif"
  ]
  bot.say(random.choice(neat))

@module.require_admin
@module.rule(r".*my\sserver.*")
def myserver(bot, trigger):
  my_server = [
    "https://actionsack.com/img/server/irl.jpg",
    "https://actionsack.com/img/server/weekend.png"
  ]
  bot.say(random.choice(my_server))

@module.rule(r".*(?<!\w)moist(?!\w).*")
def moist(bot, trigger):
  moist = [
    "https://actionsack.com/img/moist/asian.jpg",
    "https://actionsack.com/img/moist/old.jpg"
  ]
  bot.say(random.choice(moist))

@module.rule(".*!manga.*")
@module.commands("manga")
def manga(bot, trigger):
  """Posts a clip from the BowserVids "What's in the bag?" video.
  Can also be triggered with '!manga' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/manga.mp4")

@module.rule(r".*let\sme\sin.*")
def letmein(bot, trigger):
  bot.say("https://actionsack.com/img/videos/letmein.mp4")

@module.rule(r".*i\smade\sthis.*")
def imadethis(bot, trigger):
  iMadeThis = [
    "https://actionsack.com/img/OC/apple.png",
    "https://actionsack.com/img/OC/comic.png",
    "https://actionsack.com/img/OC/iGIF.gif",
    "https://actionsack.com/img/OC/iGIF2.gif",
    "https://actionsack.com/img/OC/iPickle.png",
    "https://actionsack.com/img/OC/starwars.png"
  ]
  bot.say(random.choice(iMadeThis))

@module.rule(r".*(?<!\w)eat\sshit.*")
def frank(bot, trigger):
  bot.say("https://actionsack.com/img/misc/frank.gif")

@module.rule(".*GTFO.*")
def gtfo(bot, trigger):
  bot.say("https://actionsack.com/img/misc/gtfo.png")

@module.rule(".*hawt.*")
def hawt(bot, trigger):
  bot.say("🥵")

@module.rule("^hwat.*")
def hwat(bot, trigger):
  hwat = [
    "https://actionsack.com/img/wat/hwat01.webp",
    "https://actionsack.com/img/wat/hwat02.webp"
  ]
  bot.say(random.choice(hwat))

@module.rule(r".*I\ssee\syou(?!\').*")
def iseeyou(bot, trigger):
  bot.say("https://actionsack.com/img/👀/iSeeU.mp4")

@module.rule(".*eyelids.*")
def eyelids(bot, trigger):
  bot.say("https://actionsack.com/img/👀/eyelids.mp4")

@module.rule(".*👀.*")
def eyes(bot, trigger):
  eyes = [
    "https://actionsack.com/img/👀/anime.png",
    "https://actionsack.com/img/👀/big01.png",
    "https://actionsack.com/img/👀/big02.png",
    "https://actionsack.com/img/👀/big03.png",
    "https://actionsack.com/img/👀/big04.png",
    "https://actionsack.com/img/👀/big05.png",
    "https://actionsack.com/img/👀/big06.png",
    "https://actionsack.com/img/👀/big07.png",
    "https://actionsack.com/img/👀/big08.png",
    "https://actionsack.com/img/👀/bigred.png",
    "https://actionsack.com/img/👀/deadpool.gif",
    "https://actionsack.com/img/👀/eric01.png",
    "https://actionsack.com/img/👀/eric02.png",
    "https://actionsack.com/img/👀/eyelids.mp4",
    "https://actionsack.com/img/👀/fecktk.png",
    "https://actionsack.com/img/👀/iSeeU.mp4",
    "https://actionsack.com/img/👀/monkey.png",
    "https://actionsack.com/img/👀/obama.png",
    "https://actionsack.com/img/👀/trump.png",
    "https://actionsack.com/img/👀/walrus.png",
    "https://actionsack.com/img/👀/woody.png"
  ]
  bot.say(random.choice(eyes))

@module.rule(r"^💩(|\s)💩$")
def shit(bot, trigger):
  shit_gifs = [
    "https://actionsack.com/img/💩/cardi.mp4",
    "https://actionsack.com/img/💩/extreme.mp4",
    "https://actionsack.com/img/💩/McCafé.gif",
    "https://actionsack.com/img/💩/🚽.gif"
  ]
  bot.say(random.choice(shit_gifs))

@module.rule(".*!tesla.*")
@module.commands("tesla")
def tesla(bot, trigger):
  """Can also be triggered with '!tesla' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/tesla.webm")

@module.rule(".*!vn.*")
@module.commands("vn")
def vapenaysh(bot, trigger):
  """Vape naysh, y'all!
  Can also be triggered with '!vn' anywhere in a message."""
  vape_naysh = [
    "https://actionsack.com/img/vn/20.png",
    "https://actionsack.com/img/vn/2fast.png",
    "https://actionsack.com/img/vn/5minutes.png",
    "https://actionsack.com/img/vn/anal.png",
    "https://actionsack.com/img/vn/area.png",
    "https://actionsack.com/img/vn/arrest.webm",
    "https://actionsack.com/img/vn/bart.gif",
    "https://actionsack.com/img/vn/bart.webm",
    "https://actionsack.com/img/vn/beanie.png",
    "https://actionsack.com/img/vn/breakingbad.png",
    "https://actionsack.com/img/vn/bubble.mp4",
    "https://actionsack.com/img/vn/burns.gif",
    "https://actionsack.com/img/vn/charged.png",
    "https://actionsack.com/img/vn/C&H.gif",
    "https://actionsack.com/img/vn/coconut.png",
    "https://actionsack.com/img/vn/dora.png",
    "https://actionsack.com/img/vn/faceswap.gif",
    "https://actionsack.com/img/vn/fancy-ethan.png",
    "https://actionsack.com/img/vn/first.png",
    "https://actionsack.com/img/vn/flappy.gif",
    "https://actionsack.com/img/vn/gaysex.png",
    "https://actionsack.com/img/vn/godzilla.gif",
    "https://actionsack.com/img/vn/goldengate.png",
    "https://actionsack.com/img/vn/h3h3.png",
    "https://actionsack.com/img/vn/iRape.png",
    "https://actionsack.com/img/vn/it.png",
    "https://actionsack.com/img/vn/iVape.png",
    "https://actionsack.com/img/vn/legend.png",
    "https://actionsack.com/img/vn/LOV.png",
    "https://actionsack.com/img/vn/lungs.gif",
    "https://actionsack.com/img/vn/mei.gif",
    "https://actionsack.com/img/vn/minecraft.png",
    "https://actionsack.com/img/vn/mountvapemore.png",
    "https://actionsack.com/img/vn/mowing.webm",
    "https://actionsack.com/img/vn/party.png",
    "https://actionsack.com/img/vn/passcode.png",
    "https://actionsack.com/img/vn/pc.mp4",
    "https://actionsack.com/img/vn/pepe.png",
    "https://actionsack.com/img/vn/phatcash.png",
    "https://actionsack.com/img/vn/phatclouds.mp4",
    "https://actionsack.com/img/vn/☂.png",
    "https://actionsack.com/img/vn/server.mp4",
    "https://actionsack.com/img/vn/skills.gif",
    "https://actionsack.com/img/vn/skull.png",
    "https://actionsack.com/img/vn/space-smile.png",
    "https://actionsack.com/img/vn/sphynx.png",
    "https://actionsack.com/img/vn/spongebob.png",
    "https://actionsack.com/img/vn/stock_vape.png",
    "https://actionsack.com/img/vn/tornado-ethan.png",
    "https://actionsack.com/img/vn/tornado.png",
    "https://actionsack.com/img/vn/tower.png",
    "https://actionsack.com/img/vn/twintowers.png",
    "https://actionsack.com/img/vn/vapecat.gif",
    "https://actionsack.com/img/vn/vapecat.mp4",
    "https://actionsack.com/img/vn/vapecat.png",
    "https://actionsack.com/img/vn/vapeman.mp4",
    "https://actionsack.com/img/vn/vnkit.png",
    "https://actionsack.com/img/vn/wedding.png",
    "https://actionsack.com/img/vn/whale.png",
    "https://actionsack.com/img/vn/woodwork.png",
    "https://actionsack.com/img/vn/wut.png"
  ]
  bot.say(random.choice(vape_naysh))

@module.rule(".*🦈.*")
def sharku(bot, trigger):
  sharks = [
    "https://actionsack.com/img/🦈/TV.webp",
    "https://actionsack.com/img/🦈/bed.webp",
    "https://actionsack.com/img/🦈/bleps_irl.webp",
    "https://actionsack.com/img/🦈/borking.webp",
    "https://actionsack.com/img/🦈/buff_girl.webp",
    "https://actionsack.com/img/🦈/comic.webp",
    "https://actionsack.com/img/🦈/costume.webp",
    "https://actionsack.com/img/🦈/cuddles.webp",
    "https://actionsack.com/img/🦈/drawing.webp",
    "https://actionsack.com/img/🦈/flame.webp",
    "https://actionsack.com/img/🦈/food_bowl.webp",
    "https://actionsack.com/img/🦈/leash.webp",
    "https://actionsack.com/img/🦈/pet.webp"
  ]
  bot.say(random.choice(sharks))

@module.rule(r".*🦇(|\s)👨.*")
@module.commands("batman")
def batman(bot, trigger):
  """Summons a Batman. Names are base64 encoded.
  Can also be triggered by sending a message that is only the "🦇👨" emoji."""
  bat_men = [
    "https://actionsack.com/img/🦇👨/amFqYWJybzE=.webp",
    "https://actionsack.com/img/🦇👨/beer.webp",
    "https://actionsack.com/img/🦇👨/bWlrZQ==.webp",
    "https://actionsack.com/img/🦇👨/dGFzaWFu.webp",
    "https://actionsack.com/img/🦇👨/eG5hYXM=.webp",
    "https://actionsack.com/img/🦇👨/ZmVja3Rr.webp",
    "https://actionsack.com/img/🦇👨/ZmVlaw==.webp"
  ]
  bot.say(random.choice(bat_men))

@module.rule(".*🤔{3,}.*")
def think(bot, trigger):
  thinking = [
    "https://actionsack.com/img/think/aesthetic.webp",
    "https://actionsack.com/img/think/agon.webp",
    "https://actionsack.com/img/think/barometer.webp",
    "https://actionsack.com/img/think/beer.webp",
    "https://actionsack.com/img/think/circle.webp",
    "https://actionsack.com/img/think/e.webp",
    "https://actionsack.com/img/think/fu.webp",
    "https://actionsack.com/img/think/layers.webp",
    "https://actionsack.com/img/think/something.webp",
    "https://actionsack.com/img/think/spin.webp",
    "https://actionsack.com/img/think/spinner.webp",
    "https://actionsack.com/img/think/statue.webp",
    "https://actionsack.com/img/think/thonk.webp"
  ]
  bot.say(random.choice(thinking))

@module.rule(".*🚸.*")
def as_linus(bot, trigger):
  bot.say("https://actionsack.com/img/as/linus.png")

@module.rule(".*🚬.*")
def smoking(bot, trigger):
  bot.say("https://actionsack.com/img/misc/smoking.webp")

@module.rule(".*🚁.*")
def heli(bot, trigger):
  helicopter = [
    "https://actionsack.com/img/🚁/engineer.webp",
    "https://actionsack.com/img/🚁/fgr.webp",
    "https://actionsack.com/img/🚁/hair.webp",
    "https://actionsack.com/img/🚁/peewee.webp"
  ]
  bot.say(random.choice(helicopter))

@module.rule(".*🍝.*")
def spaghetti(bot, trigger):
  spaghettis = [
    "https://actionsack.com/img/🍝/21pilots.webm",
    "https://actionsack.com/img/🍝/allstar.webm",
    "https://actionsack.com/img/🍝/disasta.webm",
    "https://actionsack.com/img/🍝/double.png",
    "https://actionsack.com/img/🍝/lie.webm",
    "https://actionsack.com/img/🍝/mom's.webm"
  ]
  bot.say(random.choice(spaghettis))

@module.rule(".*svehla.*")
def svehla(bot, trigger):
  bot.say("https://actionsack.com/img/misc/svehla.webp")

@module.rule(".*🗑.*")
def trash(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🗑.webp")

@module.rule(".*!cumcan.*")
@module.commands("cumcan")
def cumcan(bot, trigger):
  """Cum cleanup.
  Can also be triggered with '!cumcan' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/cumcan.webp")

@module.rule(".*!cancer.*")
@module.commands("cancer")
def cancer(bot, trigger):
  """Warning! Posts pure cancer into chat.
  Can also be triggered with '!cancer' anywhere in a message."""
  cancer_images = [
    "https://actionsack.com/img/as/cancer-list.png",
    "https://actionsack.com/img/as/cancer-microscope.png"
  ]
  bot.say(random.choice(cancer_images))

@module.rule(".*!daquan.*")
@module.commands("daquan")
def daquan(bot, trigger):
  """Can also be triggered with '!daquan' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/daquan.jpg")

@module.rule(".*!heff.*")
@module.commands("heff")
def heff(bot, trigger):
  """Is only game, why you heff to be mad?
  Can also be triggered with '!heff' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/heff.webm")

@module.rule(".*!salty.*")
@module.commands("salty")
def salty(bot, trigger):
  """Can also be triggered with '!salty' anywhere in a message."""
  salty = [
    "https://actionsack.com/img/salt/#staysalty.png",
    "https://actionsack.com/img/salt/all-these-flavors.png",
    "https://actionsack.com/img/salt/dance.webp",
    "https://actionsack.com/img/salt/power-salt.gif",
    "https://actionsack.com/img/salt/salty-bitch.png",
    "https://actionsack.com/img/salt/super-salty.png"
  ]
  bot.say(random.choice(salty))

@module.rule(r".*\[laughs\].*")
def laughs(bot, trigger):
  bot.say("https://actionsack.com/img/misc/laughs.jpg")

@module.rule(r".*\[raughs\].*")
def raughs(bot, trigger):
  bot.say("https://actionsack.com/img/tasian/raughs.webp")

# Action Sack People Section
@module.rule(".*!asak.*")
@module.commands("asak")
def asak(bot, trigger):
  """Posts an Action Sack meme.
  Can also be triggered with '!asak' anywhere in a message."""
  asak = [
    "https://actionsack.com/img/as/AG.gif",
    "https://actionsack.com/img/as/aids-convo.png",
    "https://actionsack.com/img/as/beej.gif",
    "https://actionsack.com/img/as/brokeback.png",
    "https://actionsack.com/img/as/bus-stop.png",
    "https://actionsack.com/img/as/cancer-list.png",
    "https://actionsack.com/img/as/cancer-microscope.png",
    "https://actionsack.com/img/as/copy.png",
    "https://actionsack.com/img/as/dirty-jaja.png",
    "https://actionsack.com/img/as/family-fart.png",
    "https://actionsack.com/img/as/family-gun.gif",
    "https://actionsack.com/img/as/fecktk-eyes-mike.png",
    "https://actionsack.com/img/as/gangster.png",
    "https://actionsack.com/img/as/gay-shit.png",
    "https://actionsack.com/img/as/hackers.png",
    "https://actionsack.com/img/as/hand.gif",
    "https://actionsack.com/img/as/iQuit.png",
    "https://actionsack.com/img/as/kys-mike.png",
    "https://actionsack.com/img/as/kys-or-smd.png",
    "https://actionsack.com/img/as/linus.png",
    "https://actionsack.com/img/as/mikeybikey.png",
    "https://actionsack.com/img/as/mugshot.png",
    "https://actionsack.com/img/as/pumpkin.png",
    "https://actionsack.com/img/as/reflection.png",
    "https://actionsack.com/img/as/snapchat.png",
    "https://actionsack.com/img/as/soup.png"
  ]
  bot.say(random.choice(asak))

@module.rule(".*!bytes.*")
@module.commands("bytes")
def ComputersByte(bot, trigger):
  """Posts a ComputersByte meme.
  Can also be triggered with '!bytes' anywhere in a message."""
  computers_byte = [
    "https://actionsack.com/img/bytes/april.png",
    "https://actionsack.com/img/bytes/bj.png",
    "https://actionsack.com/img/bytes/bytes.gif",
    "https://actionsack.com/img/bytes/bytes01.png",
    "https://actionsack.com/img/bytes/cursor.png",
    "https://actionsack.com/img/bytes/hatched.png",
    "https://actionsack.com/img/bytes/syrup.png"
  ]
  bot.say(random.choice(computers_byte))

@module.rule(".*!fecktk.*")
@module.commands("fecktk")
@module.rate(user=900)
def fecktk(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  fecktks = [
    "https://actionsack.com/img/fecktk/ascii.webp",
    "https://actionsack.com/img/fecktk/baclol.webp",
    "https://actionsack.com/img/fecktk/bacon.webp",
    "https://actionsack.com/img/fecktk/blowie.webp",
    "https://actionsack.com/img/fecktk/elif.webp",
    "https://actionsack.com/img/fecktk/empty.webp",
    "https://actionsack.com/img/fecktk/eyes.webp",
    "https://actionsack.com/img/fecktk/fecktk01.webp",
    "https://actionsack.com/img/fecktk/fecktk02.webp",
    "https://actionsack.com/img/fecktk/fecktk03.webp",
    "https://actionsack.com/img/fecktk/fecktk04.webp",
    "https://actionsack.com/img/fecktk/fecktk05.webp",
    "https://actionsack.com/img/fecktk/fecktk06.webp",
    "https://actionsack.com/img/fecktk/fecktk07.webp",
    "https://actionsack.com/img/fecktk/fecktk08.webp",
    "https://actionsack.com/img/fecktk/fecktk09.webp",
    "https://actionsack.com/img/fecktk/fecktk10.webp",
    "https://actionsack.com/img/fecktk/fecktk11.webp",
    "https://actionsack.com/img/fecktk/fecktk12.webp",
    "https://actionsack.com/img/fecktk/fecktk13.webp",
    "https://actionsack.com/img/fecktk/fecktk14.webp",
    "https://actionsack.com/img/fecktk/fecktk15.webp",
    "https://actionsack.com/img/fecktk/fecktk16.webp",
    "https://actionsack.com/img/fecktk/fecktk17.webp",
    "https://actionsack.com/img/fecktk/fecktk18.webp",
    "https://actionsack.com/img/fecktk/fecktk19.webp",
    "https://actionsack.com/img/fecktk/fecktk20.webp",
    "https://actionsack.com/img/fecktk/fecktk21.webp",
    "https://actionsack.com/img/fecktk/fecktk22.webp",
    "https://actionsack.com/img/fecktk/fecktk23.webp",
    "https://actionsack.com/img/fecktk/fetus.webp",
    "https://actionsack.com/img/fecktk/guilty.webp",
    "https://actionsack.com/img/fecktk/holden.webp",
    "https://actionsack.com/img/fecktk/lildick.webp",
    "https://actionsack.com/img/fecktk/mumble.webp",
    "https://actionsack.com/img/fecktk/neck.webp",
    "https://actionsack.com/img/fecktk/newegg.webp",
    "https://actionsack.com/img/fecktk/newhouse.webp",
    "https://actionsack.com/img/fecktk/punch.webp",
    "https://actionsack.com/img/fecktk/rape.webp",
    "https://actionsack.com/img/fecktk/sandwich.webp",
    "https://actionsack.com/img/fecktk/slap.webp",
    "https://actionsack.com/img/fecktk/snatch.webp",
    "https://actionsack.com/img/fecktk/strim.webp",
    "https://actionsack.com/img/fecktk/zoomies.webp"
  ]
  bot.say(random.choice(fecktks))

@module.rule(".*!feek.*")
@module.commands("feek")
@module.rate(user=900)
def feek(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  feeks = [
    "Works for Me™",
    "https://actionsack.com/img/feek/ben.webp",
    "https://actionsack.com/img/feek/bitch.webp",
    "https://actionsack.com/img/feek/die.webp",
    "https://actionsack.com/img/feek/error.webp",
    "https://actionsack.com/img/feek/feek01.webp",
    "https://actionsack.com/img/feek/feek02.webp",
    "https://actionsack.com/img/feek/feek03.webp",
    "https://actionsack.com/img/feek/feek04.webp",
    "https://actionsack.com/img/feek/feek05.webp",
    "https://actionsack.com/img/feek/feek06.webp",
    "https://actionsack.com/img/feek/feek07.webp",
    "https://actionsack.com/img/feek/feek08.webp",
    "https://actionsack.com/img/feek/free.webp",
    "https://actionsack.com/img/feek/hated.webp",
    "https://actionsack.com/img/feek/hidden.webp",
    "https://actionsack.com/img/feek/lucky.webp",
    "https://actionsack.com/img/feek/PokéKeith.webp",
    "https://actionsack.com/img/feek/rape.webp"
  ]
  bot.say(random.choice(feeks))

@module.rule(".*!jaja.*")
@module.commands("jaja")
@module.rate(user=900)
def jajabro(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  jajabros = [
    "https://actionsack.com/img/jaja/dogs.png",
    "https://actionsack.com/img/jaja/halo.jpg",
    "https://actionsack.com/img/jaja/jaja01.png",
    "https://actionsack.com/img/jaja/jaja02.png",
    "https://actionsack.com/img/jaja/jaja03.png",
    "https://actionsack.com/img/jaja/jaja04.png",
    "https://actionsack.com/img/jaja/jaja05.png",
    "https://actionsack.com/img/jaja/jaja06.gif",
    "https://actionsack.com/img/jaja/jaja07.gif",
    "https://actionsack.com/img/jaja/jaja08.png",
    "https://actionsack.com/img/jaja/jaja09.png",
    "https://actionsack.com/img/jaja/jaja10.png",
    "https://actionsack.com/img/jaja/jaja11.png",
    "https://actionsack.com/img/jaja/jaja12.png",
    "https://actionsack.com/img/jaja/plush.png",
    "https://actionsack.com/img/jaja/que.png",
    "https://actionsack.com/img/jaja/smrt.gif",
    "https://actionsack.com/img/jaja/subwat.png"
  ]
  bot.say(random.choice(jajabros))

@module.rule(".*!mike.*")
@module.commands("mike")
@module.rate(user=900)
def mike(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  mikes = [
    "https://actionsack.com/img/mike/720v1080.png",
    "https://actionsack.com/img/mike/8ball.png",
    "https://actionsack.com/img/mike/amnesia.png",
    "https://actionsack.com/img/mike/bath.png",
    "https://actionsack.com/img/mike/bernie.png",
    "https://actionsack.com/img/mike/blowie.png",
    "https://actionsack.com/img/mike/brony.png",
    "https://actionsack.com/img/mike/change.png",
    "https://actionsack.com/img/mike/cocksucker.png",
    "https://actionsack.com/img/mike/cuppstick.gif",
    "https://actionsack.com/img/mike/cuppstick.png",
    "https://actionsack.com/img/mike/dance.mp4",
    "https://actionsack.com/img/mike/doll.png",
    "https://actionsack.com/img/mike/down.gif",
    "https://actionsack.com/img/mike/drink.gif",
    "https://actionsack.com/img/mike/everydaymike.gif",
    "https://actionsack.com/img/mike/fraud.png",
    "https://actionsack.com/img/mike/graphene.png",
    "https://actionsack.com/img/mike/haloistrash.png",
    "https://actionsack.com/img/mike/high.png",
    "https://actionsack.com/img/mike/MAGA.png",
    "https://actionsack.com/img/mike/mashed-potatoes.png",
    "https://actionsack.com/img/mike/mike001.png",
    "https://actionsack.com/img/mike/mike002.png",
    "https://actionsack.com/img/mike/mike004.png",
    "https://actionsack.com/img/mike/mike005.png",
    "https://actionsack.com/img/mike/mike006.png",
    "https://actionsack.com/img/mike/mike008.png",
    "https://actionsack.com/img/mike/mike009.png",
    "https://actionsack.com/img/mike/mike010.png",
    "https://actionsack.com/img/mike/mike011.png",
    "https://actionsack.com/img/mike/mike012.png",
    "https://actionsack.com/img/mike/mike013.png",
    "https://actionsack.com/img/mike/mike014.png",
    "https://actionsack.com/img/mike/mike015.png",
    "https://actionsack.com/img/mike/mike016.png",
    "https://actionsack.com/img/mike/mike017.png",
    "https://actionsack.com/img/mike/mike018.png",
    "https://actionsack.com/img/mike/mike019.png",
    "https://actionsack.com/img/mike/mike020.png",
    "https://actionsack.com/img/mike/mike021.png",
    "https://actionsack.com/img/mike/mike022.png",
    "https://actionsack.com/img/mike/mike023.png",
    "https://actionsack.com/img/mike/mike024.png",
    "https://actionsack.com/img/mike/mike025.png",
    "https://actionsack.com/img/mike/mike026.png",
    "https://actionsack.com/img/mike/mike027.png",
    "https://actionsack.com/img/mike/mike028.png",
    "https://actionsack.com/img/mike/mike029.png",
    "https://actionsack.com/img/mike/mike030.png",
    "https://actionsack.com/img/mike/mike031.png",
    "https://actionsack.com/img/mike/mike032.png",
    "https://actionsack.com/img/mike/miker.png",
    "https://actionsack.com/img/mike/MLP.png",
    "https://actionsack.com/img/mike/MMM.png",
    "https://actionsack.com/img/mike/noctua.png",
    "https://actionsack.com/img/mike/nosex.png",
    "https://actionsack.com/img/mike/quora.png",
    "https://actionsack.com/img/mike/simple-mike.png",
    "https://actionsack.com/img/mike/smurf.png",
    "https://actionsack.com/img/mike/syria.png",
    "https://actionsack.com/img/mike/virgin.png",
    "https://actionsack.com/img/mike/yoj.png",
    "https://actionsack.com/img/mike/yummy-mike.png",
    "https://actionsack.com/img/mike/📖/📖+.jpg",
    "https://actionsack.com/img/mike/📖/📖.gif",
    "https://actionsack.com/img/mike/📖/📖.jpg",
    "https://actionsack.com/img/mike/📖/📖🐇.jpg"
  ]
  bot.say(random.choice(mikes))

@module.rule(".*!tasian.*")
@module.commands("tasian")
@module.rate(user=900)
def tasian(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  tasians = [
    "https://actionsack.com/img/tasian/2016.webp",
    "https://actionsack.com/img/tasian/balloon.webp",
    "https://actionsack.com/img/tasian/dance.webp",
    "https://actionsack.com/img/tasian/dance.mp4",
    "https://actionsack.com/img/tasian/D.webp",
    "https://actionsack.com/img/tasian/driver.webp",
    "https://actionsack.com/img/tasian/fortnite.webp",
    "https://actionsack.com/img/tasian/grin.webp",
    "https://actionsack.com/img/tasian/korea.webp",
    "https://actionsack.com/img/tasian/koreatext.webp",
    "https://actionsack.com/img/tasian/math.webp",
    "https://actionsack.com/img/tasian/naga.webp",
    "https://actionsack.com/img/tasian/noodles.webp",
    "https://actionsack.com/img/tasian/pacman.webp",
    "https://actionsack.com/img/tasian/pickles.webp",
    "https://actionsack.com/img/tasian/pikaval.webp",
    "https://actionsack.com/img/tasian/racist01.webp",
    "https://actionsack.com/img/tasian/racist02.webp",
    "https://actionsack.com/img/tasian/racist03.webp",
    "https://actionsack.com/img/tasian/raughs.webp",
    "https://actionsack.com/img/tasian/singing.mp4",
    "https://actionsack.com/img/tasian/tall.webp",
    "https://actionsack.com/img/tasian/val01.webp",
    "https://actionsack.com/img/tasian/val02.webp",
    "https://actionsack.com/img/tasian/val03.webp",
    "https://actionsack.com/img/tasian/val04.webp",
    "https://actionsack.com/img/tasian/val05.webp",
    "https://actionsack.com/img/tasian/val06.webp",
    "https://actionsack.com/img/tasian/val07.webp"
  ]
  bot.say(random.choice(tasians))

@module.rule(".*!viz.*")
@module.commands("viz")
@module.rate(user=900)
def viz(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  vizs = [
    "https://actionsack.com/img/viz/bad4u.webp",
    "https://actionsack.com/img/viz/drunk01.webp",
    "https://actionsack.com/img/viz/drunk02.webp",
    "https://actionsack.com/img/viz/drunk03.webp",
    "https://actionsack.com/img/viz/drunk04.webp",
    "https://actionsack.com/img/viz/drunk05.webp",
    "https://actionsack.com/img/viz/drunk06.webp",
    "https://actionsack.com/img/viz/drunk07.webp",
    "https://actionsack.com/img/viz/drunk08.webp",
    "https://actionsack.com/img/viz/drunk09.webp",
    "https://actionsack.com/img/viz/fecktk.webp",
    "https://actionsack.com/img/viz/FOT.webp",
    "https://actionsack.com/img/viz/lololololol.webp",
    "https://actionsack.com/img/viz/lovescock.webp",
    "https://actionsack.com/img/viz/oh.ok.webp",
    "https://actionsack.com/img/viz/poison.webp",
    "https://actionsack.com/img/viz/ride.webp",
    "https://actionsack.com/img/viz/tree.webp",
    "https://actionsack.com/img/viz/whoknows.webp"
  ]
  bot.say(random.choice(vizs))

@module.rule(".*!voodoo.*")
@module.commands("voodoo")
def voodoo(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  voodoos = [
    "https://actionsack.com/img/voodoo/eggslut.webp",
    "https://actionsack.com/img/voodoo/eggslut-lq.webp",
    "https://actionsack.com/img/voodoo/eggslut-smol.webp",
    "https://actionsack.com/img/voodoo/pewpew.webp",
    "I fantasize about fucking California's earthquake fault line. The dirt, the debris, the thought of the earth quivering under me as I slowly stick my dick into its gaping wide entrance. I keep looking at news stories and getting the firmest erections of my life seeing those beautiful cracks. She's so open and so wanting. Each earthquake is like another whimper just begging for me to take her. The amount of cum I've lost just thinking about thrusting my rod into our beloved planet. Talk about getting my rocks off. Fuck I'm hard."
  ]
  bot.say(random.choice(voodoos), max_messages=2)

@module.rule(".*!xnaas.*")
@module.commands("xnaas")
@module.rate(user=900)
def xnaas(bot, trigger):
  """A user triggering this command can only do so once per 15 minutes."""
  xnass = [
    "https://actionsack.com/img/xnaas/animals.webp",
    "https://actionsack.com/img/xnaas/d3.webm",
    "https://actionsack.com/img/xnaas/fd.mp4",
    "https://actionsack.com/img/xnaas/gape.webp",
    "https://actionsack.com/img/xnaas/iShit.webp",
    "https://actionsack.com/img/xnaas/mac.webp",
    "https://actionsack.com/img/xnaas/propain.webp",
    "https://actionsack.com/img/xnaas/pussy.mp4",
    "https://actionsack.com/img/xnaas/QotH.webp",
    "https://actionsack.com/img/xnaas/reality.webp",
    "https://actionsack.com/img/xnaas/shaved.webp",
    "https://actionsack.com/img/xnaas/typing.webp",
    "https://actionsack.com/img/xnaas/vamp.webp",
    "https://actionsack.com/img/xnaas/victory.webp",
    "https://actionsack.com/img/xnaas/wesmart.webp",
    "https://actionsack.com/img/xnaas/xnaas001.webp",
    "https://actionsack.com/img/xnaas/xnaas002.webp",
    "https://actionsack.com/img/xnaas/xnaas003.webp",
    "https://actionsack.com/img/xnaas/xnaas004.webp",
    "https://actionsack.com/img/xnaas/xnaas005.webp",
    "https://actionsack.com/img/xnaas/xnaas006.webp",
    "https://actionsack.com/img/xnaas/xnaas008.webp",
    "https://actionsack.com/img/xnaas/xnaas009.webp",
    "https://actionsack.com/img/xnaas/xnaas010.webp",
    "https://actionsack.com/img/xnaas/xnaas011.webp",
    "https://actionsack.com/img/xnaas/xnaas012.webp",
    "https://actionsack.com/img/xnaas/xnaas013.webp",
    "https://actionsack.com/img/xnaas/xnaas014.webp",
    "https://actionsack.com/img/xnaas/yeehaw.webp",
    "https://actionsack.com/img/videos/tesla.webm"
  ]
  bot.say(random.choice(xnass))
# /Action Sack People Section

@module.rule(".*!RGB.*")
@module.commands("RGB")
def RGB(bot, trigger):
  """Can also be triggered with '!RGB' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/RGB.webp")

@module.rule(".*savage!.*")
def savage(bot, trigger):
  bot.say("https://actionsack.com/img/misc/savage.gif")

@module.rule(".*salad.*")
def salad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🥗.png")

@module.rule(".*rickles.*")
def rickles(bot, trigger):
  bot.say("https://actionsack.com/img/misc/rickles.png")

@module.rule(r"^(yo|)u\swin.*")
def uwin(bot, trigger):
  bot.say("https://actionsack.com/img/misc/uWin.png")

@module.rule(r"^you\sdon\'t\ssay.*")
def udontsay(bot, trigger):
  bot.say("https://actionsack.com/img/misc/yds.png")

@module.rule(r".*you\'re\stoo\sslow.*")
def urtooslow(bot, trigger):
  too_slow = [
    "https://actionsack.com/img/sanic/master.png",
    "https://actionsack.com/img/sanic/running.gif"
  ]
  bot.say(random.choice(too_slow))

@module.rule(r".*whale\srape.*")
def whalerape(bot, trigger):
  bot.say("https://actionsack.com/img/videos/whalerape.mp4")

@module.rule(".*kwaken.*")
def kwaken(bot, trigger):
  bot.say("https://actionsack.com/img/misc/kwaken.png")

@module.rule(".*KFC.*")
def kfc(bot, trigger):
  kfc = [
    "https://actionsack.com/img/kfc/00.png",
    "https://actionsack.com/img/kfc/01.png",
    "https://actionsack.com/img/kfc/02.png",
  ]
  bot.say(random.choice(kfc))

@module.rule(".*(?<!en)joy!.*")
def joy(bot, trigger):
  bot.say("https://actionsack.com/img/misc/joy.gif")

@module.rule(".*bernie.*")
def bernii(bot, trigger):
  bot.say("https://actionsack.com/img/misc/bernii.webp")

@module.rule(".*blumkin.*")
def blumpkin(bot, trigger):
  bot.say("https://actionsack.com/img/misc/blumkin.gif")

@module.rule(".*!(chief|halo).*")
@module.commands("chief", "halo")
def chief(bot, trigger):
  """Posts a Master Chief/Halo-related image.
  Can also be triggered with '!chief' or '!halo' anywhere in chat."""
  master_chef = [
    "https://actionsack.com/img/son/chiefs.webp",
    "https://actionsack.com/img/son/halo.webp",
    "https://actionsack.com/img/halo/59bullets.png",
    "https://actionsack.com/img/halo/anime.png",
    "https://actionsack.com/img/halo/car.gif",
    "https://actionsack.com/img/halo/face00.gif",
    "https://actionsack.com/img/halo/face01.gif",
    "https://actionsack.com/img/halo/Halo5.png",
    "https://actionsack.com/img/halo/happening.gif",
    "https://actionsack.com/img/halo/jaja.png",
    "https://actionsack.com/img/halo/perfect_game.png",
    "https://actionsack.com/img/halo/pony.png",
    "https://actionsack.com/img/halo/skiing.png",
    "https://actionsack.com/img/halo/what_do_you_think.png",
    "https://actionsack.com/img/halo/❔.png",
    "https://actionsack.com/img/halo/🗑.png"
  ]
  bot.say(random.choice(master_chef))

@module.rule(".*!drphil.*")
@module.commands("drphil")
def drphil(bot, trigger):
  """Can also be triggered with '!drphil' anywhere in a message."""
  dr_phil = [
    "https://actionsack.com/img/drphil/apples.webp",
    "https://actionsack.com/img/drphil/ride.webp",
    "https://actionsack.com/img/drphil/WSTYAHHWASFOH.webp"
  ]
  bot.say(random.choice(dr_phil))

@module.rule(".*🌀.*")
def hurricane(bot, trigger):
  hurricanes = [
    "https://actionsack.com/img/🌀/AD.png",
    "https://actionsack.com/img/🌀/matthew.png"
  ]
  bot.say(random.choice(hurricanes))

@module.rule(".*!pepe.*")
@module.commands("pepe")
def pepe(bot, trigger):
  """Posts a rare pepe into chat.
  Can also be triggered with '!pepe' anywhere in a message."""
  rare_pepes = [
    "https://actionsack.com/img/pepe/anime.png",
    "https://actionsack.com/img/pepe/black.png",
    "https://actionsack.com/img/pepe/bulba.jpg",
    "https://actionsack.com/img/pepe/combat.gif",
    "https://actionsack.com/img/pepe/cthulhu.png",
    "https://actionsack.com/img/pepe/great-post.png",
    "https://actionsack.com/img/pepe/human-mouth.gif",
    "https://actionsack.com/img/pepe/reeeee.gif",
    "https://actionsack.com/img/pepe/religion.jpg",
    "https://actionsack.com/img/pepe/steak.png",
    "https://actionsack.com/img/pepe/sub.png",
    "https://actionsack.com/img/pepe/trump.png"
  ]
  bot.say(random.choice(rare_pepes))

@module.rule(".*repost.*")
def repost(bot, trigger):
  reposts = [
    "https://actionsack.com/img/repost/3weeks.png",
    "https://actionsack.com/img/repost/5minutes.png",
    "https://actionsack.com/img/repost/back-to-the-repost.png",
    "https://actionsack.com/img/repost/better.gif",
    "https://actionsack.com/img/repost/cat.webp",
    "https://actionsack.com/img/repost/cock.png",
    "https://actionsack.com/img/repost/detected.gif",
    "https://actionsack.com/img/repost/evil.gif",
    "https://actionsack.com/img/repost/GotG.mp4",
    "https://actionsack.com/img/repost/groundhog.gif",
    "https://actionsack.com/img/repost/homer.png",
    "https://actionsack.com/img/repost/IB.mp4",
    "https://actionsack.com/img/repost/ITSAREPOST!!!.png",
    "https://actionsack.com/img/repost/jurassic.gif",
    "https://actionsack.com/img/repost/MiB.webp",
    "https://actionsack.com/img/repost/nobody_cares.gif",
    "https://actionsack.com/img/repost/ohshit.mp4",
    "https://actionsack.com/img/repost/pacific_rim.gif",
    "https://actionsack.com/img/repost/picard.mp4",
    "https://actionsack.com/img/repost/police.png",
    "https://actionsack.com/img/repost/rekt.gif",
    "https://actionsack.com/img/repost/remember.png",
    "https://actionsack.com/img/repost/repeat.gif",
    "https://actionsack.com/img/repost/security-check.png",
    "https://actionsack.com/img/repost/seinfeld.gif",
    "https://actionsack.com/img/repost/soflo.png",
    "https://actionsack.com/img/repost/wait....gif"
  ]
  bot.say(random.choice(reposts))

@module.rule("^(rip|🪦)$")
def rip(bot, trigger):
  bot.say("https://actionsack.com/img/emoji/rip.png")

@module.rule(".*!trump.*")
@module.commands("trump")
def trump(bot, trigger):
  """Can also be triggered with '!trump' anywhere in a message."""
  trumps = [
    "https://actionsack.com/img/trump/baby.png",
    "https://actionsack.com/img/trump/beatdown.gif",
    "https://actionsack.com/img/trump/bingbong.png",
    "https://actionsack.com/img/trump/blog.mp4",
    "https://actionsack.com/img/trump/boo!.mp4",
    "https://actionsack.com/img/trump/caress.gif",
    "https://actionsack.com/img/trump/covfefe.png",
    "https://actionsack.com/img/trump/dump.png",
    "https://actionsack.com/img/trump/fuckyou.gif",
    "https://actionsack.com/img/trump/golf.gif",
    "https://actionsack.com/img/trump/HEYYOUGUYS.png",
    "https://actionsack.com/img/trump/kiss.png",
    "https://actionsack.com/img/trump/monster.mp4",
    "https://actionsack.com/img/trump/nagus.png",
    "https://actionsack.com/img/trump/no.mp4",
    "https://actionsack.com/img/trump/real-villian.gif",
    "https://actionsack.com/img/trump/reason.mp4",
    "https://actionsack.com/img/trump/satan.gif",
    "https://actionsack.com/img/trump/sauron.png",
    "https://actionsack.com/img/trump/simple.png",
    "https://actionsack.com/img/trump/stump.gif",
    "https://actionsack.com/img/trump/tacos.gif",
    "https://actionsack.com/img/trump/tap.png",
    "https://actionsack.com/img/trump/tears.mp4",
    "https://actionsack.com/img/trump/tears.png",
    "https://actionsack.com/img/trump/think.png",
    "https://actionsack.com/img/trump/troll.png",
    "https://actionsack.com/img/trump/trump-chan.png",
    "https://actionsack.com/img/trump/trumpler.mp4",
    "https://actionsack.com/img/trump/trump-vs-hillary.mp4",
    "https://actionsack.com/img/trump/trump-yell.png",
    "https://actionsack.com/img/trump/wall.mp4",
    "https://actionsack.com/img/trump/WOF.png",
    "https://actionsack.com/img/trump/トランプ.webm"
  ]
  bot.say(random.choice(trumps))

@module.commands("downvote")
def downvote(bot, trigger):
  downvotes = [
    "https://actionsack.com/img/vote/down/00.gif"
  ]
  bot.say(random.choice(downvotes))

@module.commands("upvote")
def upvote(bot, trigger):
  upvotes = [
    "https://actionsack.com/img/vote/up/00.mp4",
    "https://actionsack.com/img/vote/up/01.mp4"
  ]
  bot.say(random.choice(upvotes))

@module.rule(r"^apologize\.(\s$|$)")
def apologize(bot, trigger):
  bot.say("https://actionsack.com/img/misc/apologize.webp")

@module.rule(r".*(?<!sh)it\'s\shappening.*")
def happening(bot, trigger):
  its_happening = [
    "https://actionsack.com/img/halo/happening.gif",
    "https://actionsack.com/img/misc/happening.gif"
  ]
  bot.say(random.choice(its_happening))

@module.rule(r"^It\'s\stime\sto\sstop!$")
def timetostop(bot, trigger):
  time_to_stop = [
    "https://actionsack.com/img/🛑/00.webp",
    "https://actionsack.com/img/🛑/01.webp",
    "https://actionsack.com/img/🛑/02.webp",
    "https://actionsack.com/img/🛑/03.webp",
  ]
  bot.say(random.choice(time_to_stop))

@module.rule(".*pepsi.*")
def pepsi(bot, trigger):
  bot.say("https://actionsack.com/img/misc/pepsi.gif")

@module.rule(".*terrorist.*")
def terrorists(bot, trigger):
  bot.say("https://actionsack.com/img/misc/terrorist.gif")

@module.rule(r".*space\spants!.*")
def spacepants(bot, trigger):
  space_pants = [
    "https://actionsack.com/img/misc/spacepants.gif",
    "https://actionsack.com/img/videos/spacepants.mp4"
  ]
  bot.say(random.choice(space_pants))

@module.rule(".*!peep.*")
@module.commands("peep")
def peep(bot, trigger):
  """Peep on chat. Can also be triggered with '!peep' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/peep.gif")

@module.rule(".*🥒.*")
def cucumber(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🥒.gif")

@module.rule(".*krang.*")
def krang(bot, trigger):
  bot.say("https://actionsack.com/img/misc/krang.png")

@module.rule(".*!reality.*")
@module.commands("reality")
@module.rate(channel=86400)
def reality(bot, trigger):
  """Lays down a hard reality. Rate-limited to once per day per channel."""
  bot.say("https://actionsack.com/img/xnaas/reality.webp")

@module.rule(r".*mass\smurder.*")
@module.commands("shooting")
def shooting(bot, trigger):
  bot.say("https://actionsack.com/img/misc/shooting.gif")

@module.rule(r".*🆒(|\s)🐱.*")
def coolcat(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🆒🐱.png")

@module.rule(".*shitpost.*")
def shitpost(bot, trigger):
  shit_post = [
    "https://actionsack.com/img/shitpost/catpost.gif",
    "https://actionsack.com/img/shitpost/dbz.png",
    "https://actionsack.com/img/shitpost/shitpost.png"
  ]
  bot.say(random.choice(shit_post))

@module.rule("^No!$")
def no(bot, trigger):
  nonono = [
    "https://actionsack.com/img/no/00.mp4",
    "https://actionsack.com/img/no/01.mp4",
  ]
  bot.say(random.choice(nonono))

@module.rule(r"^just\.\.\.no$")
def justno(bot, trigger):
  bot.say("https://actionsack.com/img/no/just...no.webp")

@module.rule(".*🏇.*")
def horses(bot, trigger):
  race_horses = [
    "https://actionsack.com/img/🏇/girl.gif",
    "https://actionsack.com/img/🏇/hoh.gif"
  ]
  bot.say(random.choice(race_horses))

@module.rule(".*👽.*")
def alien(bot, trigger):
  bot.say("https://actionsack.com/img/misc/👽.webp")

@module.rule(".*😮{3,}.*")
def gaping_mouth(bot, trigger):
  bot.say("https://actionsack.com/img/misc/😮.webp")

@module.rule(".*🕷(?!👨).*")
def spider(bot, trigger):
  spiders = [
    "https://actionsack.com/img/🕷/cat.webp",
    "https://actionsack.com/img/🕷/girl.webp",
    "https://actionsack.com/img/🕷/song.webp",
    "https://actionsack.com/img/🕷/swing.webp"
  ]
  bot.say(random.choice(spiders))

@module.rule(r".*(spiderman|🕷(|\s)👨).*")
def spiderman(bot, trigger):
  spider_man = [
    "https://actionsack.com/img/🕷👨/orphans.webp",
    "https://actionsack.com/img/🕷👨/smell.webp"
  ]
  bot.say(random.choice(spider_man))

@module.rule(".*shitstorm.*")
def shitstorm(bot, trigger):
  bot.say("https://actionsack.com/img/misc/shitstorm.webp")

@module.rule("!ts")
@module.commands("ts")
def teamspeak(bot, trigger):
  bot.say("https://actionsack.com/img/music/teamspeak.opus")

@module.rule(".*!tmf.*")
@module.commands("tmf")
def thatsmyfetish(bot, trigger):
  """That's my fetish. ( ͡° ͜ʖ ͡°)"""
  bot.say("https://actionsack.com/img/misc/tmf.webp")

@module.rule("^NDA$")
def nda(bot, trigger):
    bot.say(formatting.bold("⚠️ That's ⚠️ some ⚠️ NDA ⚠️ shit ⚠️ right ⚠️ there! ⚠️"))

@module.rule(".*darude.*")
def darude(bot, trigger):
    bot.say("https://actionsack.com/img/videos/darude.mp4")

@module.rule(".*numa.*")
def numanuma(bot, trigger):
    bot.say("https://actionsack.com/img/videos/numa.mp4")
