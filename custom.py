from sopel import plugin, formatting
import random
import unicodedata


@plugin.rule(".*!nod.*")
@plugin.command("nod")
def nod(bot, trigger):
    """Nod."""
    bot.say("https://p.actionsack.com/trek/nod.webp")


@plugin.rule(".*!spok.*")
@plugin.command("spok")
def spok(bot, trigger):
    """Summon SPOK into chat."""
    bot.say("https://p.actionsack.com/trek/spok.webp")


@plugin.rule(".*!cube.*")
@plugin.command("cube")
def trek_cube(bot, trigger):
    bot.say("https://p.actionsack.com/trek/cube.webp")


@plugin.rule(r"^Hello(\?|!)$")
def hi(bot, trigger):
    bot.say("Hello, {}!".format(trigger.nick))


@plugin.rule(r"^(Nice\.)(\s$|$)")
def nice(bot, trigger):
    bot.say(trigger.group(1))


@plugin.rule(r"^(This\sis\sThe\sWay\.)($|\s$)")
def theway(bot, trigger):
    bot.say(trigger.group(1))


@plugin.rule(r"^(It\sis\sknown\.)(\s$|$)")
def itisknown(bot, trigger):
    bot.say(trigger.group(1))


@plugin.rule("^yeah!$")
def yeah(bot, trigger):
    bot.say("https://p.actionsack.com/misc/yeah!.webp")


@plugin.rule("^retard.*")
def retarded(bot, trigger):
    retard = [
        "https://p.actionsack.com/retard/catarded.webp",
        "https://p.actionsack.com/retard/retarded.webp",
        "https://p.actionsack.com/retard/△.webp"
    ]
    bot.say(random.choice(retard))


@plugin.rule(".*rekt.*")
def rekt(bot, trigger):
    rekt = [
        "https://p.actionsack.com/rekt/baseball.gif",
        "https://p.actionsack.com/rekt/beachdive.mp4",
        "https://p.actionsack.com/rekt/beachskillz.gif",
        "https://p.actionsack.com/rekt/bf1revenge.mp4",
        "https://p.actionsack.com/rekt/bf1sniper.mp4",
        "https://p.actionsack.com/rekt/blackman.gif",
        "https://p.actionsack.com/rekt/botw-sled.gif",
        "https://p.actionsack.com/rekt/calligraphy.mp4",
        "https://p.actionsack.com/rekt/carcrash.gif",
        "https://p.actionsack.com/rekt/dive.gif",
        "https://p.actionsack.com/rekt/ForHonor.webm",
        "https://p.actionsack.com/rekt/gta-bike.mp4",
        "https://p.actionsack.com/rekt/gta-bounce.mp4",
        "https://p.actionsack.com/rekt/gta-cop.mp4",
        "https://p.actionsack.com/rekt/gta-flight.mp4",
        "https://p.actionsack.com/rekt/gta-gas.mp4",
        "https://p.actionsack.com/rekt/gta-phone.mp4",
        "https://p.actionsack.com/rekt/gta-post.mp4",
        "https://p.actionsack.com/rekt/gta-rekt.mp4",
        "https://p.actionsack.com/rekt/gta-stomp.gif",
        "https://p.actionsack.com/rekt/gta-walkitoff.mp4",
        "https://p.actionsack.com/rekt/jeep.gif",
        "https://p.actionsack.com/rekt/leap.gif",
        "https://p.actionsack.com/rekt/LOLOLOLOL.gif",
        "https://p.actionsack.com/rekt/poolgirl.gif",
        "https://p.actionsack.com/rekt/pubg-redzone.mp4",
        "https://p.actionsack.com/rekt/rekt.png",
        "https://p.actionsack.com/rekt/running.gif",
        "https://p.actionsack.com/rekt/skateit.mp4",
        "https://p.actionsack.com/rekt/slammin.gif",
        "https://p.actionsack.com/rekt/smash.mp4",
        "https://p.actionsack.com/rekt/sniped.mp4",
        "https://p.actionsack.com/rekt/walkbot.gif",
        "https://p.actionsack.com/rekt/watergun.gif",
        "https://w.wiki/n9f"
    ]
    bot.say(random.choice(rekt))


@plugin.rule("^420.*")
def fourtwenty(bot, trigger):
    fourtwozero = [
        "https://p.actionsack.com/420/attacks.webp",
        "https://p.actionsack.com/420/birb.webp",
        "https://p.actionsack.com/420/champions.webp",
        "https://p.actionsack.com/420/chinarocket.webp",
        "https://p.actionsack.com/420/claim.webp",
        "https://p.actionsack.com/420/coma.webp",
        "https://p.actionsack.com/420/commits.webp",
        "https://p.actionsack.com/420/comrade.webp",
        "https://p.actionsack.com/420/crewdragon.webp",
        "https://p.actionsack.com/420/doc.webp",
        "https://p.actionsack.com/420/dr.webp",
        "https://p.actionsack.com/420/exp.webp",
        "https://p.actionsack.com/420/gravityfalls.webp",
        "https://p.actionsack.com/420/highnoon-a.webp",
        "https://p.actionsack.com/420/highnoon.webp",
        "https://p.actionsack.com/420/lisa.webp",
        "https://p.actionsack.com/420/mowing.webp",
        "https://p.actionsack.com/420/old.webp",
        "https://p.actionsack.com/420/pikachu.webp",
        "https://p.actionsack.com/420/🍩.webp",
        "https://p.actionsack.com/420/pokemon.webp",
        "https://p.actionsack.com/420/realdanger.webp",
        "https://p.actionsack.com/420/replacements.webp",
        "https://p.actionsack.com/420/sealab.webp",
        "https://p.actionsack.com/420/telluhwat.webp",
        "https://p.actionsack.com/420/thomas.webp",
        "https://p.actionsack.com/420/thomasrust.webp",
        "https://p.actionsack.com/420/timesheet.webp",
        "https://p.actionsack.com/420/toasted.webp",
        "https://p.actionsack.com/420/toystory.webp",
        "https://p.actionsack.com/420/wednesday.webp"
    ]
    bot.say(random.choice(fourtwozero))


@plugin.rule(".*:retardeyes:.*")
def retardeyes(bot, trigger):
    bot.say("https://p.actionsack.com/emoji/retardeyes.webp")


@plugin.rule(".*:wesmart:.*")
def wesmart(bot, trigger):
    bot.say("https://p.actionsack.com/emoji/wesmart.webp")


@plugin.rule("^thx.*")
def thx(bot, trigger):
    bot.say("https://p.actionsack.com/thx/thx.png")


@plugin.rule(r"^(thanks|thank\syou).*")
def thanks(bot, trigger):
    thanks = [
        "https://p.actionsack.com/thx/h3h3.webm",
        "https://p.actionsack.com/thx/t.hanks.mp4",
        "https://p.actionsack.com/thx/thankyou.mp4"
    ]
    bot.say(random.choice(thanks))


@plugin.rule("^😢$")
@plugin.command("cry")
def crying(bot, trigger):
    """Bot will reply with a crying GIF or emoticon.
    Can also be summoned by sending a message that is only the 😢 emoji."""
    crying = [
        "https://p.actionsack.com/QQ/QQ000.webp",
        "https://p.actionsack.com/QQ/QQ001.webp",
        "https://p.actionsack.com/QQ/QQ002.webp",
        "https://p.actionsack.com/QQ/QQ003.webp",
        "https://p.actionsack.com/QQ/QQ004.webp",
        "https://p.actionsack.com/QQ/QQ005.webp",
        "https://p.actionsack.com/QQ/QQ006.webp",
        "https://p.actionsack.com/QQ/QQ007.webp",
        "ಥ_ಥ",
        "＞︿＜",
        "＞﹏＜",
        "X﹏X",
        "T_T"
    ]
    bot.say(random.choice(crying))


@plugin.rule(".*!pat(?!ch).*")
@plugin.command("pat")
def pat(bot, trigger):
    pat_gifs = [
        "https://p.actionsack.com/pat/00.gif",
        "https://p.actionsack.com/pat/01.gif",
        "https://p.actionsack.com/pat/02.gif",
        "https://p.actionsack.com/pat/03.gif",
        "https://p.actionsack.com/pat/04.gif",
        "https://p.actionsack.com/pat/05.gif"
    ]
    bot.say(random.choice(pat_gifs))


@plugin.rule(r".*cry\sme\sa\sriver.*")
def cryriver(bot, trigger):
    bot.say("https://p.actionsack.com/QQ/QQ007.webp")


@plugin.rule(".*!(xms|bge).*")
def xms(bot, trigger):
    bot.say("w2g.tv/rooms/actionsack-csurhbl9dkwvwnk91a")


@plugin.rule(".*📖.*")
def book(bot, trigger):
    book = [
        "https://p.actionsack.com/mike/📖/📖.gif",
        "https://p.actionsack.com/mike/📖/📖.jpg",
        "https://p.actionsack.com/mike/📖/📖+.jpg",
        "https://p.actionsack.com/mike/📖/📖🐇.jpg"
    ]
    bot.say(random.choice(book))


@plugin.rule("^8D$")
def greg(bot, trigger):
    bot.say("Greg was never in IRC...")


@plugin.rule("^grimm$")
def grim(bot, trigger):
    bot.say("Probably still showering with his sister to this day...")


@plugin.rule("^FOAD.*")
def foad(bot, trigger):
    bot.say("https://p.actionsack.com/misc/foad.png")


@plugin.rule(".*adapters.*")
def adapters(bot, trigger):
    adapters = [
        "https://p.actionsack.com/adapters/00.webp",
        "https://p.actionsack.com/adapters/01.webp",
        "https://p.actionsack.com/adapters/02.webp"
    ]
    bot.say(random.choice(adapters))


@plugin.rule(r".*accident\W")
def accident(bot, trigger):
    bot.say("https://p.actionsack.com/misc/accident.webp")


@plugin.rule(".*14nm.*")
def fourteennm(bot, trigger):
    bot.say("https://p.actionsack.com/misc/14nm+++++.mp4")


@plugin.rule(".*bait.*")
def bait(bot, trigger):
    bait = [
        "https://p.actionsack.com/bait/404bait.png",
        "https://p.actionsack.com/bait/all-bait.gif",
        "https://p.actionsack.com/bait/b8.png",
        "https://p.actionsack.com/bait/bai--what.png",
        "https://p.actionsack.com/bait/bait-g.gif",
        "https://p.actionsack.com/bait/bait-krunk.jpg",
        "https://p.actionsack.com/bait/bait-pole.png",
        "https://p.actionsack.com/bait/bait-sim.png",
        "https://p.actionsack.com/bait/bait-therapy.png",
        "https://p.actionsack.com/bait/bait.gif",
        "https://p.actionsack.com/bait/bait.png",
        "https://p.actionsack.com/bait/bait001.jpg",
        "https://p.actionsack.com/bait/bait002.png",
        "https://p.actionsack.com/bait/bait003.jpg",
        "https://p.actionsack.com/bait/bait004.jpg",
        "https://p.actionsack.com/bait/bait005.jpg",
        "https://p.actionsack.com/bait/bait006.png",
        "https://p.actionsack.com/bait/bait007.png",
        "https://p.actionsack.com/bait/bait008.png",
        "https://p.actionsack.com/bait/bait009.jpg",
        "https://p.actionsack.com/bait/bait010.jpg",
        "https://p.actionsack.com/bait/bait011.jpg",
        "https://p.actionsack.com/bait/bait012.jpg",
        "https://p.actionsack.com/bait/bait013.jpg",
        "https://p.actionsack.com/bait/bait014.jpg",
        "https://p.actionsack.com/bait/bait015.jpg",
        "https://p.actionsack.com/bait/bait016.jpg",
        "https://p.actionsack.com/bait/bait017.png",
        "https://p.actionsack.com/bait/bait018.png",
        "https://p.actionsack.com/bait/bait019.png",
        "https://p.actionsack.com/bait/bait020.jpg",
        "https://p.actionsack.com/bait/bait021.jpg",
        "https://p.actionsack.com/bait/bait022.png",
        "https://p.actionsack.com/bait/bait023.jpg",
        "https://p.actionsack.com/bait/bait024.jpg",
        "https://p.actionsack.com/bait/bait025.png",
        "https://p.actionsack.com/bait/bait026.png",
        "https://p.actionsack.com/bait/bait027.png",
        "https://p.actionsack.com/bait/baitkakke.jpg",
        "https://p.actionsack.com/bait/baitku.png",
        "https://p.actionsack.com/bait/baitnado.jpg",
        "https://p.actionsack.com/bait/baito.png",
        "https://p.actionsack.com/bait/changed-bait.jpg",
        "https://p.actionsack.com/bait/chosen-bait.png",
        "https://p.actionsack.com/bait/debait.png",
        "https://p.actionsack.com/bait/hq-bait.jpg",
        "https://p.actionsack.com/bait/MBGA.jpg",
        "https://p.actionsack.com/bait/mikes-bait.jpg",
        "https://p.actionsack.com/bait/poke-bait.png",
        "https://p.actionsack.com/bait/teach-bait.jpg",
        "https://p.actionsack.com/bait/whose-bait.jpg",
        "https://p.actionsack.com/bait/wtf-bait.jpg"
    ]
    bot.say(random.choice(bait))


@plugin.rule(".*backhand.*")
def backhand(bot, trigger):
    bot.say("https://p.actionsack.com/misc/backhand.mp4")


@plugin.rule("^😠$")
def angryeyes(bot, trigger):
    bot.say("https://p.actionsack.com/misc/angryeyes.webp")


@plugin.rule(".*alot.*")
def alot(bot, trigger):
    bot.say("https://p.actionsack.com/alot/")


@plugin.rule(".*♿.*")
def handicap(bot, trigger):
    bot.say("https://p.actionsack.com/♿/♿.mp4")


@plugin.rule(".*⤵️.*")
def down(bot, trigger):
    bot.say("https://p.actionsack.com/mike/down.gif")


@plugin.rule(r"^\.\.\.$")
def dotdotdot(bot, trigger):
    bot.say("...")


@plugin.rule(r".*deez\snutz.*")
@plugin.command("dz")
def deeznutz(bot, trigger):
    """Can also be triggered with "deez nutz" anywhere in a message."""
    deez_nutz = [
        formatting.bold("DEEZ NUTZ!"),
        "https://p.actionsack.com/nutz/aldeez.webp",
        "https://p.actionsack.com/nutz/dd.webp",
        "https://p.actionsack.com/nutz/dragon.webp",
        "https://p.actionsack.com/nutz/grandma.webp",
        "https://p.actionsack.com/nutz/prez.webp",
        "https://p.actionsack.com/nutz/wood.webp"
    ]
    bot.say(random.choice(deez_nutz))


@plugin.command("lenny", "rlenny")
def rlenny(bot, trigger):
    """Sends a random ( ͡° ͜ʖ ͡°) variation...or a GIF/MP4!"""
    rlenny = [
        "https://p.actionsack.com/lenny/anime.gif",
        "https://p.actionsack.com/lenny/crazy.mp4",
        "https://p.actionsack.com/lenny/spiral.gif",
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
        r"¯\_( ͡° ͜ʖ ͡°)_/¯",
        "(͡ ͡° ͜ つ ͡͡°)"
    ]
    bot.say(random.choice(rlenny))


@plugin.command("shrug")
def shrugc(bot, trigger):
    bot.say("¯\\_(ツ)_/¯")


@plugin.command("tableflip", "tflip")
def tableflip(bot, trigger):
    bot.say("(╯°□°）╯︵ ┻━┻")


@plugin.rule(r".*\(╯°□°）╯︵ ┻━┻.*")
def unflip(bot, trigger):
    bot.say("┬─┬﻿ ノ( ゜-゜ノ) — Please respect tables, {}.".format(trigger.nick))


@plugin.rule("^pranked!$")
def prank(bot, trigger):
    prank = [
        "https://p.actionsack.com/prank/prank01.png",
        "https://p.actionsack.com/prank/prank02.png"
    ]
    bot.say(random.choice(prank))


@plugin.rule(r"^\?{3,}$")
def que(bot, trigger):
    bot.say("https://p.actionsack.com/misc/¿¿¿.webp")


@plugin.rule(r"^\\o/$")
def handsup(bot, trigger):
    bot.say("\\o/")


@plugin.rule(r"^¯\\\_\(ツ\)_\/¯(\s$|$)")
def shrug(bot, trigger):
    bot.say("¯\\_(ツ)_/¯")


@plugin.rule(".*🦏.*")
def rhino(bot, trigger):
    bot.say("https://p.actionsack.com/🦏/🦏.webp")


@plugin.rule(".*🧀.*")
def cheese(bot, trigger):
    bot.say("https://p.actionsack.com/🧀/🧀.mp4")


@plugin.rule(".*🦄.*")
def unicorn(bot, trigger):
    bot.say("https://p.actionsack.com/🦄/🦄.webp")


@plugin.rule("^🙃$")
def upsidedown(bot, trigger):
    bot.say("🙃")


@plugin.rule("^🖕(|🏻|🏼|🏽|🏾|🏿)$")
def fuckyouback(bot, trigger):
    bot.say("Fuck you, {}!".format(trigger.nick))


@plugin.rule("^👏$")
def clap(bot, trigger):
    bot.say("👏🏻👏🏼👏🏽👏🏾👏🏿")


@plugin.rule("^👍$")
def thumbsup(bot, trigger):
    bot.say("👍🏻👍🏼👍🏽👍🏾👍🏿")


@plugin.rule("^👎$")
def thumbsdown(bot, trigger):
    bot.say("👎🏻👎🏼👎🏽👎🏾👎🏿")


@plugin.rule("^👌$")
def okhand(bot, trigger):
    bot.say("👌🏻👌🏼👌🏽👌🏾👌🏿")


@plugin.rule("^👋$")
def wave(bot, trigger):
    bot.say("👋🏻👋🏼👋🏽👋🏾👋🏿")


@plugin.rule("^🖖$")
def vulcansalute(bot, trigger):
    bot.say("🖖🏻🖖🏼🖖🏽🖖🏾🖖🏿")


@plugin.rule("^💪$")
def muscle(bot, trigger):
    bot.say("💪🏻💪🏼💪🏽💪🏾💪🏿")


@plugin.rule("^🤞$")
def crossed(bot, trigger):
    bot.say("🤞🏻🤞🏼🤞🏽🤞🏾🤞🏿")


@plugin.rule(".*(🌎|🌍|🌏).*")
def earthchan(bot, trigger):
    bot.say("https://p.actionsack.com/🌎/water.png")


@plugin.rule("^🐉$")
def dragon(bot, trigger):
    bot.say("https://p.xnaas.info/dragon.gif")


@plugin.rule("^🏈$")
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


@plugin.rule(r".*🍍(|\s)🍕.*")
def sin(bot, trigger):
    bot.say("This is a sin.")


@plugin.rule(".*xfiles.*")
def xfiles(bot, trigger):
    bot.say("Did you know that the X-Files is going to have 6 new episodes this summer on FOX, Aegisfate?")


@plugin.rule(".*triggered.*")
def triggered(bot, trigger):
    triggered = [
        "https://p.actionsack.com/triggered/beaker.webp",
        "https://p.actionsack.com/triggered/triggered.webp",
        "https://p.actionsack.com/triggered/feek.webp"
    ]
    bot.say(random.choice(triggered))


@plugin.rule(r".*to\sbe\sfair.*")
def tobefair(bot, trigger):
    bot.say("https://p.actionsack.com/v/tobefair.webm")


@plugin.rule(r".*stop\sbeing\spoor.*")
def stopbeingpoor(bot, trigger):
    bot.say("https://p.actionsack.com/misc/stopbeingpoor.jpg")


@plugin.rule(".*!tb.*")
@plugin.command("tb")
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
        "If I can just overclock the UNIX django, I can BASIC the DDOS root. Damn. No Dice. But wait...if I disencrypt their kilobytes with a backdoor handshake then...jackpot!"]
    bot.say(random.choice(tb), max_messages=2)


@plugin.command("jolly")
@plugin.rate(channel=21600)
def jolly(bot, trigger):
    """Nothing tops The Jolly Rancher story.
    Channel-wide rate limit of once every 6 hours."""
    bot.say("Nothing tops the Jolly Rancher story.")
    bot.say("Steve and his girlfriend Samantha went off to college in August. She went to Florida State, he went to Penn. So, she decides to fly to PA to visit him. He was really happy to see her so he decided to give her some oral action.")
    bot.say("He had done this numerous times before and he always enjoyed doing it...but for some reason, this time, she smelled really horrible, and she tasted even worse. He didn't want to offend her though because he hadn't seen her in months...so he put a Jolly Rancher in his mouth to cover it up, even though it didn't do much to help.")
    bot.say("In the course of eating her out, he accidentally pushed the candy inside of her... and stuck a finger in to grab it out. He took it out, and put it back into his mouth and bit it. Only...it wasn't the Jolly Rancher.")
    bot.say("It was a nodule of gonorrhea.")
    bot.say("As in, the blister-like structure that gonorrhea makes filled with diseased pus was the size of a fucking Jolly Rancher and the poor guy BIT it. I guess it was really dark in the room. He freaked out and started vomiting all over the place when it exploded in his mouth...")
    bot.say("He demanded to know what was going on, turns out she had cheated on him at a club like, the first week of college, and fucked some random guy and the stupid bitch had no clue what was wrong with her. She noticed a strange smell though.")
    bot.say("So now, Steve is freaking out that he now has gonorrhea of the mouth and God knows what else.")


@plugin.command("hg")
def hg(bot, trigger):
    """I've got the highground now!"""
    bot.say("https://p.actionsack.com/misc/highground.jpg")


@plugin.rule(".*!fgr.*")
@plugin.command("fgr")
def fgr(bot, trigger):
    """Family Guy reference!!!!!
    Can also be triggered with '!fgr' anywhere in a message."""
    fgr = [
        "https://p.actionsack.com/fgr/gay.jpg",
        "https://p.actionsack.com/fgr/gears.jpg",
        "https://p.actionsack.com/fgr/hang.gif",
        "https://p.actionsack.com/fgr/stewie-gun.jpg"
    ]
    bot.say(random.choice(fgr))


@plugin.rule(".*!adr.*")
@plugin.command("adr")
def adr(bot, trigger):
    """American Dad reference!
    Can also be triggered with '!adr' anywhere in a message."""
    bot.say("https://p.actionsack.com/fgr/ADR.jpg")


@plugin.rule(".*!csr.*")
@plugin.command("csr")
def csr(bot, trigger):
    """Cleveland Show reference!
    Can also be triggered with '!csr' anywhere in a message."""
    bot.say("https://p.actionsack.com/fgr/CSR.jpg")


@plugin.command("aegislive")
def aegislive(bot, trigger):
    """Aegisfate's YouTube livestream link."""
    bot.say("https://youtube.com/user/mac2486/live")

# === NSFW Commands ===


@plugin.rule(".*!!banebread.*")
def banebread(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/banebread.png")


@plugin.rule(".*!!bread.*")
def bread(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/🍞.png")


@plugin.rule(".*!!datascii.*")
def datascii(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/datascii.gif")


@plugin.rule(".*!!dickaroo.*")
def dickaroo(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/dickaroo.gif")


@plugin.rule(".*!!fgr.*")
def fgrnsfw(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/chris-in-brian.png")


@plugin.rule(".*!!ghostbabies.*")
def ghostbabies(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/ghostbabies.gif")


@plugin.rule(".*!!gimp.*")
def gimp(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/gimp.gif")


@plugin.rule(".*!!nazi.*")
def nazi(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/nazi.gif")


@plugin.rule(".*!!ponies.*")
def ponies(bot, trigger):
    bot.say("https://p.actionsack.com/nsfw/ponies.mp4")


@plugin.rule(".*!!jordan.*")
def jordan(bot, trigger):
    jordan = [
        "https://p.actionsack.com/jordan/ddosvariants.png",
        "https://p.actionsack.com/jordan/littledick.png"
    ]
    bot.say(random.choice(jordan))
# === NSFW Commands ===


@plugin.rule("^!b8$")
def beight(bot, trigger):
    bot.say("steam://install/567090")


@plugin.rule(".*!kristen.*")
def kristen(bot, trigger):
    kristen = [
        "https://p.actionsack.com/kristen/chainsmokers.png",
        "https://p.actionsack.com/kristen/keith.png",
        "https://p.actionsack.com/kristen/pidgey.png",
        "https://p.actionsack.com/kristen/pins.png",
        "https://p.actionsack.com/kristen/racist.png",
        "https://p.actionsack.com/kristen/rekt.png",
        "https://p.actionsack.com/kristen/repost.png",
        "https://p.actionsack.com/kristen/top.png"
    ]
    bot.say(random.choice(kristen))


@plugin.rule(r"^Tasian\sloves\spickles\.($|\s)")
def tasianpickles(bot, trigger):
    bot.say("https://p.actionsack.com/tasian/pickles.webp")


@plugin.rule(".*!asg.*")
@plugin.command("asg")
def allsystemsgo(bot, trigger):
    """Can also be triggered with "!asg" anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/asg.webp")


@plugin.rule(".*(murica|🍔).*")
@plugin.command("america")
def murica(bot, trigger):
    """Summons Freedom™ into chat.
    Can also be triggered with 'murica' anywhere in a message."""
    murica = [
        "https://p.actionsack.com/murica/clapping.mp4",
        "https://p.actionsack.com/murica/kiss.gif",
        "https://p.actionsack.com/murica/knockknock.gif",
        "https://p.actionsack.com/murica/freedomaf.mp4"
    ]
    bot.say(random.choice(murica))


@plugin.rule(".*!knock.*")
@plugin.command("knock")
def knock(bot, trigger):
    """RP: America knocks on your door...
    Can also be triggered with '!knock' anywhere in a message."""
    bot.say("https://p.actionsack.com/murica/knockknock.gif")


@plugin.command("pledge")
@plugin.rate(channel=5400)
def pledge(bot, trigger):
    """Say the United States Pledge of Allegiance.
    Channel-wide rate-limit of 90 minutes."""
    bot.say("I pledge allegiance to the flag of the United States of America. Thank you very very much for letting us little kids live here. It really really was nice of you. You didn't have to do it. And it's really not creepy to have little little kids mindlessly recite this anthem every day and pledge their life to a government before theyre old enough to really think about what they're saying.")
    bot.say("This is not a form of brainwashing. This is not a form of brainwashing. This is not a form of brainwashing.")
    bot.say("This is really the greatest country in the whole world. All the other countries suck. And if this country ever goes to go to war, as its often wont to do, I promise to help go and kill all the other country's kids.")
    bot.say("God bless Johnson & Johnson. God bless GE. God bless Citigroup.")


@plugin.rule(".*mushkin.*")
@plugin.rate(channel=5400)
def mushkin(bot, trigger):
    bot.say("Hey xnaas and feek, did you know that Mushkin announced a 4TB SSD for $500 at CES 2016 and never fuckin' delivered? How neat is that?")


@plugin.command("mirai")
def mirai(bot, trigger):
    """Gone but not forgotten, noble soviet bear."""
    bot.say("https://p.actionsack.com/putin/🐻.mp4")


@plugin.rule(".*!putin.*")
@plugin.command("putin")
def putin(bot, trigger):
    """Posts a Putin meme of some sort.
    Can also be triggered with '!putin' anywhere in a message."""
    putin = [
        "https://p.actionsack.com/putin/dance.mp4",
        "https://p.actionsack.com/putin/pigeon.mp4",
        "https://p.actionsack.com/putin/ritz.gif",
        "https://p.actionsack.com/putin/🐻.mp4"
    ]
    bot.say(random.choice(putin))


@plugin.command("aidsclub")
def aidsclub(bot, trigger):
    """Welcome to the club, loser."""
    bot.say("https://p.actionsack.com/misc/aidsclub.webp")


@plugin.rule(".*!barometer.*")
@plugin.command("barometer")
def barometer(bot, trigger):
    bot.say("https://p.actionsack.com/misc/barometer.webp")


@plugin.rule(r"^Oh,\syou!$")
def ohyou(bot, trigger):
    bot.say("https://p.actionsack.com/misc/Oh,you!.jpg")


@plugin.rule(".*!battletoad.*")
@plugin.command("battletoad")
def battletoad(bot, trigger):
    bot.say("https://p.actionsack.com/misc/battletoad.mp4")


@plugin.rule(".*!beaker.*")
@plugin.command("beaker")
def beaker(bot, trigger):
    bot.say("https://p.actionsack.com/misc/beaker.mp4")


@plugin.rule(".*!bomb.*")
@plugin.command("bomb")
def bomb(bot, trigger):
    """Bombs Japan again... :/
    Can also be triggered with '!bomb' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/bomb.mp4")


@plugin.rule(".*!broden.*")
@plugin.command("broden")
def broden(bot, trigger):
    bot.say("https://p.actionsack.com/misc/broden.mp4")


@plugin.rule(r".*mikey\sbikey.*")
def mikeybikey(bot, trigger):
    bot.say("https://p.actionsack.com/as/mikeybikey.png")


@plugin.rule(r".*meal\swith\sit.*")
def mealwithit(bot, trigger):
    bot.say("https://p.actionsack.com/deal/mealwithit.webp")


@plugin.rule(r".*deal\swith\sit.*")
def dealwithit(bot, trigger):
    deal = [
        "https://p.actionsack.com/deal/brule.webp",
        "https://p.actionsack.com/deal/coolkid.webp",
        "https://p.actionsack.com/deal/hippo.mp4",
        "https://p.actionsack.com/deal/mealwithit.webp",
        "https://p.actionsack.com/deal/spider.webp",
        "https://p.actionsack.com/deal/squirtle.webp",
        "https://p.actionsack.com/deal/tf2.webp"
    ]
    bot.say(random.choice(deal))


@plugin.rule(".*!mindjack.*")
def mindjack(bot, trigger):
    bot.say("https://p.actionsack.com/misc/mindjack.png")


@plugin.command("doge")
def doge(bot, trigger):
    """Doge memes! (There's not very many...)"""
    doge = [
        "https://p.actionsack.com/doge/batdoge.webp",
        "https://p.actionsack.com/doge/dogemine.webp",
        "https://p.actionsack.com/doge/skeledoge.webp"
    ]
    bot.say(random.choice(doge))


@plugin.rule(".*!dogemine.*")
def dogemine(bot, trigger):
    bot.say("https://p.actionsack.com/doge/dogemine.webp")


@plugin.rule(".*!skeledoge.*")
def skeledoge(bot, trigger):
    bot.say("https://p.actionsack.com/doge/skeledoge.webp")


@plugin.rule(".*!batdoge.*")
def batdoge(bot, trigger):
    bot.say("https://p.actionsack.com/doge/batdoge.webp")


@plugin.rule(r".*slow\sdown.*")
def slowdown(bot, trigger):
    bot.say("https://www.youtube.com/watch?v=fJdqw-JzW08")


@plugin.require_admin
@plugin.command("smmcb", "smd")
def smmcb(bot, trigger):
    bot.say("https://p.actionsack.com/misc/smmcb.gif")


@plugin.rule("^(noice)$")
def noice(bot, trigger):
    bot.say(trigger.group(1))


@plugin.rule(".*sockbot.*")
def sockbot(bot, trigger):
    sockbot = [
        "https://p.actionsack.com/sockbot/headsortails.png",
        "https://p.actionsack.com/sockbot/knife.png",
        "https://p.actionsack.com/sockbot/L337.png",
        "https://p.actionsack.com/sockbot/phone.png",
        "Gone, but not forgotten.",
        "Good riddance to Discord, but RIP Sockbot. 😢"
    ]
    bot.say(random.choice(sockbot))


@plugin.rule(".*!brony.*")
@plugin.command("brony")
def brony(bot, trigger):
    bot.say("https://p.actionsack.com/mike/brony.png")


@plugin.rule("^banned.*")
def banned(bot, trigger):
    banned = [
        "https://p.actionsack.com/banned/beetlejuice.mp4",
        "https://p.actionsack.com/banned/carryon.png",
        "https://p.actionsack.com/banned/clapping.gif",
        "https://p.actionsack.com/banned/hammer00.webp",
        "https://p.actionsack.com/banned/hammer01.webp",
        "https://p.actionsack.com/banned/hanging.gif",
        "https://p.actionsack.com/banned/samuel.gif",
        "https://p.actionsack.com/banned/slapbeavis.gif",
        "https://p.actionsack.com/banned/slap.gif",
        "https://p.actionsack.com/banned/tasian.gif",
        "https://p.actionsack.com/banned/trash.png",
        "https://p.actionsack.com/banned/trump.gif",
        "https://p.actionsack.com/banned/voodoo.png",
        "https://p.actionsack.com/banned/xbox.png",
        "https://p.actionsack.com/banned/xnaas.gif"
    ]
    bot.say(random.choice(banned))


@plugin.rule(".*boycott.*")
def boycott(bot, trigger):
    bot.say("https://p.actionsack.com/misc/boycott.webp")


@plugin.rule(".*censor.*")
def censor(bot, trigger):
    censor = [
        "https://p.actionsack.com/censored/bunny.webp",
        "https://p.actionsack.com/censored/censored.webp",
        "https://p.actionsack.com/censored/eyesored.webp",
        "https://p.actionsack.com/censored/fox.webp",
        "https://p.actionsack.com/censored/fren.webp",
        "https://p.actionsack.com/censored/nose.webp",
        "https://p.actionsack.com/censored/spider.webp",
        "https://p.actionsack.com/censored/tasian.webp"
    ]
    bot.say(random.choice(censor))


@plugin.rule("^(P|B|Ch|D|S|W)ing!$")
def pingpong(bot, trigger):
    bot.say("{}ong!".format(trigger.group(1)))


@plugin.rule("^Marco!$")
def marcopolo(bot, trigger):
    bot.say("Polo!")


@plugin.rule("^(W)ee!$")
def marcopolo(bot, trigger):
    bot.say("{}oo!".format(trigger.group(1)))


@plugin.rule(".*!work.*")
@plugin.command("work")
def worktoday(bot, trigger):
    """I don't really wanna do the work today..."""
    bot.say("https://p.actionsack.com/v/work.webm")


@plugin.rule(".*stbyn.*")
def stbyn(bot, trigger):
    bot.say("Sucks to be you, {}!".format(formatting.italic("nerd")))


@plugin.rule(".*🥓.*")
def bacon(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🥓.mp4")


@plugin.rule(".*🍜.*")
def soupbowl(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🍜.mp4")


@plugin.rule(".*🍞.*")
def breadchan(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🍞.png")


@plugin.rule(".*🎅(|🏻|🏼|🏽|🏾|🏿).*")
def santa(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🎅.png")


@plugin.rule(".*🎧.*")
def headphones(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🎧.png")


@plugin.rule(r".*fuck\syou(?!r).*")
def fuckyou(bot, trigger):
    fuckyou = [
        "https://p.actionsack.com/fuck/you/airline.webp",
        "https://p.actionsack.com/fuck/you/anime.mp4",
        "https://p.actionsack.com/fuck/you/ape.webp",
        "https://p.actionsack.com/fuck/you/aquaman.webp",
        "https://p.actionsack.com/fuck/you/arrow.webp",
        "https://p.actionsack.com/fuck/you/bb8.webp",
        "https://p.actionsack.com/fuck/you/bird.webp",
        "https://p.actionsack.com/fuck/you/bot.webp",
        "https://p.actionsack.com/fuck/you/buzz.webp",
        "https://p.actionsack.com/fuck/you/card.webp",
        "https://p.actionsack.com/fuck/you/climb.webp",
        "https://p.actionsack.com/fuck/you/compilation.webp",
        "https://p.actionsack.com/fuck/you/cutout.webp",
        "https://p.actionsack.com/fuck/you/deaf.webp",
        "https://p.actionsack.com/fuck/you/deer.webp",
        "https://p.actionsack.com/fuck/you/driving.webp",
        "https://p.actionsack.com/fuck/you/drums.webp",
        "https://p.actionsack.com/fuck/you/enthusiastic.webp",
        "https://p.actionsack.com/fuck/you/faoy.webp",
        "https://p.actionsack.com/fuck/you/friday.webp",
        "https://p.actionsack.com/fuck/you/fuku.webp",
        "https://p.actionsack.com/fuck/you/fur.webp",
        "https://p.actionsack.com/fuck/you/godzilla.webp",
        "https://p.actionsack.com/fuck/you/goldenboye.webp",
        "https://p.actionsack.com/fuck/you/grow.webp",
        "https://p.actionsack.com/fuck/you/h3h3.webp",
        "https://p.actionsack.com/fuck/you/hook.webp",
        "https://p.actionsack.com/fuck/you/jacket.webp",
        "https://p.actionsack.com/fuck/you/juliemao.webp",
        "https://p.actionsack.com/fuck/you/kraken.webp",
        "https://p.actionsack.com/fuck/you/loop.webp",
        "https://p.actionsack.com/fuck/you/marvel.webp",
        "https://p.actionsack.com/fuck/you/peaceamongworlds.webp",
        "https://p.actionsack.com/fuck/you/pigeon.webp",
        "https://p.actionsack.com/fuck/you/pocket.webp",
        "https://p.actionsack.com/fuck/you/pocketcat.webp",
        "https://p.actionsack.com/fuck/you/ragnarok.webp",
        "https://p.actionsack.com/fuck/you/rudy.webp",
        "https://p.actionsack.com/fuck/you/samuel.webp",
        "https://p.actionsack.com/fuck/you/samueltransparent.webp",
        "https://p.actionsack.com/fuck/you/sayan.webp",
        "https://p.actionsack.com/fuck/you/skating.webp",
        "https://p.actionsack.com/fuck/you/space_invader.webp",
        "https://p.actionsack.com/fuck/you/square.webp",
        "https://p.actionsack.com/fuck/you/tommydoor.webp",
        "https://p.actionsack.com/fuck/you/trumpet.webp",
        "https://p.actionsack.com/fuck/you/westworld.webp",
        "https://p.actionsack.com/fuck/you/ww-mib.webp",
        "https://p.actionsack.com/fuck/you/☂.webp"
    ]
    bot.say(random.choice(fuckyou))


@plugin.rule(r".*(gfy(?!c)|go\sfuck\syourself).*")
def gfy(bot, trigger):
    gfy = [
        "https://p.actionsack.com/fuck/urself/01_Two_Feet-Go_Fuck_Yourself.ogg",
        "https://p.actionsack.com/fuck/urself/anime.webp",
        "https://p.actionsack.com/fuck/urself/arms.webp",
        "https://p.actionsack.com/fuck/urself/disney.webp",
        "https://p.actionsack.com/fuck/urself/doggo.webp",
        "https://p.actionsack.com/fuck/urself/gay.webp",
        "https://p.actionsack.com/fuck/urself/gfy.webp",
        "https://p.actionsack.com/fuck/urself/rugrats.webp",
        "https://p.actionsack.com/fuck/urself/science.webp"]
    bot.say(random.choice(gfy))


@plugin.rule(r"^What\sthe\sfuck\?$")
def wtfquestion(bot, trigger):
    bot.say("https://p.actionsack.com/wtf/wtf¿.gif")


@plugin.rule(r"^What\sthe\sfuck!$")
def wtfexclamation(bot, trigger):
    bot.say("https://p.actionsack.com/wtf/wtfh3h3.mp4")


@plugin.rule("^Fuck!$")
def fuckexclamation(bot, trigger):
    bot.say("https://p.actionsack.com/fuck/fuck!.webp")


@plugin.rule(r"^Fuck\syeah!$")
def fuckyeah(bot, trigger):
    bot.say("https://p.actionsack.com/fuck/fuckyeah!.webp")


@plugin.rule(r".*fuck\severything.*")
def fuckeverything(bot, trigger):
    bot.say("https://p.actionsack.com/fuck/fuckeverything.webp")


@plugin.rule(".*ftge.*")
def ftge(bot, trigger):
    ftge = [
        "https://p.actionsack.com/fuck/ftge-a.webp",
        "https://p.actionsack.com/fuck/ftge.webp"
    ]
    bot.say(random.choice(ftge))


@plugin.rule(r".*fooled\syou.*")
def fooledyou(bot, trigger):
    bot.say("https://p.actionsack.com/misc/fooled.png")


@plugin.rule(r".*fite\sme.*")
def fiteme(bot, trigger):
    fiteme = [
        "https://p.actionsack.com/fite/cat.gif",
        "https://p.actionsack.com/fite/phones.gif",
        "https://p.actionsack.com/fite/🌮.gif"
    ]
    bot.say(random.choice(fiteme))


@plugin.rule(r"^Found\sout\sI\'m\sgay(|\.|\s)$")
@plugin.rate(channel=21600)
def fagexclamation(bot, trigger):
    bot.say("You're gay. Hey poofta. You're a homo. You're a homo you faggot. Go suck a dick. Go suck a real big dick. Get those dick so far in your mouth that the dick's right there, you got 'em all the way, smashing the back of your throat, balls right there, bangin' on your chin. That's how much I want you to suck dick. Oi. This is me. Pretending to be you. Fist-fuckin' another man in the asshole. Just fist-fuckin' the god-givin' shit out of him. I bet you like that so much you'd like to get fist-fucked while you're doing it. Just getting fist-fucked while you're fist-fuckin' someone else. While you're at it chuck in another one. Just fist-fuckin' two strange men, getting your asshole fist-fucked with someone you just met on Grinder. I bet you wish these were dicks. I bet you wish these were big floppy dicks. You're in a big forest of dicks. Getting dicks all over ya. Covering yourself in cum. Loving cum. Can I suck your dick? Can I suck your dick and then kiss you? Kiss you square on the mouth and then fuck you? Scratch that. Can we make love? Can we make love in my bedroom and then maybe if we connect on more than just a physical level, I'll take you out, I'll introduce you to my mum and my dad and my little sister Jennifer, she's really cool. She's into Goosebumps at the moment. And then maybe we can all go out for dinner together. And they'll really like you because of your cool taste in music and your wonderful dress sense. And then maybe, after confronting their initial misguided preconceptions, my family will come to respect our love for its tangibility. And they'll reject it because of bias or religious and political agendas of hate that have been weaved through the social fabric of hundreds and hundreds of years. FAGGOT!!!", max_messages=6)


@plugin.rule(".*fags.*")
def fags(bot, trigger):
    bot.say("https://p.actionsack.com/faggot/fags.png")


@plugin.rule(".*fag(?!s).*")
def faggot(bot, trigger):
    faggot = [
        "https://p.actionsack.com/faggot/faggot.gif",
        "https://p.actionsack.com/faggot/oh.gif",
        "https://p.actionsack.com/faggot/urafaget.png",
        "Faggot!",
        "(/¯◡ ‿ ◡)/¯ ~~~~ Abracadabra, you're a faggot!"
    ]
    bot.say(random.choice(faggot))


@plugin.rule("^Gay!$")
def gayexclamation(bot, trigger):
    gayexclamation = [
        "https://p.actionsack.com/gay/!.webp",
        "https://p.actionsack.com/gay/sayshere.webp",
        "https://p.actionsack.com/gay/shit.webp"
    ]
    bot.say(random.choice(gayexclamation))


@plugin.rule(r".*everything's\sfucked.*")
def everythingsfucked(bot, trigger):
    bot.say("https://p.actionsack.com/misc/everythingsfucked.gif")


@plugin.rule(r"^o\sshit.*")
def datboi(bot, trigger):
    oshit = [
        "https://p.actionsack.com/oshit/8ball.png",
        "https://p.actionsack.com/oshit/actorboi.gif",
        "https://p.actionsack.com/oshit/bikeboi.gif",
        "https://p.actionsack.com/oshit/boistory3.png",
        "https://p.actionsack.com/oshit/busboi.png",
        "https://p.actionsack.com/oshit/darksouls.png",
        "https://p.actionsack.com/oshit/datboi.gif",
        "https://p.actionsack.com/oshit/deadboi.gif",
        "https://p.actionsack.com/oshit/edgy.png",
        "https://p.actionsack.com/oshit/fallen.png",
        "https://p.actionsack.com/oshit/fancy.png",
        "https://p.actionsack.com/oshit/fastboi.gif",
        "https://p.actionsack.com/oshit/fellow.png",
        "https://p.actionsack.com/oshit/ghostboi.png",
        "https://p.actionsack.com/oshit/greninja.png",
        "https://p.actionsack.com/oshit/haramboi.png",
        "https://p.actionsack.com/oshit/IRL.png",
        "https://p.actionsack.com/oshit/iWish.png",
        "https://p.actionsack.com/oshit/jewboi.png",
        "https://p.actionsack.com/oshit/komradboi.png",
        "https://p.actionsack.com/oshit/lasthope.png",
        "https://p.actionsack.com/oshit/milkshake.png",
        "https://p.actionsack.com/oshit/mortyboi.png",
        "https://p.actionsack.com/oshit/movie.png",
        "https://p.actionsack.com/oshit/newboi.png",
        "https://p.actionsack.com/oshit/news.png",
        "https://p.actionsack.com/oshit/objectionboi.png",
        "https://p.actionsack.com/oshit/origin.gif",
        "https://p.actionsack.com/oshit/pajamaboi.png",
        "https://p.actionsack.com/oshit/playboi.png",
        "https://p.actionsack.com/oshit/poolboi.png",
        "https://p.actionsack.com/oshit/poster.png",
        "https://p.actionsack.com/oshit/realluke.png",
        "https://p.actionsack.com/oshit/reasons.png",
        "https://p.actionsack.com/oshit/sexboi.png",
        "https://p.actionsack.com/oshit/shiningboi.png",
        "https://p.actionsack.com/oshit/starwars.png",
        "https://p.actionsack.com/oshit/suicideboi.png",
        "https://p.actionsack.com/oshit/sweater.png",
        "https://p.actionsack.com/oshit/teamboi.png",
        "https://p.actionsack.com/oshit/towers.png",
        "https://p.actionsack.com/oshit/trumpboi.png",
        "https://p.actionsack.com/oshit/warriorboi.png",
        "https://p.actionsack.com/oshit/wat.png",
        "https://p.actionsack.com/oshit/woodwork.png"
    ]
    bot.say(random.choice(oshit))


@plugin.command("spl")
def smitepro(bot, trigger):
    """YouTube and Twitch links for the Smite Pro League stream."""
    bot.say("YT: youtube.com/user/smitegame/live | Twitch: twitch.tv/smitegame")


@plugin.rule(".*!xmas.*")
@plugin.command("xmas")
def xmassong(bot, trigger):
    """The only good Christmas song.
    Can also be triggered with '!xmas' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/xmas.webm")


@plugin.rule(".*!swat.*")
@plugin.command("swat")
def swat(bot, trigger):
    """Summon SWAT into chat.
    Can also be triggered with '!swat' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/SWAT.mp4")


@plugin.rule(".*(▫|◽|◻|⬜|▪|◾|◼|⬛|🟥|🟧|🟨|🟩|🟦|🟪|🟫).*")
def square(bot, trigger):
    bot.say("https://p.actionsack.com/v/square.mp4")


@plugin.command("dblflip")
def dblflip(bot, trigger):
    """Flip two tables...at the same time!"""
    bot.say("┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻")


@plugin.rule(r".*bite\sme.*")
@plugin.require_chanmsg
def bitesback(bot, trigger):
    bot.action("bites {}".format(trigger.nick))


@plugin.rule("^Bye!$")
def byebye(bot, trigger):
    bot.say("https://p.actionsack.com/misc/BYE!.webp")


@plugin.command("cb")
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
        "What This Man Learned From Having Sex With 365 Guys In One Year"]
    bot.say(random.choice(clickbait))


@plugin.rule(".*COVID19!.*")
def windofgod(bot, trigger):
    bot.say("https://p.actionsack.com/v/windofgod.webm")


@plugin.rule(".*crossfit.*")
def crossfit(bot, trigger):
    bot.say("https://p.actionsack.com/v/crossfit.webm")


@plugin.rule("^dang$")
def dang(bot, trigger):
    bot.say("https://p.actionsack.com/misc/dang.jpg")


@plugin.command("dbc")
def dbc(bot, trigger):
    """Post a Dragonbro Chi comic."""
    dbc = [
        "https://p.actionsack.com/dbc/dbc01.png",
        "https://p.actionsack.com/dbc/dbc02.png",
        "https://p.actionsack.com/dbc/dbc03.png",
        "https://p.actionsack.com/dbc/dbc04.png",
        "https://p.actionsack.com/dbc/dbc07.png",
        "https://p.actionsack.com/dbc/dbc08.png",
        "https://p.actionsack.com/dbc/dbc09.png",
        "https://p.actionsack.com/dbc/dbc10.png"
    ]
    bot.say(random.choice(dbc))


@plugin.rule(r"^Deus\svult!$")
def deusvult(bot, trigger):
    bot.say("https://p.actionsack.com/v/deusvult.webm")


@plugin.rule(".*fake!.*")
@plugin.command("fake")
def fake(bot, trigger):
    """For when something is super fake.
    Can also be triggered with 'fake!' anywhere in a message."""
    fake = [
        "https://p.actionsack.com/fake/faux.png",
        "https://p.actionsack.com/fake/kazoo.gif"
    ]
    bot.say(random.choice(fake))


@plugin.rule(".*!erect.*")
@plugin.command("erect")
def erect(bot, trigger):
    """Classic Krieger GIF.
    Can also be triggered with '!erect' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/erect.gif")


@plugin.rule(".*GOAT!.*")
@plugin.command("goat")
def goat(bot, trigger):
    """Greatest of all time!
    Can also be triggered with 'GOAT!' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/GOAT.webm")


@plugin.rule("^hackers$")
@plugin.command("hackers")
def hackers(bot, trigger):
    """Summons the world's two greatest hackers.
    Can also be summoned without the preceeding period/full stop."""
    bot.say("https://p.actionsack.com/as/hackers.png")


@plugin.rule("^hue.*")
def hue(bot, trigger):
    hue = [
        "https://p.actionsack.com/hue/bots.gif",
        "https://p.actionsack.com/hue/bus.gif",
        "https://p.actionsack.com/hue/cat.gif",
        "https://p.actionsack.com/hue/combo.gif",
        "https://p.actionsack.com/hue/drhue.gif",
        "https://p.actionsack.com/hue/drhueves.gif",
        "https://p.actionsack.com/hue/horse.gif",
        "https://p.actionsack.com/hue/huemanatee.gif",
        "https://p.actionsack.com/hue/hueppo.gif",
        "https://p.actionsack.com/hue/jellyfish.gif",
        "https://p.actionsack.com/hue/kitten.gif",
        "https://p.actionsack.com/hue/mike.gif",
        "https://p.actionsack.com/hue/owls.gif",
        "https://p.actionsack.com/hue/sdc.gif"
    ]
    bot.say(random.choice(hue))


@plugin.rule(r"^I am the machine\.(\s$|$)")
def iamthemachine(bot, trigger):
    bot.say("https://www.youtube.com/watch?v=8PAtFsJY5q0")


@plugin.rule(r".*I\scan't\seven.*", r".*I'm\sliterally\scan't\seven.*")
def icanteven(bot, trigger):
    bot.say("https://p.actionsack.com/v/icanteven.webm")


@plugin.rule(r"^I\sship\s(it|that).*")
def ishipit(bot, trigger):
    bot.say("https://p.actionsack.com/misc/fedex.webp")


@plugin.rule(".*idgaf.*")
def idgaf(bot, trigger):
    idgaf = [
        "https://p.actionsack.com/idgaf/20thcentury.webp",
        "https://p.actionsack.com/idgaf/nophux.webp"
    ]
    bot.say(random.choice(idgaf))


@plugin.rule(r".*hugh\smungus.*")
def hughmungus(bot, trigger):
    bot.say("https://p.actionsack.com/v/hughmungus.webm")


@plugin.rule(".*IMDABES.*")
def imdabes(bot, trigger):
    bot.say("https://p.actionsack.com/v/IMDABES.webm")


@plugin.rule(".*!JPEG.*")
@plugin.command("jpeg")
def jpeg(bot, trigger):
    """Do I look like I know what a JPEG is?
    Can also be triggered with '!JPEG' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/JPEG.webm")


@plugin.rule(".*!kazoo.*")
@plugin.command("kazoo")
def kazoo(bot, trigger):
    """Kaaazzzzoooooooooo!!!
    Can also be triggered with '!kazoo' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/kazoo.webm")


@plugin.rule(r"^kill\sme.*")
def killme(bot, trigger):
    killme = [
        "https://p.actionsack.com/killme/bulb.webp",
        "https://p.actionsack.com/killme/char.webp",
        "https://p.actionsack.com/killme/pika.webp",
    ]
    bot.say(random.choice(killme))


@plugin.rule(r".*((?<!\w)k(y|m)s(?!\w)|kill\syourself).*")
def kys(bot, trigger):
    kys = [
        "https://p.actionsack.com/kys/deals.webp",
        "https://p.actionsack.com/kys/elmo.webp",
        "https://p.actionsack.com/kys/gift.webp",
        "https://p.actionsack.com/kys/gta.webp",
        "https://p.actionsack.com/kys/hang.webp",
        "https://p.actionsack.com/kys/howto.webp",
        "https://p.actionsack.com/kys/iGuess.webp",
        "https://p.actionsack.com/kys/ike.webp",
        "https://p.actionsack.com/kys/kys.webp",
        "https://p.actionsack.com/kys/mike-pepe.webp",
        "https://p.actionsack.com/kys/mike.webp",
        "https://p.actionsack.com/kys/music.webp",
        "https://p.actionsack.com/kys/ohhai.webp",
        "https://p.actionsack.com/kys/pasta.webp",
        "https://p.actionsack.com/kys/pepe.webp",
        "https://p.actionsack.com/kys/peter-joe.webp",
        "https://p.actionsack.com/kys/peter.webp",
        "https://p.actionsack.com/kys/puft.webp",
        "https://p.actionsack.com/kys/tried.webp",
        "https://p.actionsack.com/kys/wendys.webp",
        "https://p.actionsack.com/kys/window.webp",
        "https://lostallhope.com/"
    ]
    bot.say(random.choice(kys))


@plugin.rule(".*!music.*")
def listentomusic(bot, trigger):
    bot.say("https://p.actionsack.com/kys/music.webp")


@plugin.rule(r"^oh\shai.*")
def ohhai(bot, trigger):
    bot.say("https://p.actionsack.com/kys/ohhai.webp")


@plugin.rule(".*legal!.*")
@plugin.command("legal")
def legal(bot, trigger):
    """100% totally legal!
    Can also be triggered with 'legal!' anywhere in a message."""
    legal = [
        "https://p.actionsack.com/misc/👍LEGAL👍.mp4",
        "https://p.actionsack.com/misc/🕺LEGAL🕺.mp4"
    ]
    bot.say(random.choice(legal))


@plugin.command("judge")
@plugin.require_chanmsg
def judge(bot, trigger):
    """Judge someone or something."""
    judges = [
        "not guilty! https://p.actionsack.com/misc/not-guilty.png",
        "guilty! https://p.actionsack.com/misc/guilty.png"
    ]
    text = formatting.plain(trigger.group(2))

    if not text:
        try:
            msg = "I need someone or something to judge!"
        except KeyError:
            msg = "How did you do that?!"
        bot.reply(msg)
        return

    bot.say("{} is {}".format(text, random.choice(judges)))


@plugin.rule(r"^wat($|\W)")
def wat(bot, trigger):
    wat = [
        "https://p.actionsack.com/wat/3wats.webp",
        "https://p.actionsack.com/wat/65wat.webp",
        "https://p.actionsack.com/wat/emma.webp",
        "https://p.actionsack.com/wat/filming.webp",
        "https://p.actionsack.com/wat/gigawat.webp",
        "https://p.actionsack.com/wat/holdwat.webp",
        "https://p.actionsack.com/wat/hwat02.webp",
        "https://p.actionsack.com/wat/inthebutt.webp",
        "https://p.actionsack.com/wat/jabba.webp",
        "https://p.actionsack.com/wat/jaja.webp",
        "https://p.actionsack.com/wat/jjwat.webp",
        "https://p.actionsack.com/wat/konichiwat.webp",
        "https://p.actionsack.com/wat/olde.webp",
        "https://p.actionsack.com/wat/police.webp",
        "https://p.actionsack.com/wat/slipwat.webp",
        "https://p.actionsack.com/wat/space.webp",
        "https://p.actionsack.com/wat/subwat.webp",
        "https://p.actionsack.com/wat/swat.webp",
        "https://p.actionsack.com/wat/watchdogs.webp",
        "https://p.actionsack.com/wat/watduel.webp",
        "https://p.actionsack.com/wat/waterworld.webp",
        "https://p.actionsack.com/wat/wathusky.webp",
        "https://p.actionsack.com/wat/watif.webp",
        "https://p.actionsack.com/wat/watinthehat.webp",
        "https://p.actionsack.com/wat/watislove.webp",
        "https://p.actionsack.com/wat/watmouth.webp",
        "https://p.actionsack.com/wat/wat.webp",
        "https://p.actionsack.com/wat/watshake.webp",
        "https://p.actionsack.com/wat/watwatwatwat.webp",
        "https://p.actionsack.com/wat/wow.webp"
    ]
    bot.say(random.choice(wat))


@plugin.rule(".*✝.*")
def praisejesus(bot, trigger):
    bot.say("Praise Jesus!")


@plugin.rule(r".*jesus\schrist.*")
def jesuschrist(bot, trigger):
    bot.say("Praise Him!")


@plugin.rule(r".*Windows\s10.*")
@plugin.command("w10")
def windowsten(bot, trigger):
    """Windows 10 bad.
    Can also be triggered with 'Windows 10' anywhere in a message."""
    w10 = [
        "https://p.actionsack.com/W10/game.png",
        "https://p.actionsack.com/W10/pubg.webm",
        "https://p.actionsack.com/W10/stuck.png",
        "https://p.actionsack.com/W10/updates.webm"
    ]
    bot.say(random.choice(w10))


@plugin.rule(".*!wizard.*", ".*wazard.*")
@plugin.command("wizard")
def wazard(bot, trigger):
    """Hagrid tells you what you are.
    Can also be triggered with '!wizard' or 'wazard' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/wazard.mp4")


@plugin.rule(".*wow!.*")
@plugin.command("wow")
def wow(bot, trigger):
    """Wow! — Can also be triggered with 'wow!' anywhere in a message."""
    wow = [
        "https://p.actionsack.com/wow/corrupt.webp",
        "https://p.actionsack.com/wow/wow!!.mp4",
        "https://p.actionsack.com/wow/wow.webp"
    ]
    bot.say(random.choice(wow))


@plugin.rule(".*whoa.*")
def whoa(bot, trigger):
    bot.say("https://p.actionsack.com/misc/whoa.webp")


@plugin.rule(r".*wew\slad.*", ".*wew!.*")
@plugin.command("wew")
def wew(bot, trigger):
    """wew lad! — Can also be triggered with 'wew!' or 'wew lad' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/wew.webp")


@plugin.rule(r"^(uh\.\.\.|uh{2,})$")
def uhh(bot, trigger):
    uhh = [
        "https://p.actionsack.com/uh/uh01.webp",
        "https://p.actionsack.com/uh/uh02.webp",
        "https://p.actionsack.com/uh/uh03.webp",
        "https://p.actionsack.com/uh/uh04.webp",
        "https://p.actionsack.com/uh/uhbytes.webp"
    ]
    bot.say(random.choice(uhh))


@plugin.rule(".*!!twerk.*")
def twerk(bot, trigger):
    twerkit = [
        "https://p.actionsack.com/twerk/ash.gif",
        "https://p.actionsack.com/twerk/nose.gif"
    ]
    bot.say(random.choice(twerkit))


@plugin.rule(r".*swiggity\sswooty.*")
def swiggityswooty(bot, trigger):
    swiggity = [
        "https://p.actionsack.com/swiggityswooty/birb.gif",
        "https://p.actionsack.com/swiggityswooty/fatman.gif"
    ]
    bot.say(random.choice(swiggity))


@plugin.rule(r".*praise\sthe\ssun.*")
@plugin.command("praise")
def praisethesun(bot, trigger):
    """Praise the Sun!
    Can also be triggered with 'praise the sun' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/praisethesun.webm")


@plugin.rule(".*#spam.*")
def spam(bot, trigger):
    bot.say("https://p.actionsack.com/misc/spam.png")


@plugin.rule(".*!son.*")
@plugin.command("son")
def son(bot, trigger):
    """Posts a "don't talk to me or my son" meme/image.
    Can also be triggered with "!son" anywhere in a message."""
    son = [
        "https://p.actionsack.com/son/acnh.webp",
        "https://p.actionsack.com/son/chiefs.webp",
        "https://p.actionsack.com/son/doggos.webp",
        "https://p.actionsack.com/son/halo.webp",
        "https://p.actionsack.com/son/subs.webp",
        "https://p.actionsack.com/son/teslas.webp",
        "https://p.actionsack.com/son/wieners.webp"
    ]
    bot.say(random.choice(son))


@plugin.rule("^sh{2,}$")
def shh(bot, trigger):
    shhh = [
        "https://p.actionsack.com/shh/clouds.jpg",
        "https://p.actionsack.com/shh/eardrums.mp4",
        "https://p.actionsack.com/shh/ninjagaiden.png",
        "https://p.actionsack.com/shh/stfub.mp4",
        "https://p.actionsack.com/shh/tlou.jpg"
    ]
    bot.say(random.choice(shhh))


@plugin.rule(r".*sex\srobot.*")
def sexrobot(bot, trigger):
    bot.say("https://p.actionsack.com/misc/sexrobot.gif")


@plugin.rule(".*!stickers.*")
@plugin.command("stickers")
def stickers(bot, trigger):
    """Well-known fact: each sticker on your car adds 5 horsepower.
    Can also be triggered with '!stickers' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/stickers.gif")


@plugin.command("shaved")
def shaved(bot, trigger):
    """xnaas' beautiful shaved leg circa 2011."""
    bot.say("https://p.actionsack.com/xnaas/shaved.webp")


@plugin.rule(".*!rimshot.*")
@plugin.command("rimshot")
def rimshot(bot, trigger):
    """Replies with a 'rimshot' GIF.
    Can also be triggered with '!rimshot' anywhere in a message."""
    rim_shot = [
        "https://p.actionsack.com/rimshot/effects.gif",
        "https://p.actionsack.com/rimshot/fgr.gif",
        "https://p.actionsack.com/rimshot/mlp.gif",
        "https://p.actionsack.com/rimshot/rimshot.gif"
    ]
    bot.say(random.choice(rim_shot))


@plugin.rule(".*!newhouse.*")
@plugin.command("newhouse")
def newhouse(bot, trigger):
    """Can also be triggered with '!newhouse' anywhere in a message."""
    bot.say("https://p.actionsack.com/fecktk/newhouse.webp")


@plugin.rule(".*!drone.*")
@plugin.command("drone")
def drone(bot, trigger):
    """Summons a drone into chat.
    Can also be summoned with '!drone' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/drone.webm")


@plugin.rule(".*!cage.*")
@plugin.command("cage")
def nickcage(bot, trigger):
    """Summons Nicolas Cage into chat.
    Can also be summoned with '!cage' anywhere in a message."""
    nick_cage = [
        "https://p.actionsack.com/cage/scream.webp",
        "https://p.actionsack.com/cage/side-to-side.webp",
        "https://p.actionsack.com/cage/wink.webp"
    ]
    bot.say(random.choice(nick_cage))


@plugin.rule(".*!va.*")
@plugin.command("va")
@plugin.rate(user=900)
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
        "https://p.actionsack.com/misc/'voiceactor'.png"]
    bot.say(random.choice(voice_actor), max_messages=3)


@plugin.rule(".*!baby.*")
@plugin.command("baby")
def baby(bot, trigger):
    """Posts an image of GIF involving babies.
    WARNING: not a cutesy command.
    Can also be triggered with '!baby' anywhere in a message."""
    baby_pics = [
        "https://p.actionsack.com/baby/inflammable.gif",
        "https://p.actionsack.com/baby/man.png",
        "https://p.actionsack.com/baby/prayfor.png",
        "https://p.actionsack.com/baby/rolling.gif",
        "https://p.actionsack.com/baby/spider.gif"
    ]
    bot.say(random.choice(baby_pics))


@plugin.rule(".*boom!.*")
@plugin.command("boom")
def boom(bot, trigger):
    """BOOM! — Can also be triggered with 'boom!' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/boom.webp")


@plugin.rule(".*burn!.*")
def burn(bot, trigger):
    bot.say("https://w.wiki/n9f")


@plugin.rule(".*bustin'.*")
@plugin.command("bustin")
def bustin(bot, trigger):
    """Bustin' makes me feel good!
    Can also be triggered with "bustin'" anywhere in a message."""
    bot.say("https://p.actionsack.com/v/bustin.webm")


@plugin.rule(r".*(?<!s)canned(?!\sair).*")
def canned(bot, trigger):
    bot.say("https://p.actionsack.com/misc/canned.gif")


@plugin.rule(r".*consider(\s|ed\s)this.*")
def consider(bot, trigger):
    bot.say("https://p.actionsack.com/misc/consider.webp")


@plugin.rule(".*congraturaisins.*")
def congraturaisins(bot, trigger):
    bot.say("https://p.actionsack.com/misc/congraturaisins.png")


@plugin.rule(".*cowabunga.*")
def cowabunga(bot, trigger):
    bot.say("https://p.actionsack.com/misc/cowabunga.png")


@plugin.rule(".*correct!.*")
def correcthorse(bot, trigger):
    bot.say("https://p.actionsack.com/misc/correct!.gif")


@plugin.rule(".*centaur.*")
def centaur(bot, trigger):
    bot.say("https://p.actionsack.com/misc/centaur.png")


@plugin.rule(".*(!dance|dance!).*")
@plugin.command("dance")
def dance(bot, trigger):
    """Posts a dancing GIF.
    Can also be triggered with 'dance!' or '!dance' anywhere in a message."""
    dance_gifs = [
        "https://p.actionsack.com/dance/arms.gif",
        "https://p.actionsack.com/dance/arthur.gif",
        "https://p.actionsack.com/dance/bunny.gif",
        "https://p.actionsack.com/dance/frankie.gif",
        "https://p.actionsack.com/dance/gijoe.gif",
        "https://p.actionsack.com/dance/guy.gif",
        "https://p.actionsack.com/dance/jontron.gif",
        "https://p.actionsack.com/dance/skeleton.gif"
    ]
    bot.say(random.choice(dance_gifs))


@plugin.command("doomanimal")
def doomanimal(bot, trigger):
    """Posts "DOOMANIMAL" video by @andmish."""
    bot.say("https://p.actionsack.com/v/DOOMANIMAL.webm")


@plugin.command("doomcrossing")
def doomcrossing(bot, trigger):
    """Posts "DOOM CROSSING: Eternal Horizons" by The Chalkeaters feat. Natalia Natchan."""
    bot.say("https://p.actionsack.com/v/DOOMCROSSING.webm")


@plugin.rule(r".*doom\sguy.*")
def doomguy(bot, trigger):
    bot.say("https://p.actionsack.com/misc/doomguy.webp")


@plugin.rule(".*grapist.*")
def grapist(bot, trigger):
    bot.say("https://p.actionsack.com/misc/grapist.gif")


@plugin.rule(r".*it\swas\sme(?!ant).*")
def itwasme(bot, trigger):
    me_dio = [
        "https://p.actionsack.com/dio/dva.png",
        "https://p.actionsack.com/dio/sombra.png",
        "https://p.actionsack.com/dio/trumpva.gif"
    ]
    bot.say(random.choice(me_dio))


@plugin.rule(r"^god\sbless\s(.*)")
def godbless(bot, trigger):
    bot.action("blesses {}".format(trigger.group(1)))


@plugin.rule(r".*hail\ssatan!.*")
def hailsatan(bot, trigger):
    hail_satan = [
        "https://p.actionsack.com/satan/mii.webm",
        "https://p.actionsack.com/satan/pooh.mp4"
    ]
    bot.say(random.choice(hail_satan))


@plugin.rule(r".*have\sa\sseat.*")
def haveaseat(bot, trigger):
    bot.say("https://p.actionsack.com/misc/haveaseat.gif")


@plugin.rule(".*(jews|✡️|✡).*")
def jews(bot, trigger):
    jew_pics = [
        "https://p.actionsack.com/jews/blame.webp",
        "https://p.actionsack.com/jews/donate.webp"
    ]
    bot.say(random.choice(jew_pics))


@plugin.rule("^k$")
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
        "https://p.actionsack.com/k/kermit.mp4",
        "https://p.actionsack.com/k/seuss.mp4",
        "https://p.actionsack.com/k/shirt.mp4",
        "https://p.actionsack.com/k/snow.mp4",
        "https://p.actionsack.com/k/VHS.mp4",
        "https://p.actionsack.com/k/vldlk.gif"
    ]
    bot.say(random.choice(kk))


@plugin.rule(".*!words.*")
def words(bot, trigger):
    # Requested by Aegisfate on 2020-11-19
    bot.say("https://p.actionsack.com/misc/words.webp")


@plugin.rule(".*kiki.*")
def kiki(bot, trigger):
    kiki = [
        "https://p.actionsack.com/kiki/sauce.png",
        "https://p.actionsack.com/kiki/snoop.png",
        formatting.monospace('[4:44 PM] Kiki: U sound so far right now'),
        "I S M A E L  C H I A  T O R R E S"]
    bot.say(random.choice(kiki))


@plugin.rule(r".*major\sspoiler.*")
def majorspoiler(bot, trigger):
    bot.say("https://p.actionsack.com/misc/spoiler.png")


@plugin.rule(".*!navy.*")
@plugin.command("navy")
@plugin.rate(channel=21600)
def navyseal(bot, trigger):
    """Posts the infamous Navy Seal copypasta...or you get a cat GIF/MP4 version.
    Server-wide rate limit of once per 6 hours.
    Can also be triggered with '!navy' anywhere in a message."""
    navy_seal = [
        "https://p.actionsack.com/misc/navyseal.mp4",
        "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little ''clever'' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
    ]
    bot.say(random.choice(navy_seal), max_messages=4)


@plugin.rule(".*racist.*")
def racist(bot, trigger):
    racists = [
        "https://p.actionsack.com/racist/birds.gif",
        "https://p.actionsack.com/racist/blackmexican.gif",
        "https://p.actionsack.com/racist/fall.gif",
        "https://p.actionsack.com/racist/nelson.gif",
        "https://p.actionsack.com/racist/prettyracist.mp4",
        "https://p.actionsack.com/racist/racist.mp4",
        "https://p.actionsack.com/racist/shake.gif",
        "https://p.actionsack.com/racist/wash.png"
    ]
    bot.say(random.choice(racists))


@plugin.rule(".*niggers.*")
def niggers(bot, trigger):
    niggers = [
        "https://p.actionsack.com/racist/nig/cana.png",
        "https://p.actionsack.com/racist/nig/kan.png",
        "https://p.actionsack.com/racist/nig/kristen.png",
        "https://p.actionsack.com/racist/nig/naggers.gif",
        "https://p.actionsack.com/racist/nig/welfare.png"
    ]
    if trigger.is_privmsg or trigger.sender == "#nsfw":
        bot.say(random.choice(niggers))


@plugin.rule(r".*pasta\sdisasta.*")
def pastadisasta(bot, trigger):
    bot.say("https://p.actionsack.com/🍝/disasta.webm")


@plugin.rule(r".*(?<!his)panic!.*")
def panic(bot, trigger):
    panic_room = [
        "https://p.actionsack.com/panic/00.webp",
        "https://p.actionsack.com/panic/01.webp",
        "https://p.actionsack.com/panic/02.webp",
        "https://p.actionsack.com/panic/03.webp",
        "https://p.actionsack.com/panic/04.webp",
        "https://p.actionsack.com/panic/05.webp",
        "https://p.actionsack.com/panic/06.webp"
    ]
    bot.say(random.choice(panic_room))


@plugin.rule(r".*my\sbrand.*")
def mybrand(bot, trigger):
    bot.say("https://p.actionsack.com/v/MY_BRAND!.webm")


@plugin.rule(".*!nms.*")
def nms(bot, trigger):
    no_mans_sky = [
        "https://p.actionsack.com/nms/ice.png",
        "https://p.actionsack.com/nms/legit.gif",
        "https://p.actionsack.com/nms/mike.png"
    ]
    bot.say(random.choice(no_mans_sky))


@plugin.rule(r"^(nice|sick)\sgif.*")
def sickgif(bot, trigger):
    bot.say("https://p.actionsack.com/misc/sickgif.gif")


@plugin.rule("^nerd!$")
def nerd(bot, trigger):
    bot.say("https://p.actionsack.com/misc/nerd!.gif")


@plugin.rule(".*neat!.*")
def neat(bot, trigger):
    neat = [
        "https://p.actionsack.com/neat/anime.gif",
        "https://p.actionsack.com/neat/bender01.gif",
        "https://p.actionsack.com/neat/bender02.gif",
        "https://p.actionsack.com/neat/bender03.gif",
        "https://p.actionsack.com/neat/ffcat.png",
        "https://p.actionsack.com/neat/neat.mp4",
        "https://p.actionsack.com/neat/spiderman.gif",
        "https://p.actionsack.com/neat/stare.gif"
    ]
    bot.say(random.choice(neat))


@plugin.require_admin
@plugin.rule(r".*my\sserver.*")
def myserver(bot, trigger):
    my_server = [
        "https://p.actionsack.com/server/irl.jpg",
        "https://p.actionsack.com/server/weekend.png"
    ]
    bot.say(random.choice(my_server))


@plugin.rule(r".*(?<!\w)moist(?!\w).*")
def moist(bot, trigger):
    moist = [
        "https://p.actionsack.com/moist/asian.jpg",
        "https://p.actionsack.com/moist/old.jpg"
    ]
    bot.say(random.choice(moist))


@plugin.rule(".*!manga.*")
@plugin.command("manga")
def manga(bot, trigger):
    """Posts a clip from the BowserVids "What's in the bag?" video.
    Can also be triggered with '!manga' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/manga.mp4")


@plugin.rule(r".*let\sme\sin.*")
def letmein(bot, trigger):
    bot.say("https://p.actionsack.com/v/letmein.mp4")


@plugin.rule(r".*i\smade\sthis.*")
def imadethis(bot, trigger):
    iMadeThis = [
        "https://p.actionsack.com/OC/apple.png",
        "https://p.actionsack.com/OC/comic.png",
        "https://p.actionsack.com/OC/iGIF.gif",
        "https://p.actionsack.com/OC/iGIF2.gif",
        "https://p.actionsack.com/OC/iPickle.png",
        "https://p.actionsack.com/OC/starwars.png"
    ]
    bot.say(random.choice(iMadeThis))


@plugin.rule(r".*(?<!\w)eat\sshit.*")
def frank(bot, trigger):
    bot.say("https://p.actionsack.com/misc/frank.gif")


@plugin.rule(".*GTFO.*")
def gtfo(bot, trigger):
    bot.say("https://p.actionsack.com/misc/gtfo.png")


@plugin.rule(".*hawt.*")
def hawt(bot, trigger):
    bot.say("🥵")


@plugin.rule("^hwat.*")
def hwat(bot, trigger):
    hwat = [
        "https://p.actionsack.com/wat/hwat01.webp",
        "https://p.actionsack.com/wat/hwat02.webp"
    ]
    bot.say(random.choice(hwat))


@plugin.rule(r".*I\ssee\syou(?!\').*")
def iseeyou(bot, trigger):
    bot.say("https://p.actionsack.com/👀/iSeeU.mp4")


@plugin.rule(".*eyelids.*")
def eyelids(bot, trigger):
    bot.say("https://p.actionsack.com/👀/eyelids.mp4")


@plugin.rule(".*👀.*")
def eyes(bot, trigger):
    eyes = [
        "https://p.actionsack.com/👀/anime.png",
        "https://p.actionsack.com/👀/big01.png",
        "https://p.actionsack.com/👀/big02.png",
        "https://p.actionsack.com/👀/big03.png",
        "https://p.actionsack.com/👀/big04.png",
        "https://p.actionsack.com/👀/big05.png",
        "https://p.actionsack.com/👀/big06.png",
        "https://p.actionsack.com/👀/big07.png",
        "https://p.actionsack.com/👀/big08.png",
        "https://p.actionsack.com/👀/bigred.png",
        "https://p.actionsack.com/👀/deadpool.gif",
        "https://p.actionsack.com/👀/eric01.png",
        "https://p.actionsack.com/👀/eric02.png",
        "https://p.actionsack.com/👀/eyelids.mp4",
        "https://p.actionsack.com/👀/fecktk.png",
        "https://p.actionsack.com/👀/iSeeU.mp4",
        "https://p.actionsack.com/👀/monkey.png",
        "https://p.actionsack.com/👀/obama.png",
        "https://p.actionsack.com/👀/trump.png",
        "https://p.actionsack.com/👀/walrus.png",
        "https://p.actionsack.com/👀/woody.png"
    ]
    bot.say(random.choice(eyes))


@plugin.rule(r"^💩(|\s)💩$")
def shit(bot, trigger):
    shit_gifs = [
        "https://p.actionsack.com/💩/cardi.mp4",
        "https://p.actionsack.com/💩/extreme.mp4",
        "https://p.actionsack.com/💩/McCafé.gif",
        "https://p.actionsack.com/💩/🚽.gif"
    ]
    bot.say(random.choice(shit_gifs))


@plugin.rule(".*!tesla.*")
@plugin.command("tesla")
def tesla(bot, trigger):
    """Can also be triggered with '!tesla' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/tesla.webm")


@plugin.rule(".*!vn.*")
@plugin.command("vn")
def vapenaysh(bot, trigger):
    """Vape naysh, y'all!
    Can also be triggered with '!vn' anywhere in a message."""
    vape_naysh = [
        "https://p.actionsack.com/vn/20.png",
        "https://p.actionsack.com/vn/2fast.png",
        "https://p.actionsack.com/vn/5minutes.png",
        "https://p.actionsack.com/vn/anal.png",
        "https://p.actionsack.com/vn/area.png",
        "https://p.actionsack.com/vn/arrest.webm",
        "https://p.actionsack.com/vn/bart.gif",
        "https://p.actionsack.com/vn/bart.webm",
        "https://p.actionsack.com/vn/beanie.png",
        "https://p.actionsack.com/vn/breakingbad.png",
        "https://p.actionsack.com/vn/bubble.mp4",
        "https://p.actionsack.com/vn/burns.gif",
        "https://p.actionsack.com/vn/charged.png",
        "https://p.actionsack.com/vn/C&H.gif",
        "https://p.actionsack.com/vn/coconut.png",
        "https://p.actionsack.com/vn/dora.png",
        "https://p.actionsack.com/vn/faceswap.gif",
        "https://p.actionsack.com/vn/fancy-ethan.png",
        "https://p.actionsack.com/vn/first.png",
        "https://p.actionsack.com/vn/flappy.gif",
        "https://p.actionsack.com/vn/gaysex.png",
        "https://p.actionsack.com/vn/godzilla.gif",
        "https://p.actionsack.com/vn/goldengate.png",
        "https://p.actionsack.com/vn/h3h3.png",
        "https://p.actionsack.com/vn/iRape.png",
        "https://p.actionsack.com/vn/it.png",
        "https://p.actionsack.com/vn/iVape.png",
        "https://p.actionsack.com/vn/legend.png",
        "https://p.actionsack.com/vn/LOV.png",
        "https://p.actionsack.com/vn/lungs.gif",
        "https://p.actionsack.com/vn/mei.gif",
        "https://p.actionsack.com/vn/minecraft.png",
        "https://p.actionsack.com/vn/mountvapemore.png",
        "https://p.actionsack.com/vn/mowing.webm",
        "https://p.actionsack.com/vn/party.png",
        "https://p.actionsack.com/vn/passcode.png",
        "https://p.actionsack.com/vn/pc.mp4",
        "https://p.actionsack.com/vn/pepe.png",
        "https://p.actionsack.com/vn/phatcash.png",
        "https://p.actionsack.com/vn/phatclouds.mp4",
        "https://p.actionsack.com/vn/☂.png",
        "https://p.actionsack.com/vn/server.mp4",
        "https://p.actionsack.com/vn/skills.gif",
        "https://p.actionsack.com/vn/skull.png",
        "https://p.actionsack.com/vn/space-smile.png",
        "https://p.actionsack.com/vn/sphynx.png",
        "https://p.actionsack.com/vn/spongebob.png",
        "https://p.actionsack.com/vn/stock_vape.png",
        "https://p.actionsack.com/vn/tornado-ethan.png",
        "https://p.actionsack.com/vn/tornado.png",
        "https://p.actionsack.com/vn/tower.png",
        "https://p.actionsack.com/vn/twintowers.png",
        "https://p.actionsack.com/vn/vapecat.gif",
        "https://p.actionsack.com/vn/vapecat.mp4",
        "https://p.actionsack.com/vn/vapecat.png",
        "https://p.actionsack.com/vn/vapeman.mp4",
        "https://p.actionsack.com/vn/vnkit.png",
        "https://p.actionsack.com/vn/wedding.png",
        "https://p.actionsack.com/vn/whale.png",
        "https://p.actionsack.com/vn/woodwork.png",
        "https://p.actionsack.com/vn/wut.png"
    ]
    bot.say(random.choice(vape_naysh))


@plugin.rule(".*🦈.*")
def sharku(bot, trigger):
    sharks = [
        "https://p.actionsack.com/🦈/TV.webp",
        "https://p.actionsack.com/🦈/bed.webp",
        "https://p.actionsack.com/🦈/bleps_irl.webp",
        "https://p.actionsack.com/🦈/borking.webp",
        "https://p.actionsack.com/🦈/buff_girl.webp",
        "https://p.actionsack.com/🦈/comic.webp",
        "https://p.actionsack.com/🦈/costume.webp",
        "https://p.actionsack.com/🦈/cuddles.webp",
        "https://p.actionsack.com/🦈/drawing.webp",
        "https://p.actionsack.com/🦈/flame.webp",
        "https://p.actionsack.com/🦈/food_bowl.webp",
        "https://p.actionsack.com/🦈/leash.webp",
        "https://p.actionsack.com/🦈/pet.webp"
    ]
    bot.say(random.choice(sharks))


@plugin.rule(r".*🦇(|\s)👨.*")
@plugin.command("batman")
def batman(bot, trigger):
    """Summons a Batman. Names are base64 encoded.
    Can also be triggered by sending a message that is only the "🦇👨" emoji."""
    bat_men = [
        "https://p.actionsack.com/🦇👨/amFqYWJybzE=.webp",
        "https://p.actionsack.com/🦇👨/beer.webp",
        "https://p.actionsack.com/🦇👨/bWlrZQ==.webp",
        "https://p.actionsack.com/🦇👨/dGFzaWFu.webp",
        "https://p.actionsack.com/🦇👨/eG5hYXM=.webp",
        "https://p.actionsack.com/🦇👨/ZmVja3Rr.webp",
        "https://p.actionsack.com/🦇👨/ZmVlaw==.webp"
    ]
    bot.say(random.choice(bat_men))


@plugin.rule(".*🤔{3,}.*")
def think(bot, trigger):
    thinking = [
        "https://p.actionsack.com/think/aesthetic.webp",
        "https://p.actionsack.com/think/agon.webp",
        "https://p.actionsack.com/think/barometer.webp",
        "https://p.actionsack.com/think/beer.webp",
        "https://p.actionsack.com/think/circle.webp",
        "https://p.actionsack.com/think/e.webp",
        "https://p.actionsack.com/think/fu.webp",
        "https://p.actionsack.com/think/layers.webp",
        "https://p.actionsack.com/think/something.webp",
        "https://p.actionsack.com/think/spin.webp",
        "https://p.actionsack.com/think/spinner.webp",
        "https://p.actionsack.com/think/statue.webp",
        "https://p.actionsack.com/think/thonk.webp"
    ]
    bot.say(random.choice(thinking))


@plugin.rule(".*🚸.*")
def as_linus(bot, trigger):
    bot.say("https://p.actionsack.com/as/linus.png")


@plugin.rule(".*🚬.*")
def smoking(bot, trigger):
    bot.say("https://p.actionsack.com/misc/smoking.webp")


@plugin.rule(".*🚁.*")
def heli(bot, trigger):
    helicopter = [
        "https://p.actionsack.com/🚁/engineer.webp",
        "https://p.actionsack.com/🚁/fgr.webp",
        "https://p.actionsack.com/🚁/hair.webp",
        "https://p.actionsack.com/🚁/peewee.webp"
    ]
    bot.say(random.choice(helicopter))


@plugin.rule(".*🍝.*")
def spaghetti(bot, trigger):
    spaghettis = [
        "https://p.actionsack.com/🍝/21pilots.webm",
        "https://p.actionsack.com/🍝/allstar.webm",
        "https://p.actionsack.com/🍝/disasta.webm",
        "https://p.actionsack.com/🍝/double.png",
        "https://p.actionsack.com/🍝/lie.webm",
        "https://p.actionsack.com/🍝/mom's.webm"
    ]
    bot.say(random.choice(spaghettis))


@plugin.rule(".*svehla.*")
def svehla(bot, trigger):
    bot.say("https://p.actionsack.com/misc/svehla.webp")


@plugin.rule(".*🗑.*")
def trash(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🗑.webp")


@plugin.rule(".*!cumcan.*")
@plugin.command("cumcan")
def cumcan(bot, trigger):
    """Cum cleanup.
    Can also be triggered with '!cumcan' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/cumcan.webp")


@plugin.rule(".*!cancer.*")
@plugin.command("cancer")
def cancer(bot, trigger):
    """Warning! Posts pure cancer into chat.
    Can also be triggered with '!cancer' anywhere in a message."""
    cancer_images = [
        "https://p.actionsack.com/as/cancer-list.png",
        "https://p.actionsack.com/as/cancer-microscope.png"
    ]
    bot.say(random.choice(cancer_images))


@plugin.rule(".*!daquan.*")
@plugin.command("daquan")
def daquan(bot, trigger):
    """Can also be triggered with '!daquan' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/daquan.jpg")


@plugin.rule(".*!heff.*")
@plugin.command("heff")
def heff(bot, trigger):
    """Is only game, why you heff to be mad?
    Can also be triggered with '!heff' anywhere in a message."""
    bot.say("https://p.actionsack.com/v/heff.webm")


@plugin.rule(".*!salty.*")
@plugin.command("salty")
def salty(bot, trigger):
    """Can also be triggered with '!salty' anywhere in a message."""
    salty = [
        "https://p.actionsack.com/salt/%23staysalty.png",
        "https://p.actionsack.com/salt/all-these-flavors.png",
        "https://p.actionsack.com/salt/dance.webp",
        "https://p.actionsack.com/salt/power-salt.gif",
        "https://p.actionsack.com/salt/salty-bitch.png",
        "https://p.actionsack.com/salt/super-salty.png"
    ]
    bot.say(random.choice(salty))


@plugin.rule(r".*\[laughs\].*")
def laughs(bot, trigger):
    bot.say("https://p.actionsack.com/misc/laughs.jpg")


@plugin.rule(r".*\[raughs\].*")
def raughs(bot, trigger):
    bot.say("https://p.actionsack.com/tasian/raughs.webp")

# Action Sack People Section


@plugin.rule(".*!asak.*")
@plugin.command("asak")
def asak(bot, trigger):
    """Posts an Action Sack meme.
    Can also be triggered with '!asak' anywhere in a message."""
    asak = [
        "https://p.actionsack.com/as/AG.gif",
        "https://p.actionsack.com/as/aids-convo.png",
        "https://p.actionsack.com/as/beej.gif",
        "https://p.actionsack.com/as/brokeback.png",
        "https://p.actionsack.com/as/bus-stop.png",
        "https://p.actionsack.com/as/cancer-list.png",
        "https://p.actionsack.com/as/cancer-microscope.png",
        "https://p.actionsack.com/as/copy.png",
        "https://p.actionsack.com/as/dirty-jaja.png",
        "https://p.actionsack.com/as/family-fart.png",
        "https://p.actionsack.com/as/family-gun.gif",
        "https://p.actionsack.com/as/fecktk-eyes-mike.png",
        "https://p.actionsack.com/as/gangster.png",
        "https://p.actionsack.com/as/gay-shit.png",
        "https://p.actionsack.com/as/hackers.png",
        "https://p.actionsack.com/as/hand.gif",
        "https://p.actionsack.com/as/iQuit.png",
        "https://p.actionsack.com/as/kys-mike.png",
        "https://p.actionsack.com/as/kys-or-smd.png",
        "https://p.actionsack.com/as/linus.png",
        "https://p.actionsack.com/as/mikeybikey.png",
        "https://p.actionsack.com/as/mugshot.png",
        "https://p.actionsack.com/as/pumpkin.png",
        "https://p.actionsack.com/as/reflection.png",
        "https://p.actionsack.com/as/snapchat.png",
        "https://p.actionsack.com/as/soup.png"
    ]
    bot.say(random.choice(asak))


@plugin.rule(".*!bytes.*")
@plugin.command("bytes")
def ComputersByte(bot, trigger):
    """Posts a ComputersByte meme.
    Can also be triggered with '!bytes' anywhere in a message."""
    computers_byte = [
        "https://p.actionsack.com/bytes/april.png",
        "https://p.actionsack.com/bytes/bj.png",
        "https://p.actionsack.com/bytes/bytes.gif",
        "https://p.actionsack.com/bytes/bytes01.png",
        "https://p.actionsack.com/bytes/cursor.png",
        "https://p.actionsack.com/bytes/hatched.png",
        "https://p.actionsack.com/bytes/syrup.png"
    ]
    bot.say(random.choice(computers_byte))


@plugin.rule(".*!fecktk.*")
@plugin.command("fecktk")
@plugin.rate(user=900)
def fecktk(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    fecktks = [
        "https://p.actionsack.com/fecktk/ascii.webp",
        "https://p.actionsack.com/fecktk/baclol.webp",
        "https://p.actionsack.com/fecktk/bacon.webp",
        "https://p.actionsack.com/fecktk/blowie.webp",
        "https://p.actionsack.com/fecktk/elif.webp",
        "https://p.actionsack.com/fecktk/empty.webp",
        "https://p.actionsack.com/fecktk/eyes.webp",
        "https://p.actionsack.com/fecktk/fecktk01.webp",
        "https://p.actionsack.com/fecktk/fecktk02.webp",
        "https://p.actionsack.com/fecktk/fecktk03.webp",
        "https://p.actionsack.com/fecktk/fecktk04.webp",
        "https://p.actionsack.com/fecktk/fecktk05.webp",
        "https://p.actionsack.com/fecktk/fecktk06.webp",
        "https://p.actionsack.com/fecktk/fecktk07.webp",
        "https://p.actionsack.com/fecktk/fecktk08.webp",
        "https://p.actionsack.com/fecktk/fecktk09.webp",
        "https://p.actionsack.com/fecktk/fecktk10.webp",
        "https://p.actionsack.com/fecktk/fecktk11.webp",
        "https://p.actionsack.com/fecktk/fecktk12.webp",
        "https://p.actionsack.com/fecktk/fecktk13.webp",
        "https://p.actionsack.com/fecktk/fecktk14.webp",
        "https://p.actionsack.com/fecktk/fecktk15.webp",
        "https://p.actionsack.com/fecktk/fecktk16.webp",
        "https://p.actionsack.com/fecktk/fecktk17.webp",
        "https://p.actionsack.com/fecktk/fecktk18.webp",
        "https://p.actionsack.com/fecktk/fecktk19.webp",
        "https://p.actionsack.com/fecktk/fecktk20.webp",
        "https://p.actionsack.com/fecktk/fecktk21.webp",
        "https://p.actionsack.com/fecktk/fecktk22.webp",
        "https://p.actionsack.com/fecktk/fecktk23.webp",
        "https://p.actionsack.com/fecktk/fetus.webp",
        "https://p.actionsack.com/fecktk/guilty.webp",
        "https://p.actionsack.com/fecktk/holden.webp",
        "https://p.actionsack.com/fecktk/lildick.webp",
        "https://p.actionsack.com/fecktk/mumble.webp",
        "https://p.actionsack.com/fecktk/neck.webp",
        "https://p.actionsack.com/fecktk/newegg.webp",
        "https://p.actionsack.com/fecktk/newhouse.webp",
        "https://p.actionsack.com/fecktk/punch.webp",
        "https://p.actionsack.com/fecktk/rape.webp",
        "https://p.actionsack.com/fecktk/sandwich.webp",
        "https://p.actionsack.com/fecktk/slap.webp",
        "https://p.actionsack.com/fecktk/snatch.webp",
        "https://p.actionsack.com/fecktk/strim.webp",
        "https://p.actionsack.com/fecktk/zoomies.webp"
    ]
    bot.say(random.choice(fecktks))


@plugin.rule(".*!feek.*")
@plugin.command("feek")
@plugin.rate(user=900)
def feek(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    feeks = [
        "Works for Me™",
        "https://p.actionsack.com/feek/ben.webp",
        "https://p.actionsack.com/feek/bitch.webp",
        "https://p.actionsack.com/feek/die.webp",
        "https://p.actionsack.com/feek/error.webp",
        "https://p.actionsack.com/feek/feek01.webp",
        "https://p.actionsack.com/feek/feek02.webp",
        "https://p.actionsack.com/feek/feek03.webp",
        "https://p.actionsack.com/feek/feek04.webp",
        "https://p.actionsack.com/feek/feek05.webp",
        "https://p.actionsack.com/feek/feek06.webp",
        "https://p.actionsack.com/feek/feek07.webp",
        "https://p.actionsack.com/feek/feek08.webp",
        "https://p.actionsack.com/feek/free.webp",
        "https://p.actionsack.com/feek/hated.webp",
        "https://p.actionsack.com/feek/hidden.webp",
        "https://p.actionsack.com/feek/lucky.webp",
        "https://p.actionsack.com/feek/PokéKeith.webp",
        "https://p.actionsack.com/feek/rape.webp"
    ]
    bot.say(random.choice(feeks))


@plugin.rule(".*!jaja.*")
@plugin.command("jaja")
@plugin.rate(user=900)
def jajabro(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    jajabros = [
        "https://p.actionsack.com/jaja/dogs.png",
        "https://p.actionsack.com/jaja/halo.jpg",
        "https://p.actionsack.com/jaja/jaja01.png",
        "https://p.actionsack.com/jaja/jaja02.png",
        "https://p.actionsack.com/jaja/jaja03.png",
        "https://p.actionsack.com/jaja/jaja04.png",
        "https://p.actionsack.com/jaja/jaja05.png",
        "https://p.actionsack.com/jaja/jaja06.gif",
        "https://p.actionsack.com/jaja/jaja07.gif",
        "https://p.actionsack.com/jaja/jaja08.png",
        "https://p.actionsack.com/jaja/jaja09.png",
        "https://p.actionsack.com/jaja/jaja10.png",
        "https://p.actionsack.com/jaja/jaja11.png",
        "https://p.actionsack.com/jaja/jaja12.png",
        "https://p.actionsack.com/jaja/plush.png",
        "https://p.actionsack.com/jaja/que.png",
        "https://p.actionsack.com/jaja/smrt.gif",
        "https://p.actionsack.com/jaja/subwat.png"
    ]
    bot.say(random.choice(jajabros))


@plugin.rule(".*!mike.*")
@plugin.command("mike")
@plugin.rate(user=900)
def mike(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    mikes = [
        "https://p.actionsack.com/mike/720v1080.png",
        "https://p.actionsack.com/mike/8ball.png",
        "https://p.actionsack.com/mike/amnesia.png",
        "https://p.actionsack.com/mike/bath.png",
        "https://p.actionsack.com/mike/bernie.png",
        "https://p.actionsack.com/mike/blowie.png",
        "https://p.actionsack.com/mike/brony.png",
        "https://p.actionsack.com/mike/change.png",
        "https://p.actionsack.com/mike/cocksucker.png",
        "https://p.actionsack.com/mike/cuppstick.gif",
        "https://p.actionsack.com/mike/cuppstick.png",
        "https://p.actionsack.com/mike/dance.mp4",
        "https://p.actionsack.com/mike/doll.png",
        "https://p.actionsack.com/mike/down.gif",
        "https://p.actionsack.com/mike/drink.gif",
        "https://p.actionsack.com/mike/everydaymike.gif",
        "https://p.actionsack.com/mike/fraud.png",
        "https://p.actionsack.com/mike/graphene.png",
        "https://p.actionsack.com/mike/haloistrash.png",
        "https://p.actionsack.com/mike/high.png",
        "https://p.actionsack.com/mike/MAGA.png",
        "https://p.actionsack.com/mike/mashed-potatoes.png",
        "https://p.actionsack.com/mike/mike001.png",
        "https://p.actionsack.com/mike/mike002.png",
        "https://p.actionsack.com/mike/mike004.png",
        "https://p.actionsack.com/mike/mike005.png",
        "https://p.actionsack.com/mike/mike006.png",
        "https://p.actionsack.com/mike/mike008.png",
        "https://p.actionsack.com/mike/mike009.png",
        "https://p.actionsack.com/mike/mike010.png",
        "https://p.actionsack.com/mike/mike011.png",
        "https://p.actionsack.com/mike/mike012.png",
        "https://p.actionsack.com/mike/mike013.png",
        "https://p.actionsack.com/mike/mike014.png",
        "https://p.actionsack.com/mike/mike015.png",
        "https://p.actionsack.com/mike/mike016.png",
        "https://p.actionsack.com/mike/mike017.png",
        "https://p.actionsack.com/mike/mike018.png",
        "https://p.actionsack.com/mike/mike019.png",
        "https://p.actionsack.com/mike/mike020.png",
        "https://p.actionsack.com/mike/mike021.png",
        "https://p.actionsack.com/mike/mike022.png",
        "https://p.actionsack.com/mike/mike023.png",
        "https://p.actionsack.com/mike/mike024.png",
        "https://p.actionsack.com/mike/mike025.png",
        "https://p.actionsack.com/mike/mike026.png",
        "https://p.actionsack.com/mike/mike027.png",
        "https://p.actionsack.com/mike/mike028.png",
        "https://p.actionsack.com/mike/mike029.png",
        "https://p.actionsack.com/mike/mike030.png",
        "https://p.actionsack.com/mike/mike031.png",
        "https://p.actionsack.com/mike/mike032.png",
        "https://p.actionsack.com/mike/miker.png",
        "https://p.actionsack.com/mike/MLP.png",
        "https://p.actionsack.com/mike/MMM.png",
        "https://p.actionsack.com/mike/noctua.png",
        "https://p.actionsack.com/mike/nosex.png",
        "https://p.actionsack.com/mike/quora.png",
        "https://p.actionsack.com/mike/simple-mike.png",
        "https://p.actionsack.com/mike/smurf.png",
        "https://p.actionsack.com/mike/syria.png",
        "https://p.actionsack.com/mike/virgin.png",
        "https://p.actionsack.com/mike/yoj.png",
        "https://p.actionsack.com/mike/yummy-mike.png",
        "https://p.actionsack.com/mike/📖/📖+.jpg",
        "https://p.actionsack.com/mike/📖/📖.gif",
        "https://p.actionsack.com/mike/📖/📖.jpg",
        "https://p.actionsack.com/mike/📖/📖🐇.jpg"
    ]
    bot.say(random.choice(mikes))


@plugin.rule(".*!tasian.*")
@plugin.command("tasian")
@plugin.rate(user=900)
def tasian(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    tasians = [
        "https://p.actionsack.com/tasian/2016.webp",
        "https://p.actionsack.com/tasian/balloon.webp",
        "https://p.actionsack.com/tasian/dance.webp",
        "https://p.actionsack.com/tasian/dance.mp4",
        "https://p.actionsack.com/tasian/D.webp",
        "https://p.actionsack.com/tasian/driver.webp",
        "https://p.actionsack.com/tasian/fortnite.webp",
        "https://p.actionsack.com/tasian/grin.webp",
        "https://p.actionsack.com/tasian/korea.webp",
        "https://p.actionsack.com/tasian/koreatext.webp",
        "https://p.actionsack.com/tasian/math.webp",
        "https://p.actionsack.com/tasian/naga.webp",
        "https://p.actionsack.com/tasian/noodles.webp",
        "https://p.actionsack.com/tasian/pacman.webp",
        "https://p.actionsack.com/tasian/pickles.webp",
        "https://p.actionsack.com/tasian/pikaval.webp",
        "https://p.actionsack.com/tasian/racist01.webp",
        "https://p.actionsack.com/tasian/racist02.webp",
        "https://p.actionsack.com/tasian/racist03.webp",
        "https://p.actionsack.com/tasian/raughs.webp",
        "https://p.actionsack.com/tasian/singing.mp4",
        "https://p.actionsack.com/tasian/tall.webp",
        "https://p.actionsack.com/tasian/val01.webp",
        "https://p.actionsack.com/tasian/val02.webp",
        "https://p.actionsack.com/tasian/val03.webp",
        "https://p.actionsack.com/tasian/val04.webp",
        "https://p.actionsack.com/tasian/val05.webp",
        "https://p.actionsack.com/tasian/val06.webp",
        "https://p.actionsack.com/tasian/val07.webp"
    ]
    bot.say(random.choice(tasians))


@plugin.rule(".*!viz.*")
@plugin.command("viz")
@plugin.rate(user=900)
def viz(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    vizs = [
        "https://p.actionsack.com/viz/bad4u.webp",
        "https://p.actionsack.com/viz/drunk01.webp",
        "https://p.actionsack.com/viz/drunk02.webp",
        "https://p.actionsack.com/viz/drunk03.webp",
        "https://p.actionsack.com/viz/drunk04.webp",
        "https://p.actionsack.com/viz/drunk05.webp",
        "https://p.actionsack.com/viz/drunk06.webp",
        "https://p.actionsack.com/viz/drunk07.webp",
        "https://p.actionsack.com/viz/drunk08.webp",
        "https://p.actionsack.com/viz/drunk09.webp",
        "https://p.actionsack.com/viz/fecktk.webp",
        "https://p.actionsack.com/viz/FOT.webp",
        "https://p.actionsack.com/viz/lololololol.webp",
        "https://p.actionsack.com/viz/lovescock.webp",
        "https://p.actionsack.com/viz/oh.ok.webp",
        "https://p.actionsack.com/viz/poison.webp",
        "https://p.actionsack.com/viz/ride.webp",
        "https://p.actionsack.com/viz/tree.webp",
        "https://p.actionsack.com/viz/whoknows.webp"
    ]
    bot.say(random.choice(vizs))


@plugin.rule(".*!voodoo.*")
@plugin.command("voodoo")
def voodoo(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    voodoos = [
        "https://p.actionsack.com/voodoo/eggslut.webp",
        "https://p.actionsack.com/voodoo/eggslut-lq.webp",
        "https://p.actionsack.com/voodoo/eggslut-smol.webp",
        "https://p.actionsack.com/voodoo/pewpew.webp",
        "I fantasize about fucking California's earthquake fault line. The dirt, the debris, the thought of the earth quivering under me as I slowly stick my dick into its gaping wide entrance. I keep looking at news stories and getting the firmest erections of my life seeing those beautiful cracks. She's so open and so wanting. Each earthquake is like another whimper just begging for me to take her. The amount of cum I've lost just thinking about thrusting my rod into our beloved planet. Talk about getting my rocks off. Fuck I'm hard."
    ]
    bot.say(random.choice(voodoos), max_messages=2)


@plugin.rule(".*!xnaas.*")
@plugin.command("xnaas")
@plugin.rate(user=900)
def xnaas(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    xnass = [
        "https://p.actionsack.com/xnaas/animals.webp",
        "https://p.actionsack.com/xnaas/d3.webm",
        "https://p.actionsack.com/xnaas/fd.mp4",
        "https://p.actionsack.com/xnaas/gape.webp",
        "https://p.actionsack.com/xnaas/iShit.webp",
        "https://p.actionsack.com/xnaas/mac.webp",
        "https://p.actionsack.com/xnaas/propain.webp",
        "https://p.actionsack.com/xnaas/pussy.mp4",
        "https://p.actionsack.com/xnaas/QotH.webp",
        "https://p.actionsack.com/xnaas/reality.webp",
        "https://p.actionsack.com/xnaas/shaved.webp",
        "https://p.actionsack.com/xnaas/typing.webp",
        "https://p.actionsack.com/xnaas/vamp.webp",
        "https://p.actionsack.com/xnaas/victory.webp",
        "https://p.actionsack.com/xnaas/wesmart.webp",
        "https://p.actionsack.com/xnaas/xnaas001.webp",
        "https://p.actionsack.com/xnaas/xnaas002.webp",
        "https://p.actionsack.com/xnaas/xnaas003.webp",
        "https://p.actionsack.com/xnaas/xnaas004.webp",
        "https://p.actionsack.com/xnaas/xnaas005.webp",
        "https://p.actionsack.com/xnaas/xnaas006.webp",
        "https://p.actionsack.com/xnaas/xnaas008.webp",
        "https://p.actionsack.com/xnaas/xnaas009.webp",
        "https://p.actionsack.com/xnaas/xnaas010.webp",
        "https://p.actionsack.com/xnaas/xnaas011.webp",
        "https://p.actionsack.com/xnaas/xnaas012.webp",
        "https://p.actionsack.com/xnaas/xnaas013.webp",
        "https://p.actionsack.com/xnaas/xnaas014.webp",
        "https://p.actionsack.com/xnaas/yeehaw.webp",
        "https://p.actionsack.com/v/tesla.webm"
    ]
    bot.say(random.choice(xnass))


@plugin.rule(".*!JTL.*")
@plugin.command("JTL")
@plugin.rate(user=900)
def JTL(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    JTL = [
        "JTL thinks he's not 100% gay lol",
        "JTL is addicted to {} 😱".format("\u200B".join("xnaas")),
        "God cries because JTL touches himself at night.",
        "JTL's quote addition is insane. Almost feel bad for the dude.",
        "https://p.actionsack.com/JTL/sendit.webp"
    ]
    bot.say(random.choice(JTL))


@plugin.rule(".*!nC.*")
@plugin.command("nC")
@plugin.rate(user=900)
def nC(bot, trigger):
    """A user triggering this command can only do so once per 15 minutes."""
    nC = [
        "https://p.actionsack.com/nC/gambler.webp"
    ]
    bot.say(random.choice(nC))

# /Action Sack People Section


@plugin.rule(".*!RGB.*")
@plugin.command("RGB")
def RGB(bot, trigger):
    """Can also be triggered with '!RGB' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/RGB.webp")


@plugin.rule(".*savage!.*")
def savage(bot, trigger):
    bot.say("https://p.actionsack.com/misc/savage.gif")


@plugin.rule(".*(salad|🥗).*")
def salad(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🥗.png")


@plugin.rule(".*(?<!t)rickles.*")
def rickles(bot, trigger):
    bot.say("https://p.actionsack.com/misc/rickles.png")


@plugin.rule(r"^(yo|)u\swin.*")
def uwin(bot, trigger):
    bot.say("https://p.actionsack.com/misc/uWin.png")


@plugin.rule(r"^you\sdon\'t\ssay.*")
def udontsay(bot, trigger):
    bot.say("https://p.actionsack.com/misc/yds.png")


@plugin.rule(r".*you\'re\stoo\sslow.*")
def urtooslow(bot, trigger):
    too_slow = [
        "https://p.actionsack.com/sanic/master.png",
        "https://p.actionsack.com/sanic/running.gif"
    ]
    bot.say(random.choice(too_slow))


@plugin.rule(r".*whale\srape.*")
def whalerape(bot, trigger):
    bot.say("https://p.actionsack.com/v/whalerape.mp4")


@plugin.rule(".*kwaken.*")
def kwaken(bot, trigger):
    bot.say("https://p.actionsack.com/misc/kwaken.png")


@plugin.rule(".*KFC.*")
def kfc(bot, trigger):
    kfc = [
        "https://p.actionsack.com/kfc/00.png",
        "https://p.actionsack.com/kfc/01.png",
        "https://p.actionsack.com/kfc/02.png",
    ]
    bot.say(random.choice(kfc))


@plugin.rule(".*(?<!en)joy!.*")
def joy(bot, trigger):
    bot.say("https://p.actionsack.com/misc/joy.gif")


@plugin.rule(".*bernie.*")
def bernii(bot, trigger):
    bot.say("https://p.actionsack.com/misc/bernii.webp")


@plugin.rule(".*blumkin.*")
def blumpkin(bot, trigger):
    bot.say("https://p.actionsack.com/misc/blumkin.gif")


@plugin.rule(".*!(chief|halo).*")
@plugin.command("chief", "halo")
def chief(bot, trigger):
    """Posts a Master Chief/Halo-related image.
    Can also be triggered with '!chief' or '!halo' anywhere in chat."""
    master_chef = [
        "https://p.actionsack.com/son/chiefs.webp",
        "https://p.actionsack.com/son/halo.webp",
        "https://p.actionsack.com/halo/59bullets.png",
        "https://p.actionsack.com/halo/anime.png",
        "https://p.actionsack.com/halo/car.gif",
        "https://p.actionsack.com/halo/face00.gif",
        "https://p.actionsack.com/halo/face01.gif",
        "https://p.actionsack.com/halo/Halo5.png",
        "https://p.actionsack.com/halo/happening.gif",
        "https://p.actionsack.com/halo/jaja.png",
        "https://p.actionsack.com/halo/perfect_game.png",
        "https://p.actionsack.com/halo/pony.png",
        "https://p.actionsack.com/halo/skiing.png",
        "https://p.actionsack.com/halo/what_do_you_think.png",
        "https://p.actionsack.com/halo/❔.png",
        "https://p.actionsack.com/halo/🗑.png"
    ]
    bot.say(random.choice(master_chef))


@plugin.rule(".*!drphil.*")
@plugin.command("drphil")
def drphil(bot, trigger):
    """Can also be triggered with '!drphil' anywhere in a message."""
    dr_phil = [
        "https://p.actionsack.com/drphil/apples.webp",
        "https://p.actionsack.com/drphil/ride.webp",
        "https://p.actionsack.com/drphil/WSTYAHHWASFOH.webp"
    ]
    bot.say(random.choice(dr_phil))


@plugin.rule(".*🌀.*")
def hurricane(bot, trigger):
    hurricanes = [
        "https://p.actionsack.com/🌀/AD.png",
        "https://p.actionsack.com/🌀/matthew.png"
    ]
    bot.say(random.choice(hurricanes))


@plugin.rule(".*!pepe.*")
@plugin.command("pepe")
def pepe(bot, trigger):
    """Posts a rare pepe into chat.
    Can also be triggered with '!pepe' anywhere in a message."""
    rare_pepes = [
        "https://p.actionsack.com/pepe/anime.png",
        "https://p.actionsack.com/pepe/black.png",
        "https://p.actionsack.com/pepe/bulba.jpg",
        "https://p.actionsack.com/pepe/combat.gif",
        "https://p.actionsack.com/pepe/cthulhu.png",
        "https://p.actionsack.com/pepe/great-post.png",
        "https://p.actionsack.com/pepe/human-mouth.gif",
        "https://p.actionsack.com/pepe/reeeee.gif",
        "https://p.actionsack.com/pepe/religion.jpg",
        "https://p.actionsack.com/pepe/steak.png",
        "https://p.actionsack.com/pepe/sub.png",
        "https://p.actionsack.com/pepe/trump.png"
    ]
    bot.say(random.choice(rare_pepes))


@plugin.rule(".*repost.*")
def repost(bot, trigger):
    reposts = [
        "https://p.actionsack.com/repost/3weeks.png",
        "https://p.actionsack.com/repost/5minutes.png",
        "https://p.actionsack.com/repost/back-to-the-repost.png",
        "https://p.actionsack.com/repost/better.gif",
        "https://p.actionsack.com/repost/cat.webp",
        "https://p.actionsack.com/repost/cock.png",
        "https://p.actionsack.com/repost/detected.gif",
        "https://p.actionsack.com/repost/evil.gif",
        "https://p.actionsack.com/repost/GotG.mp4",
        "https://p.actionsack.com/repost/groundhog.gif",
        "https://p.actionsack.com/repost/homer.png",
        "https://p.actionsack.com/repost/IB.mp4",
        "https://p.actionsack.com/repost/ITSAREPOST!!!.png",
        "https://p.actionsack.com/repost/jurassic.gif",
        "https://p.actionsack.com/repost/MiB.webp",
        "https://p.actionsack.com/repost/nobody_cares.gif",
        "https://p.actionsack.com/repost/ohshit.mp4",
        "https://p.actionsack.com/repost/pacific_rim.gif",
        "https://p.actionsack.com/repost/picard.mp4",
        "https://p.actionsack.com/repost/police.png",
        "https://p.actionsack.com/repost/rekt.gif",
        "https://p.actionsack.com/repost/remember.png",
        "https://p.actionsack.com/repost/repeat.gif",
        "https://p.actionsack.com/repost/security-check.png",
        "https://p.actionsack.com/repost/seinfeld.gif",
        "https://p.actionsack.com/repost/soflo.png",
        "https://p.actionsack.com/repost/wait....gif"
    ]
    bot.say(random.choice(reposts))


@plugin.rule("^🪦$")
def rip(bot, trigger):
    bot.say("https://p.actionsack.com/emoji/rip.png")


@plugin.rule(".*!trump.*")
@plugin.command("trump")
def trump(bot, trigger):
    """Can also be triggered with '!trump' anywhere in a message."""
    trumps = [
        "https://p.actionsack.com/trump/baby.png",
        "https://p.actionsack.com/trump/beatdown.gif",
        "https://p.actionsack.com/trump/bingbong.png",
        "https://p.actionsack.com/trump/blog.mp4",
        "https://p.actionsack.com/trump/boo!.mp4",
        "https://p.actionsack.com/trump/caress.gif",
        "https://p.actionsack.com/trump/covfefe.png",
        "https://p.actionsack.com/trump/dump.png",
        "https://p.actionsack.com/trump/fuckyou.gif",
        "https://p.actionsack.com/trump/golf.gif",
        "https://p.actionsack.com/trump/HEYYOUGUYS.png",
        "https://p.actionsack.com/trump/kiss.png",
        "https://p.actionsack.com/trump/monster.mp4",
        "https://p.actionsack.com/trump/nagus.png",
        "https://p.actionsack.com/trump/no.mp4",
        "https://p.actionsack.com/trump/real-villian.gif",
        "https://p.actionsack.com/trump/reason.mp4",
        "https://p.actionsack.com/trump/satan.gif",
        "https://p.actionsack.com/trump/sauron.png",
        "https://p.actionsack.com/trump/simple.png",
        "https://p.actionsack.com/trump/stump.gif",
        "https://p.actionsack.com/trump/tacos.gif",
        "https://p.actionsack.com/trump/tap.png",
        "https://p.actionsack.com/trump/tears.mp4",
        "https://p.actionsack.com/trump/tears.png",
        "https://p.actionsack.com/trump/think.png",
        "https://p.actionsack.com/trump/troll.png",
        "https://p.actionsack.com/trump/trump-chan.png",
        "https://p.actionsack.com/trump/trumpler.mp4",
        "https://p.actionsack.com/trump/trump-vs-hillary.mp4",
        "https://p.actionsack.com/trump/trump-yell.png",
        "https://p.actionsack.com/trump/wall.mp4",
        "https://p.actionsack.com/trump/WOF.png",
        "https://p.actionsack.com/trump/トランプ.webm"
    ]
    bot.say(random.choice(trumps))


@plugin.command("downvote")
def downvote(bot, trigger):
    downvotes = [
        "https://p.actionsack.com/vote/down/00.gif"
    ]
    bot.say(random.choice(downvotes))


@plugin.command("upvote")
def upvote(bot, trigger):
    upvotes = [
        "https://p.actionsack.com/vote/up/00.mp4",
        "https://p.actionsack.com/vote/up/01.mp4"
    ]
    bot.say(random.choice(upvotes))


@plugin.rule(r"^apologize\.(\s$|$)")
def apologize(bot, trigger):
    bot.say("https://p.actionsack.com/misc/apologize.webp")


@plugin.rule(r".*(?<!sh)it\'s\shappening.*")
def happening(bot, trigger):
    its_happening = [
        "https://p.actionsack.com/halo/happening.gif",
        "https://p.actionsack.com/misc/happening.gif"
    ]
    bot.say(random.choice(its_happening))


@plugin.rule(r"^It\'s\stime\sto\sstop!$")
def timetostop(bot, trigger):
    time_to_stop = [
        "https://p.actionsack.com/🛑/00.webp",
        "https://p.actionsack.com/🛑/01.webp",
        "https://p.actionsack.com/🛑/02.webp",
        "https://p.actionsack.com/🛑/03.webp",
    ]
    bot.say(random.choice(time_to_stop))


@plugin.rule(".*pepsi.*")
def pepsi(bot, trigger):
    bot.say("https://p.actionsack.com/misc/pepsi.gif")


@plugin.rule(".*terrorist.*")
def terrorists(bot, trigger):
    bot.say("https://p.actionsack.com/misc/terrorist.gif")


@plugin.rule(r".*space\spants!.*")
def spacepants(bot, trigger):
    space_pants = [
        "https://p.actionsack.com/misc/spacepants.gif",
        "https://p.actionsack.com/v/spacepants.mp4"
    ]
    bot.say(random.choice(space_pants))


@plugin.rule(".*!peep.*")
@plugin.command("peep")
def peep(bot, trigger):
    """Peep on chat. Can also be triggered with '!peep' anywhere in a message."""
    bot.say("https://p.actionsack.com/misc/peep.gif")


@plugin.rule(".*🥒.*")
def cucumber(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🥒.gif")


@plugin.rule(".*krang.*")
def krang(bot, trigger):
    bot.say("https://p.actionsack.com/misc/krang.png")


@plugin.rule(".*!reality.*")
@plugin.command("reality")
@plugin.rate(channel=86400)
def reality(bot, trigger):
    """Lays down a hard reality. Rate-limited to once per day per channel."""
    bot.say("https://p.actionsack.com/xnaas/reality.webp")


@plugin.rule(r".*mass\smurder.*")
@plugin.command("shooting")
def shooting(bot, trigger):
    bot.say("https://p.actionsack.com/misc/shooting.gif")


@plugin.rule(r".*🆒(|\s)🐱.*")
def coolcat(bot, trigger):
    bot.say("https://p.actionsack.com/misc/🆒🐱.png")


@plugin.rule(".*shitpost.*")
def shitpost(bot, trigger):
    shit_post = [
        "https://p.actionsack.com/shitpost/catpost.gif",
        "https://p.actionsack.com/shitpost/dbz.png",
        "https://p.actionsack.com/shitpost/shitpost.png"
    ]
    bot.say(random.choice(shit_post))


@plugin.rule("^No!$")
def no(bot, trigger):
    nonono = [
        "https://p.actionsack.com/no/00.mp4",
        "https://p.actionsack.com/no/01.mp4",
    ]
    bot.say(random.choice(nonono))


@plugin.rule(r"^just\.\.\.no$")
def justno(bot, trigger):
    bot.say("https://p.actionsack.com/no/just...no.webp")


@plugin.rule(".*🏇.*")
def horses(bot, trigger):
    race_horses = [
        "https://p.actionsack.com/🏇/girl.gif",
        "https://p.actionsack.com/🏇/hoh.gif"
    ]
    bot.say(random.choice(race_horses))


@plugin.rule(".*👽.*")
def alien(bot, trigger):
    bot.say("https://p.actionsack.com/misc/👽.webp")


@plugin.rule(".*😮{3,}.*")
def gaping_mouth(bot, trigger):
    bot.say("https://p.actionsack.com/misc/😮.webp")


@plugin.rule(".*🕷(?!👨).*")
def spider(bot, trigger):
    spiders = [
        "https://p.actionsack.com/🕷/cat.webp",
        "https://p.actionsack.com/🕷/girl.webp",
        "https://p.actionsack.com/🕷/song.webp",
        "https://p.actionsack.com/🕷/swing.webp"
    ]
    bot.say(random.choice(spiders))


@plugin.rule(r".*(spiderman|🕷(|\s)👨).*")
def spiderman(bot, trigger):
    spider_man = [
        "https://p.actionsack.com/🕷👨/orphans.webp",
        "https://p.actionsack.com/🕷👨/smell.webp"
    ]
    bot.say(random.choice(spider_man))


@plugin.rule(".*shitstorm.*")
def shitstorm(bot, trigger):
    bot.say("https://p.actionsack.com/misc/shitstorm.webp")


@plugin.rule("!ts")
@plugin.command("ts")
def teamspeak(bot, trigger):
    bot.say("https://p.actionsack.com/a/teamspeak.ogg")


@plugin.rule(".*!tmf.*")
@plugin.command("tmf")
def thatsmyfetish(bot, trigger):
    """That's my fetish. ( ͡° ͜ʖ ͡°)"""
    bot.say("https://p.actionsack.com/misc/tmf.webp")


@plugin.rule("^NDA$")
def nda(bot, trigger):
    bot.say(formatting.bold(
        "⚠️ That's ⚠️ some ⚠️ NDA ⚠️ shit ⚠️ right ⚠️ there! ⚠️"))


@plugin.rule(".*darude.*")
def darude(bot, trigger):
    bot.say("https://p.actionsack.com/v/darude.mp4")


@plugin.rule(".*numa.*")
def numanuma(bot, trigger):
    bot.say("https://p.actionsack.com/v/numa.mp4")


@plugin.rule(".*!gems.*")
@plugin.command("gems")
def gems(bot, trigger):
    bot.say("https://p.actionsack.com/v/gems.mp4")


@plugin.rule(".*explosion!.*")
def explosion(bot, trigger):
    explosion = [
        "https://p.actionsack.com/v/explosion/01.mp4",
        "https://p.actionsack.com/v/explosion/02.mp4",
        "https://p.actionsack.com/v/explosion/03.mp4"
    ]
    bot.say(random.choice(explosion))


@plugin.rule(r".*I\sneed\sa\shero.*")
def ineedahero(bot, trigger):
    bot.say("https://p.actionsack.com/v/ineedahero.mp4")


@plugin.rule(".*!MDMA.*")
@plugin.command("mdma")
def mdma(bot, trigger):
    bot.say("https://p.actionsack.com/a/MDMA.ogg")


@plugin.rule(".*!albatraoz.*")
@plugin.command("albatraoz")
def albatraoz(bot, trigger):
    bot.say("https://p.actionsack.com/a/albatraoz.ogg")


@plugin.rule(".*!swing.*")
@plugin.command("swing")
def little_swing(bot, trigger):
    bot.say("https://p.actionsack.com/a/swing.ogg")
