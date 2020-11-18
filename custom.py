from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, formatting
import random
import itertools
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
  bot.say("https://actionsack.com/img/trek/nod.gif")

@module.commands("spok")
def spok(bot, trigger):
  """Summon SPOK into chat."""
  bot.say("https://actionsack.com/img/trek/spok.gif")

@module.rule("^Hello(\?|!)$")
def hi(bot, trigger):
  bot.say("Hello, %s!" %trigger.nick)

@module.rule("^(Nice\.)(\s$|$)")
def nice(bot, trigger):
  bot.say(trigger.group(1))

@module.rule("^(This\sis\sThe\sWay\.)($|\s$)")
def theway(bot, trigger):
  bot.say(trigger.group(1))

@module.rule("^(It\sis\sknown\.)(\s$|$)")
def itisknown(bot, trigger):
  bot.say(trigger.group(1))

@module.rule("^yeah!$")
def yeah(bot, trigger):
  bot.say("https://actionsack.com/img/misc/yeah!.gif")

@module.rule("^retard.*")
def retarded(bot, trigger):
  retard = [
    "https://actionsack.com/img/retard/catarded.png",
    "https://actionsack.com/img/retard/retarded.gif",
    "https://actionsack.com/img/retard/△.gif"
  ]
  bot.say(random.choice(retard))

@module.rule(".*rekt.*")
def rekt(bot, trigger):
  rekt = [
    "https://actionsack.com/img/rekt/baseball.gif",
    "https://actionsack.com/img/rekt/beachdive.mp4",
    "https://actionsack.com/img/rekt/beachskillz.mp4",
    "https://actionsack.com/img/rekt/bf1revenge.mp4",
    "https://actionsack.com/img/rekt/bf1sniper.mp4",
    "https://actionsack.com/img/rekt/blackman.mp4",
    "https://actionsack.com/img/rekt/botw-sled.mp4",
    "https://actionsack.com/img/rekt/bridgedive.mp4",
    "https://actionsack.com/img/rekt/carcrash.gif",
    "https://actionsack.com/img/rekt/gta-bike.mp4",
    "https://actionsack.com/img/rekt/gta-flight.mp4",
    "https://actionsack.com/img/rekt/gta-phone.mp4",
    "https://actionsack.com/img/rekt/gta-post.mp4",
    "https://actionsack.com/img/rekt/gta-rekt.mp4",
    "https://actionsack.com/img/rekt/gta-stomp.gif",
    "https://actionsack.com/img/rekt/jeep.gif",
    "https://actionsack.com/img/rekt/leap!.mp4",
    "https://actionsack.com/img/rekt/LOLOLOLOL.gif",
    "https://actionsack.com/img/rekt/poolgirl.gif",
    "https://actionsack.com/img/rekt/rekt.png",
    "https://actionsack.com/img/rekt/running.gif",
    "https://actionsack.com/img/rekt/skateit.mp4",
    "https://actionsack.com/img/rekt/slammin.mp4",
    "https://actionsack.com/img/rekt/smash.mp4",
    "https://actionsack.com/img/rekt/sniped.mp4",
    "https://actionsack.com/img/rekt/walkbot.mp4",
    "https://actionsack.com/img/rekt/walkitoff.mp4",
    "https://actionsack.com/img/rekt/watergun.mp4"
  ]
  bot.say(random.choice(rekt))

@module.rule("^420.*")
def fourtwenty(bot, trigger):
  fourtwozero = [
    "https://actionsack.com/img/420/birb.png",
    "https://actionsack.com/img/420/champions.png",
    "https://actionsack.com/img/420/claim.png",
    "https://actionsack.com/img/420/coma.png",
    "https://actionsack.com/img/420/comrade.png",
    "https://actionsack.com/img/420/crewdragon.png",
    "https://actionsack.com/img/420/dr.png",
    "https://actionsack.com/img/420/exp.png",
    "https://actionsack.com/img/420/gravityfalls.png",
    "https://actionsack.com/img/420/highnoon.gif",
    "https://actionsack.com/img/420/highnoon.png",
    "https://actionsack.com/img/420/lisa.png",
    "https://actionsack.com/img/420/mowing.png",
    "https://actionsack.com/img/420/old.png",
    "https://actionsack.com/img/420/pikachu.png",
    "https://actionsack.com/img/420/🍩.png",
    "https://actionsack.com/img/420/pokemon.png",
    "https://actionsack.com/img/420/realdanger.png",
    "https://actionsack.com/img/420/sealab.png",
    "https://actionsack.com/img/420/telluhwat.png",
    "https://actionsack.com/img/420/thomas.png",
    "https://actionsack.com/img/420/thomasrust.png",
    "https://actionsack.com/img/420/timesheet.png",
    "https://actionsack.com/img/420/toasted.gif",
    "https://actionsack.com/img/420/toystory.png",
    "https://actionsack.com/img/420/wednesday.png"
  ]
  bot.say(random.choice(fourtwozero))

@module.rule(":retardeyes:")
def retardeyes(bot, trigger):
  bot.say("https://cdn.discordapp.com/emojis/286222898836799488.png")

@module.rule("^thx.*")
def thx(bot, trigger):
  bot.say("https://actionsack.com/img/thx/thx.png")

@module.rule("^(thanks.*|thank\syou.*)")
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
    "https://actionsack.com/img/QQ/QQ001.gif",
    "https://actionsack.com/img/QQ/QQ002.gif",
    "https://actionsack.com/img/QQ/QQ003.gif",
    "https://actionsack.com/img/QQ/QQ004.gif",
    "https://actionsack.com/img/QQ/QQ005.gif",
    "ಥ_ಥ",
    "＞︿＜",
    "＞﹏＜",
    "X﹏X",
    "(T_T)"
  ]
  bot.say(random.choice(crying))

@module.rule(".*!xms.*", ".*!bge.*")
def xms(bot, trigger):
  bot.say("https://w2g.tv/rooms/actionsack-csurhbl9dkwvwnk91a")

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

@module.rule("^FOAD.*")
def foad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/foad.png")

@module.rule(".*adapters.*")
def adapters(bot, trigger):
  adapters = [
    "https://actionsack.com/img/misc/adapters01.png",
    "https://actionsack.com/img/misc/adapters02.png"
  ]
  bot.say(random.choice(adapters))

@module.rule(".*accident\W")
def accident(bot, trigger):
  bot.say("https://actionsack.com/img/misc/accident.png")

@module.rule(".*14nm.*")
def fourteennm(bot, trigger):
  bot.say("https://actionsack.com/img/misc/14nm+++++.mp4")

@module.rule("^bait.*")
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
  bot.say("https://actionsack.com/img/misc/angryeyes.gif")

@module.rule(".*alot.*")
def alot(bot, trigger):
  bot.say("https://actionsack.com/img/alot/")

@module.rule(".*♿.*")
def handicap(bot, trigger):
  bot.say("https://actionsack.com/img/♿/♿.mp4")

@module.rule(".*⤵️.*")
def down(bot, trigger):
  bot.say("https://actionsack.com/img/mike/down.gif")

@module.rule("^\.\.\.$")
def dotdotdot(bot, trigger):
  bot.say("...")

@module.rule("^\.dz$")
def deeznutz(bot, trigger):
  bot.say(formatting.bold("DEEZ NUTZ!"))

@module.rule("^\s\/lenny$")
def lenny(bot, trigger):
  lenny = [
    "https://actionsack.com/img/lenny/anime.gif",
    "https://actionsack.com/img/lenny/crazy.mp4",
    "https://actionsack.com/img/lenny/spiral.gif"
  ]
  bot.say(random.choice(lenny))

@module.commands("rlenny")
def rlenny(bot, trigger):
  """Sends a random ( ͡° ͜ʖ ͡°) variation."""
  rlenny = [
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

@module.rule("^pranked!$")
def prank(bot, trigger):
  prank = [
    "https://actionsack.com/img/prank/prank01.png",
    "https://actionsack.com/img/prank/prank02.png"
  ]
  bot.say(random.choice(prank))

@module.rule("^\?\?\?$")
def que(bot, trigger):
  bot.say("https://actionsack.com/img/misc/¿¿¿.png")

@module.rule("^\\\o/$")
def handsup(bot, trigger):
  bot.say("\\o/")

@module.rule("^¯\\\_\(ツ\)_\/¯$")
def shrug(bot, trigger):
  bot.say("¯\\_(ツ)_/¯")

@module.rule(".*🦏.*")
def rhino(bot, trigger):
  bot.say("https://actionsack.com/img/🦏/🦏.gif")

@module.rule(".*🧀.*")
def cheese(bot, trigger):
  bot.say("https://actionsack.com/img/🧀/🧀.mp4")

@module.rule(".*🦄.*")
def unicorn(bot, trigger):
  bot.say("https://actionsack.com/img/🦄/🦄.jpg")

@module.rule("^🙃$")
def upsidedown(bot, trigger):
  bot.say("🙃")

@module.rule("^🖕($|🏻|🏼|🏽|🏾|🏿)$")
def fuckyouback(bot, trigger):
  bot.say("Fuck you, %s!" %trigger.nick)

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

@module.rule(".*🍍🍕.*")
def sin(bot, trigger):
  bot.say("This is a sin.")

@module.rule(".*xfiles.*")
def xfiles(bot, trigger):
  bot.say("Did you know that the X-Files is going to have 6 new episodes this summer on FOX, Aegisfate?")

@module.rule(".*triggered.*")
def triggered(bot, trigger):
  triggered = [
    "https://actionsack.com/img/triggered/beaker.gif",
    "https://actionsack.com/img/triggered/triggered.gif",
    "https://actionsack.com/img/triggered/feek.gif"
  ]
  bot.say(random.choice(triggered))

@module.rule(".*to\sbe\sfair.*")
def tobefair(bot, trigger):
  bot.say("https://actionsack.com/img/videos/tobefair.webm")

@module.rule("^stop\sbeing\spoor.*")
def stopbeingpoor(bot, trigger):
  bot.say("https://actionsack.com/img/misc/stopbeingpoor.jpg")

@module.commands("tb")
def tb(bot, trigger):
  """Spout technobabble."""
  tb = ["When you account for the nm offset variable, the difference between 32-bit and 64-bit CPUs really only matters when calculating differential sub-routine pipeline algorithms.", "high 32-bit TOS encrypted voIP", "remote access through TeamSpeak", "if you reboot it may cement the command scripts that the virus is using to distribute DDOS variants", "When the biometrics of the boot sector exceeds the buffer cache then clock-cycles reroute to the LAN thus creating  a load balancing markup stack.", "I'll start on a GUI in Visual Basic to backtrack the mainframe.", "You can use the ps commands to redirect you to the home directory provided you used the subversion syntax correctly.", "The Internet is like water in pipes: when one pipe gets cut the Internet pressure drops because it is leaking uncontrollably from the open pipe. The Internet through WiFi, however, is like a swimming pool. If you open a hole in the building or pool the wifi starts flooding out and the wifi starts to lower. That's the reasoning behind revolving doors. Since they're compartmentalized, the building loses a smaller, fixed amount of internet per entry/exit, which reduces costs and allows more consistency for planning an office's WiFi needs.", "I JSON SQL DBs all the time!", "Lol you a pussyyyyy when I pull your IP address I'm gonna take your account then you gonna have to make a new account bc you cant get it back", "Can't leave without your processor? Clone it! You can copy the processor operating code wirelessly with a sniffer device.", "Then they do a triple worm blue cobalt IP hack.", "That's how the hacking's done. Satellite telemetry.", "SECURITY UPDATES CAUSE AUTISM. WON'T SOMEBODY THINK OF THE CHILDREN???", "The asymmetrical phase splitter is offline. We need to compensate for the gravimetric charge imbalance by re-routing power through the electron plasma injector port.", "Overheating weak partitions inverts the critical protocols.", "Higher numbered ports are always faster, because they travel nearer the outside of the wire, and the 'skin effect' means that that type of transmission is more reliable. So port 80 is going to be slower. If you want to connect with a very fast speed, you might want to try port 3389. This is why when you connect to port 22 you're probably only going to get some kind of text interface, if you connect to port 80 you might get some images along with it, and if you connect to port 3389, you'll get to see and interact with the whole operating system.", "That's a node brainer!", "Laptops generally don't need to take as many breaks/pauses as desktops, so they don't need that key. Sometimes, the larger laptops like yours w/ a numpad will have it, but only if the laptop hasn't worked out in a while, and gets winded easily.", "In order to hack a laptop's battery you need to initiate a GET request from an HTML page then use CSS to parse the DOS command XPLDBTRY.EXE that will make the battery's cooling fail, and then explode.", "Atlas Seeds contain zonally-shifted quasi-stellar substrate. WARNING: do not allow matrix to commune with this dimensional space.", "Sending packets is reserved to level 1337 hackers only. If you really want to do this you would need to bypass the FireWire's mainframe on your computer. Then you would need to encrypt and enumerate the firewall of whatever server you are trying to send the packet to. Then you would need to exploit the server's hypervisor root code to overflow the VGA interface. After that, all you need to do is code a VPN in Visual Basic and you should be able to do it without any problems.", "You should rebuild the kernel but only after rebooting your router. It gets a bit tricky with the buttons 'cause you need to press ctrl + alt + printscreen for 5 seconds and at the same time the reset button on your router. Last time I used my hands for the keyboard and reached for the router with one foot and managed to send the packet, although I also installed a firewall on Winamp and now I can only play Nickelback songs.", "Yeah but quantum info extraction was patched by the NSA last month, you gotta entangle the data stream to a local area network loop now.", "Don't worry, you'll just need to use a Raspberry Pi to enable four-factor authentication VPN firewalls and he won't be able to get into the mainframe!", "Uh oh, his friend is good with Linux! Better watch out! He might grep into your sudoers file and DDoS your hard drive!", "We reverse engineered Amazo's operating system and whipped up a virus to wipe his CPU.", "He's got a better grasp on Python 6 malware encryption than anybody at the DEO.", "I don't want to say the computer is old, but its IP address was 1.", "Are you coding in SQL or Java?", "Your UI is open-source JPEGs you got from MP3s off the web.", "Software running slow? Just decompile it!", "The secondary gyrodyne relays of the propulsion field intermatrix have depolarized!", "The Enterprise computer system is controlled by three primary main processing cores, cross-linked with a redundant melacortz ramistat. Fourteen kiloquad interface modules. The core element is based on an FTL nanoprocessor with twenty five bilateral kelilactirals, with twenty of those being slaved into the primary heisenfram terminal.", "Shunt plasma from the buzzard collectors into the Heisenberg compensators in order to generate sufficient tachyon emissions to disperse neutrino buildup around the warp core, thereby establishing a static warp bubble!"]
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

@module.rule("^!b8$")
def beight(bot, trigger):
  bot.say("steam://install/567090")

@module.rule(".*kristen.*")
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

@module.rule("^Tasian\sloves\spickles\.($|\s)")
def tasianpickles(bot, trigger):
  bot.say("https://actionsack.com/img/tasian/pickles.png")

@module.rule(".*!asg.*")
def allsystemsgo(bot, trigger):
  bot.say("https://actionsack.com/img/misc/allsystemsgo.png")

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
@module.rate(server=5400)
def pledge(bot, trigger):
  """Say the United States Pledge of Allegiance.
  Server-wide rate-limit of 90 minutes."""
  bot.say("I pledge allegiance to the flag of the United States of America. Thank you very very much for letting us little kids live here. It really really was nice of you. You didn't have to do it. And it's really not creepy to have little little kids mindlessly recite this anthem every day and pledge their life to a government before theyre old enough to really think about what they're saying.")
  bot.say("This is not a form of brainwashing. This is not a form of brainwashing. This is not a form of brainwashing.")
  bot.say("This is really the greatest country in the whole world. All the other countries suck. And if this country ever goes to go to war, as its often wont to do, I promise to help go and kill all the other country's kids.")
  bot.say("God bless Johnson & Johnson. God bless GE. God bless Citigroup.")

@module.rule(".*mushkin.*")
def mushkin(bot, trigger):
  bot.say("Hey xnaas and feek, did you know that Mushkin announced a 4TB SSD for $500 at CES 2016 and never fuckin' delivered? How neat is that?")

@module.commands("mirai")
def mirai(bot, trigger):
  """Gone but not forgotten, noble soviet bear."""
  bot.say("https://actionsack.com/img/putin/🐻.mp4")

@module.rule(".*!putin.*")
def putin(bot, trigger):
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
  bot.say("https://actionsack.com/img/misc/aidsclub.png")

@module.rule(".*!barometer.*")
def barometer(bot, trigger):
  bot.say("https://actionsack.com/img/misc/barometer.png")

@module.rule("^Oh,\syou!$")
def ohyou(bot, trigger):
  bot.say("https://actionsack.com/img/misc/Oh,you!.jpg")

@module.rule(".*!battletoad.*")
def battletoad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/battletoad.mp4")

@module.rule(".*!beaker.*")
def beaker(bot, trigger):
  bot.say("https://actionsack.com/img/misc/beaker.mp4")

@module.rule(".*!bomb.*")
@module.commands("bomb")
def bomb(bot, trigger):
  """Bombs Japan again... :/
  Can also be triggered with '!bomb' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/bomb.mp4")

@module.rule(".*!broden.*")
def broden(bot, trigger):
  bot.say("https://actionsack.com/img/misc/broden.mp4")

@module.rule(".*mikey\sbikey.*")
def mikeybikey(bot, trigger):
  bot.say("https://actionsack.com/img/as/mikeybikey.png")

@module.rule(".*meal\swith\sit.*")
def mealwithit(bot, trigger):
  bot.say("https://actionsack.com/img/deal/mealwithit.gif")

@module.rule(".*deal\swith\sit.*")
def dealwithit(bot, trigger):
  deal = [
    "https://actionsack.com/img/deal/brule.gif",
    "https://actionsack.com/img/deal/coolkid.gif",
    "https://actionsack.com/img/deal/hippo.mp4",
    "https://actionsack.com/img/deal/mealwithit.gif",
    "https://actionsack.com/img/deal/spider.gif",
    "https://actionsack.com/img/deal/squirtle.gif",
    "https://actionsack.com/img/deal/tf2.gif"
  ]
  bot.say(random.choice(deal))

@module.rule(".*!mindjack.*")
def mindjack(bot, trigger):
  bot.say("https://actionsack.com/img/misc/mindjack.png")

@module.rule(".*!music.*")
def listentomusic(bot, trigger):
  bot.say("https://actionsack.com/img/kys/music.gif")

@module.commands("doge")
def doge(bot, trigger):
  """Doge memes! (There's not very many...)"""
  doge = [
    "https://actionsack.com/img/doge/batdoge.gif",
    "https://actionsack.com/img/doge/dogemine.gif",
    "https://actionsack.com/img/doge/skeledoge.gif"
  ]
  bot.say(random.choice(doge))

@module.rule(".*!dogemine.*")
def dogemine(bot, trigger):
  bot.say("https://actionsack.com/img/doge/dogemine.gif")

@module.rule(".*!skeledoge.*")
def skeledoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/skeledoge.gif")

@module.rule(".*!batdoge.*")
def batdoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/batdoge.gif")

@module.rule(".*slow\sdown.*")
def slowdown(bot, trigger):
  bot.say("https://www.youtube.com/watch?v=fJdqw-JzW08")

@module.require_admin
@module.commands("smmcb", "smd")
def smmcb(bot, trigger):
  bot.say("https://actionsack.com/img/misc/smmcb.gif")

@module.rule("^noice$")
def noice(bot, trigger):
  bot.say("noice")

@module.rule(".*sockbot.*")
def sockbot(bot, trigger):
  sockbot = [
    "https://actionsack.com/img/sockbot/headsortails.png",
    "https://actionsack.com/img/sockbot/L337.png",
    "https://actionsack.com/img/sockbot/phone.png",
    "Gone, but not forgotten.",
    "Good riddance to Discord, but RIP Sockbot. 😢"
  ]
  bot.say(random.choice(sockbot))

@module.rule(".*!brony.*")
def brony(bot, trigger):
  bot.say("https://actionsack.com/img/mike/brony.png")

@module.rule("^banned.*")
def banned(bot, trigger):
  banned = [
    "https://actionsack.com/img/banned/beetlejuice.mp4",
    "https://actionsack.com/img/banned/carryon.png",
    "https://actionsack.com/img/banned/clapping.gif",
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
  bot.say("https://actionsack.com/img/misc/boycott.jpg")

@module.rule(".*censor.*")
def censor(bot, trigger):
  censor = [
    "https://actionsack.com/img/censored/bunny.png",
    "https://actionsack.com/img/censored/censored.png",
    "https://actionsack.com/img/censored/eyesored.png",
    "https://actionsack.com/img/censored/fox.gif",
    "https://actionsack.com/img/censored/fren.png",
    "https://actionsack.com/img/censored/nose.png",
    "https://actionsack.com/img/censored/spider.png",
    "https://actionsack.com/img/censored/tasian.png"
  ]
  bot.say(random.choice(censor))

@module.rule("^Ping!$")
def pingpong(bot, trigger):
  bot.say("Pong!")

@module.rule("^Bing!$")
def bingbong(bot, trigger):
  bot.say("Bong!")

@module.rule("^Ching!$")
def chingchong(bot, trigger):
  bot.say("Chong!")

@module.rule("^Ding!$")
def dingdong(bot, trigger):
  bot.say("Dong!")

@module.rule("^Sing!$")
def singsong(bot, trigger):
  bot.say("Song!")

@module.rule("^Wing!$")
def wingwong(bot, trigger):
  bot.say("Wong!")

@module.rule("^Marco!$")
def marcopolo(bot, trigger):
  bot.say("Polo!")

@module.rule("^Wee!$")
def marcopolo(bot, trigger):
  bot.say("Woo!")

@module.commands("work")
def worktoday(bot, trigger):
  """I don't really wanna do the work today..."""
  bot.say("https://actionsack.com/img/videos/work.webm")

@module.rule(".*stbyn.*")
def stbyn(bot, trigger):
  bot.say("Sucks to be you, %s!" %formatting.italic("nerd"))

@module.rule(".*🥓.*")
def bacon(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🥓.mp4")

@module.rule(".*🍜.*")
def soupbowl(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍜.mp4")

@module.rule(".*🍞.*")
def breadchan(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍞.png")

@module.rule(".*(🎅|🎅🏻|🎅🏼|🎅🏽|🎅🏾|🎅🏿).*")
def santa(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎅.png")

@module.rule(".*🎧.*")
def headphones(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎧.png")

@module.rule(".*fuck\syou(?!r).*")
def fuckyou(bot, trigger):
  fuckyou = [
    "https://actionsack.com/img/fuck/01_Two_Feet-Go_Fuck_Yourself.mp3",
    "https://actionsack.com/img/fuck/airline.mp4",
    "https://actionsack.com/img/fuck/anime.webm",
    "https://actionsack.com/img/fuck/animegfy.mp4",
    "https://actionsack.com/img/fuck/ape.png",
    "https://actionsack.com/img/fuck/aquaman.gif",
    "https://actionsack.com/img/fuck/arms.gif",
    "https://actionsack.com/img/fuck/arrow.mp4",
    "https://actionsack.com/img/fuck/bb8.gif",
    "https://actionsack.com/img/fuck/bird.gif",
    "https://actionsack.com/img/fuck/bot.mp4",
    "https://actionsack.com/img/fuck/buzz.webm",
    "https://actionsack.com/img/fuck/card.gif",
    "https://actionsack.com/img/fuck/climb.gif",
    "https://actionsack.com/img/fuck/compilation.mp4",
    "https://actionsack.com/img/fuck/cunt.mp4",
    "https://actionsack.com/img/fuck/cutout.mp4",
    "https://actionsack.com/img/fuck/deaf.mp4",
    "https://actionsack.com/img/fuck/deer.mp4",
    "https://actionsack.com/img/fuck/disney.gif",
    "https://actionsack.com/img/fuck/doggogfy.mp4",
    "https://actionsack.com/img/fuck/driving.mp4",
    "https://actionsack.com/img/fuck/drums.mp4",
    "https://actionsack.com/img/fuck/enthusiastic.mp4",
    "https://actionsack.com/img/fuck/faoy.mp4",
    "https://actionsack.com/img/fuck/friday.mp4",
    "https://actionsack.com/img/fuck/fuku.png",
    "https://actionsack.com/img/fuck/fur.mp4",
    "https://actionsack.com/img/fuck/godzilla.mp4",
    "https://actionsack.com/img/fuck/gofuckyourself.mp4",
    "https://actionsack.com/img/fuck/goldenboye.mp4",
    "https://actionsack.com/img/fuck/grow.mp4",
    "https://actionsack.com/img/fuck/h3h3.mp4",
    "https://actionsack.com/img/fuck/hook.png",
    "https://actionsack.com/img/fuck/idgaf.mp4",
    "https://actionsack.com/img/fuck/jacket.gif",
    "https://actionsack.com/img/fuck/juliemao.mp4",
    "https://actionsack.com/img/fuck/kraken.gif",
    "https://actionsack.com/img/fuck/loop.gif",
    "https://actionsack.com/img/fuck/peaceamongworlds.gif",
    "https://actionsack.com/img/fuck/pigeon.mp4",
    "https://actionsack.com/img/fuck/pocketcat.gif",
    "https://actionsack.com/img/fuck/pocket.gif",
    "https://actionsack.com/img/fuck/ragnarok.mp4",
    "https://actionsack.com/img/fuck/rudy.png",
    "https://actionsack.com/img/fuck/rugrats.gif",
    "https://actionsack.com/img/fuck/samuel.mp4",
    "https://actionsack.com/img/fuck/samueltransparent.mp4",
    "https://actionsack.com/img/fuck/sayan.gif",
    "https://actionsack.com/img/fuck/sciencegfy.mp4",
    "https://actionsack.com/img/fuck/skating.mp4",
    "https://actionsack.com/img/fuck/square.gif",
    "https://actionsack.com/img/fuck/tommydoor.mp4",
    "https://actionsack.com/img/fuck/trumpet.mp4",
    "https://actionsack.com/img/fuck/westworld.mp4",
    "https://actionsack.com/img/fuck/ww-mib.mp4",
    "https://actionsack.com/img/fuck/☂.gif"
  ]
  bot.say(random.choice(fuckyou))

@module.rule(".*(gfy(?!c)|go\sfuck\syourself).*")
def gfy(bot, trigger):
  gfy = [
    "https://actionsack.com/img/fuck/animegfy.mp4",
    "https://actionsack.com/img/fuck/disney.gif",
    "https://actionsack.com/img/fuck/gofuckyourself.mp4",
    "https://actionsack.com/img/fuck/doggogfy.mp4",
    "https://actionsack.com/img/fuck/sciencegfy.mp4"
  ]
  bot.say(random.choice(gfy))

@module.rule("^What\sthe\sfuck\?$")
def wtfquestion(bot, trigger):
  bot.say("https://actionsack.com/img/wtf/wtf¿.gif")

@module.rule("^What\sthe\sfuck!$")
def wtfexclamation(bot, trigger):
  bot.say("https://actionsack.com/img/wtf/wtfh3h3.mp4")

@module.rule("^Fuck!$")
def fuckexclamation(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuck!.gif")

@module.rule("^Fuck\syeah!$")
def fuckyeah(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuckyeah!.mp4")

@module.rule(".*fuck\severything.*")
def fuckeverything(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuckeverything.mp4")

@module.rule(".*ftge.*")
def ftge(bot, trigger):
  ftge = [
    "https://actionsack.com/img/fuck/ftge.gif",
    "https://actionsack.com/img/fuck/ftge.png"
  ]
  bot.say(random.choice(ftge))

@module.rule(".*fooled\syou.*")
def fooledyou(bot, trigger):
  bot.say("https://actionsack.com/img/misc/fooled.png")

@module.rule(".*fite\sme.*")
def fiteme(bot, trigger):
  fiteme = [
    "https://actionsack.com/img/fite/cat.gif",
    "https://actionsack.com/img/fite/phones.gif",
    "https://actionsack.com/img/fite/🌮.gif"
  ]
  bot.say(random.choice(fiteme))

@module.rule("^Fag!$")
@module.rate(server=5400)
def fagexclamation(bot, trigger):
  bot.say("You're gay. Hey poofta. You're a homo. You're a homo you faggot. Go suck a dick. Go suck a real big dick. Get those dick so far in your mouth that the dick's right there, you got 'em all the way, smashing the back of your throat, balls right there, bangin' on your chin. That's how much I want you to suck dick. Oi. This is me. Pretending to be you. Fist-fuckin' another man in the asshole. Just fist-fuckin' the god-givin' shit out of him. I bet you like that so much you'd like to get fist-fucked while you're doing it. Just getting fist-fucked while you're fist-fuckin' someone else. While you're at it chuck in another one. Just fist-fuckin' two strange men, getting your asshole fist-fucked with someone you just met on Grinder. I bet you wish these were dicks. I bet you wish these were big floppy dicks. You're in a big forest of dicks. Getting dicks all over ya. Covering yourself in cum. Loving cum. Can I suck your dick? Can I suck your dick and then kiss you? Kiss you square on the mouth and then fuck you? Scratch that. Can we make love? Can we make love in my bedroom and then maybe if we connect on more than just a physical level, I'll take you out, I'll introduce you to my mum and my dad and my little sister Jennifer, she's really cool. She's into Goosebumps at the moment. And then maybe we can all go out for dinner together. And they'll really like you because of your cool taste in music and your wonderful dress sense. And then maybe, after confronting their initial misguided preconceptions, my family will come to respect our love for its tangibility. And they'll reject it because of bias or religious and political agendas of hate that have been weaved through the social fabric of hundreds and hundreds of years. FAGGOT!!!", max_messages=6)

@module.rule("^fags$")
def fags(bot, trigger):
  bot.say("https://actionsack.com/img/faggot/fags.png")

@module.rule(".*faggot.*", "^fag$")
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
    "https://actionsack.com/img/gay/gay!.gif",
    "https://actionsack.com/img/gay/gayshit.png"
  ]
  bot.say(random.choice(gayexclamation))

@module.rule(".*everything's\sfucked.*")
def everythingsfucked(bot, trigger):
  bot.say("https://actionsack.com/img/misc/everythingsfucked.gif")

@module.rule("^o\sshit.*")
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

@module.rule(".*\(╯°□°）╯︵ ┻━┻.*")
def unflip(bot, trigger):
  bot.say("┬─┬﻿ ノ( ゜-゜ノ) — Please respect tables, %s." %trigger.nick)

@module.rule(".*bite\sme.*")
@module.require_chanmsg
def bitesback(bot, trigger):
  bot.action("bites %s" %trigger.nick, trigger.sender)

@module.rule("^Bye!$")
def byebye(bot, trigger):
  bot.say("https://actionsack.com/img/misc/BYE!.png")

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

@module.rule("^Deus\svult!$")
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

@module.rule("^I am the machine\.(\s$|$)")
def iamthemachine(bot, trigger):
  bot.say("https://www.youtube.com/watch?v=8PAtFsJY5q0")

@module.rule(".*I\scan't\seven.*", ".*I'm\sliterally\scan't\seven.*")
def icanteven(bot, trigger):
  bot.say("https://actionsack.com/img/videos/icanteven.webm")

@module.rule("^I\sship\s(it|that).*")
def ishipit(bot, trigger):
  bot.say("https://actionsack.com/img/misc/fedex.gif")

@module.rule(".*idgaf.*")
def idgaf(bot, trigger):
  idgaf = [
    "https://actionsack.com/img/idgaf/20thcentury.mp4",
    "https://actionsack.com/img/idgaf/nophux.mp4"
  ]
  bot.say(random.choice(idgaf))

@module.rule(".*hugh\smungus.*")
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
  bot.say("https://actionsack.com/img/videos/jpeg.webm")

@module.rule(".*!kazoo.*")
@module.commands("kazoo")
def kazoo(bot, trigger):
  """Kaaazzzzoooooooooo!!!
  Can also be triggered with '!kazoo' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/kazoo.webm")

@module.rule("^kill\sme.*")
def killme(bot, trigger):
  killme = [
    "https://actionsack.com/img/misc/killme-bulb.png",
    "https://actionsack.com/img/misc/killme-char.png",
    "https://actionsack.com/img/misc/killme-pika.png"
  ]
  bot.say(random.choice(killme))

@module.rule(".*(kys|kill\syourself).*")
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
    "https://actionsack.com/img/kys/pasta.png",
    "https://actionsack.com/img/kys/pepe.png",
    "https://actionsack.com/img/kys/peter-joe.mp4",
    "https://actionsack.com/img/kys/peter.mp4",
    "https://actionsack.com/img/kys/puft.mp4",
    "https://actionsack.com/img/kys/room.gif",
    "https://actionsack.com/img/kys/tried.png",
    "https://actionsack.com/img/kys/wendys.png",
    "https://actionsack.com/img/kys/window.gif",
    "https://lostallhope.com/"
  ]
  bot.say(random.choice(kys))

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
  
  bot.say("%s is %s" %(trigger.group(2), random.choice(judges)))

@module.rule("^wat($|\W)")
def wat(bot, trigger):
  wat = [
    "https://actionsack.com/img/wat/3wats.png",
    "https://actionsack.com/img/wat/65wat.png",
    "https://actionsack.com/img/wat/emma.png",
    "https://actionsack.com/img/wat/filming.gif",
    "https://actionsack.com/img/wat/gigawat.png",
    "https://actionsack.com/img/wat/holdwat.png",
    "https://actionsack.com/img/wat/hwat01.png",
    "https://actionsack.com/img/wat/hwat02.png",
    "https://actionsack.com/img/wat/inthebutt.png",
    "https://actionsack.com/img/wat/jabba.png",
    "https://actionsack.com/img/wat/jaja.png",
    "https://actionsack.com/img/wat/jjwat.png",
    "https://actionsack.com/img/wat/konichiwat.png",
    "https://actionsack.com/img/wat/olde.png",
    "https://actionsack.com/img/wat/police.gif",
    "https://actionsack.com/img/wat/slipwat.png",
    "https://actionsack.com/img/wat/space.gif",
    "https://actionsack.com/img/wat/subwat.png",
    "https://actionsack.com/img/wat/swat.png",
    "https://actionsack.com/img/wat/watchdogs.png",
    "https://actionsack.com/img/wat/watduel.gif",
    "https://actionsack.com/img/wat/waterworld.png",
    "https://actionsack.com/img/wat/wathusky.gif",
    "https://actionsack.com/img/wat/watif.png",
    "https://actionsack.com/img/wat/watinthehat.png",
    "https://actionsack.com/img/wat/watislove.gif",
    "https://actionsack.com/img/wat/watmouth.gif",
    "https://actionsack.com/img/wat/wat.png",
    "https://actionsack.com/img/wat/watshake.gif",
    "https://actionsack.com/img/wat/watwatwatwat.png",
    "https://actionsack.com/img/wat/wow.png"
  ]
  bot.say(random.choice(wat))

@module.rule(".*✝.*")
def praisejesus(bot, trigger):
  bot.say("Praise Jesus!")

@module.rule(".*jesus\schrist.*")
def jesuschrist(bot, trigger):
  bot.say("Praise Him!")

@module.rule(".*Windows\s10.*")
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
    "https://actionsack.com/img/wow/corrupt.gif",
    "https://actionsack.com/img/wow/wow!!.mp4",
    "https://actionsack.com/img/wow/wow.gif"
  ]
  bot.say(random.choice(wow))

@module.rule(".*whoa.*")
def whoa(bot, trigger):
  bot.say("https://actionsack.com/img/misc/whoa.gif")

@module.rule(".*wew\slad.*", ".*wew!.*")
@module.commands("wew")
def wew(bot, trigger):
  """wew lad! — Can also be triggered with 'wew!' or 'wew lad' anywhere in a message."""
  bot.say("https://actionsack.com/img/misc/wew.png")

@module.rule("^(uh\.\.\.|uh{2,})$")
def uhh(bot, trigger):
  uhh = [
    "https://actionsack.com/img/uh/uh01.png",
    "https://actionsack.com/img/uh/uh02.png",
    "https://actionsack.com/img/uh/uh03.png",
    "https://actionsack.com/img/uh/uh04.png",
    "https://actionsack.com/img/uh/uhbytes.png"
  ]
  bot.say(random.choice(uhh))

@module.rule(".*!!twerk.*")
def twerk(bot, trigger):
  twerkit = [
    "https://actionsack.com/img/twerk/ash.gif",
    "https://actionsack.com/img/twerk/nose.gif"
  ]
  bot.say(random.choice(twerkit))

@module.rule(".*swiggity\sswooty.*")
def swiggityswooty(bot, trigger):
  swiggity = [
    "https://actionsack.com/img/swiggityswooty/birb.gif",
    "https://actionsack.com/img/swiggityswooty/fatman.gif"
  ]
  bot.say(random.choice(swiggity))

@module.rule(".*praise\sthe\ssun.*")
@module.commands("praise")
def praisethesun(bot, trigger):
  """Praise the Sun!
  Can also be triggered with 'praise the sun' anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/praisethesun.webm")

@module.rule(".*#spam.*")
def spam(bot, trigger):
  bot.say("https://actionsack.com/img/misc/spam.png")

@module.rule("^son$")
@module.commands("son")
def son(bot, trigger):
  """Posts a 'don't talk to me or my son' meme.
  Can also be triggered by sending a message that is only the word 'son'."""
  son = [
    "https://actionsack.com/img/son/acnh.png",
    "https://actionsack.com/img/son/doggos.png",
    "https://actionsack.com/img/son/subs.png",
    "https://actionsack.com/img/son/teslas.png",
    "https://actionsack.com/img/son/wieners.png"
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

@module.rule(".*sex\srobot.*")
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
  bot.say("https://actionsack.com/img/xnaas/shaved.jpg")

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
  """fecktk tells us about his new house.
  Can also be triggered with '!newhouse' anywhere in a message."""
  bot.say("https://actionsack.com/img/fecktk/newhouse.png")

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
    "https://actionsack.com/img/cage/scream.gif",
    "https://actionsack.com/img/cage/side-to-side.gif",
    "https://actionsack.com/img/cage/wink.gif"
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
  bot.say("https://actionsack.com/img/misc/boom.gif")

@module.rule(".*burn!.*")
def burn(bot, trigger):
  bot.say("https://w.wiki/n9f")

@module.rule(".*bustin'.*")
@module.commands("bustin")
def bustin(bot, trigger):
  """Bustin' makes me feel good!
  Can also be triggered with "bustin'" anywhere in a message."""
  bot.say("https://actionsack.com/img/videos/bustin.webm")

@module.rule(".*(?<!s)canned(?!\sair).*")
def canned(bot, trigger):
  bot.say("https://actionsack.com/img/misc/canned.gif")

@module.rule(".*consider(\s|ed\s)this.*")
def consider(bot, trigger):
  bot.say("https://actionsack.com/img/misc/consider.png")

@module.rule(".*congraturaisins.*")
def congraturaisins(bot, trigger):
  bot.say("https://actionsack.com/img/misc/congraturaisins.png")

@module.rule(".*cowabunga.*")
def cowabunga(bot, trigger):
  bot.say("https://actionsack.com/img/misc/cowabunga.png")
