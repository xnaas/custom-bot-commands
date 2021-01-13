### Smite VGS
# \x0311 – Start Light Cyan
# \u200B – ZWSP
# \x0315 – Start Light Grey
from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, formatting
import random
import unicodedata


@module.rule("^VVA$")
def vgs_vva(bot, trigger):
  bot.say("{}{}{}: [VVA] Ok!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVB$")
def vgs_vvb(bot, trigger):
  bot.say("{}{}{}: [VVB] Be right back!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGF$")
def vgs_vvgf(bot, trigger):
  bot.say("{}{}{}: [VVGF] Have fun!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGB$")
def vgs_vvgb(bot, trigger):
  bot.say("{}{}{}: [VVGB] Bye!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGL$")
def vgs_vvgl(bot, trigger):
  bot.say("{}{}{}: [VVGL] Good luck!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGN$")
def vgs_vvgn(bot, trigger):
  bot.say("{}{}{}: [VVGN] Nice job!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGO$")
def vgs_vvgo(bot, trigger):
  bot.say("{}{}{}: [VVGO] Oops!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGQ$")
def vgs_vvgq(bot, trigger):
  bot.say("{}{}{}: [VVGQ] Quiet!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGR$")
def vgs_vvgr(bot, trigger):
  bot.say("{}{}{}: [VVGR] No problem!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGS$")
def vgs_vvgs(bot, trigger):
  bot.say("{}{}{}: [VVGS] Curses!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGT$")
def vgs_vvgt(bot, trigger):
  bot.say("{}{}{}: [VVGT] That's too bad!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGW$")
def vgs_vvgw(bot, trigger):
  bot.say("{}{}{}: [VVGW] You're welcome!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVN$")
def vgs_vvn(bot, trigger):
  bot.say("{}{}{}: [VVN] No!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVP$")
def vgs_vvp(bot, trigger):
  bot.say("{}{}{}: [VVP] Please?".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVS$")
def vgs_vvs(bot, trigger):
  bot.say("{}{}{}: [VVS] Sorry!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVT$")
def vgs_vvt(bot, trigger):
  bot.say("{}{}{}: [VVT] Thanks!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVW$")
def vgs_vvw(bot, trigger):
  bot.say("{}{}{}: [VVW] Wait!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVX$")
def vgs_vvx(bot, trigger):
  bot.say("{}{}{}: [VVX] Cancel that!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVY$")
def vgs_vvy(bot, trigger):
  bot.say("{}{}{}: [VVY] Yes!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VEA$")
def vgs_vea(bot, trigger):
  bot.say("{}{}{}: [VEA] Awesome!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VEG$")
def vgs_veg(bot, trigger):
  bot.say("{}{}{}: [VEG] I'm the greatest!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VER$")
def vgs_ver(bot, trigger):
  bot.say("{}{}{}: [VER] You rock!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VEW$")
def vgs_vew(bot, trigger):
  bot.say("{}{}{}: [VEW] Woohoo!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAG$")
def vgs_vag(bot, trigger):
  bot.say("{}{}{}: [VAG] Attack the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSO$")
def vgs_vso(bot, trigger):
  bot.say("{}{}{}: [VSO] I'm on it!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSS$")
def vgs_vss(bot, trigger):
  bot.say("{}{}{}: [VSS] I'm building stacks!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSTT$")
def vgs_vstt(bot, trigger):
  bot.say("{}{}{}: [VSTT] I have returned!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVK$")
def vgs_vvk(bot, trigger):
  bot.say("{}{}{}: [VVK] Stepping away for a moment.".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVT$")
def vgs_vvvt(bot, trigger):
  bot.say("{}{}{}: [VVVT] It's a trap!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVC$")
def vgs_vvc(bot, trigger):
  bot.say("{}{}{}: [VVC] Completed!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VCC$")
def vgs_vcc(bot, trigger):
  bot.say("{}{}{}: [VCC] Be careful!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
### Smite VGS Section