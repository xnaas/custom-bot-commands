# Smite VGS
# \x0311 – Start Light Cyan
# \u200B – ZWSP
# \x0315 – Start Light Grey
from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, formatting
import random
import decimal
import unicodedata

# <VA – Attack>
@module.rule("^VAA$")
def vgs_vaa(bot, trigger):
    bot.say("{}{}{}: [VAA] Attack!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAF$")
def vgs_vaf(bot, trigger):
    bot.say("{}{}{}: [VAF] Attack Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAG$")
def vgs_vag(bot, trigger):
    bot.say("{}{}{}: [VAG] Attack the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAM$")
def vgs_vam(bot, trigger):
    bot.say("{}{}{}: [VAM] Attack the Titan!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAN$")
def vgs_van(bot, trigger):
    bot.say("{}{}{}: [VAN] Attack the Minions!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VA1$")
def vgs_va1(bot, trigger):
    bot.say("{}{}{}: [VA1] Attack left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VA2$")
def vgs_va2(bot, trigger):
    bot.say("{}{}{}: [VA2] Attack middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VA3$")
def vgs_va3(bot, trigger):
    bot.say("{}{}{}: [VA3] Attack right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VAT1$")
def vgs_vat1(bot, trigger):
    tof = [
        "left tower",
        "the left phoenix"
    ]
    bot.say("{}{}{}: [VAT1] Attack {}!".format("\x0311", "\u200B".join(trigger.nick), "\x0315", random.choice(tof)))

@module.rule("^VAT2$")
def vgs_vat2(bot, trigger):
    tof= [
        "middle tower",
        "the middle phoenix"
    ]
    bot.say("{}{}{}: [VAT2] Attack!".format("\x0311", "\u200B".join(trigger.nick), "\x0315", random.choice(tof)))

@module.rule("^VAT3$")
def vgs_vat3(bot, trigger):
    tof=[
        "right tower",
        "the right phoenix"
    ]
    bot.say("{}{}{}: [VAT3] Attack!".format("\x0311", "\u200B".join(trigger.nick), "\x0315", random.choice(tof)))
# </VA – Attack>


# <VB – Enemy>
@module.rule("^VBA$")
def vgs_vba(bot, trigger):
    bot.say("{}{}{}: [VBA] Enemy ultimate incoming!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBB$")
def vgs_vbb(bot, trigger):
    bot.say("{}{}{}: [VBB] Enemies have returned to base.".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBD$")
def vgs_vbd(bot, trigger):
    bot.say("{}{}{}: [VBD] Enemy ultimate down!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBE$")
def vgs_vbe(bot, trigger):
    bot.say("{}{}{}: [VBE] Enemies behind us!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBF$")
def vgs_vbf(bot, trigger):
    bot.say("{}{}{}: [VBF] Enemies at the Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBG$")
def vgs_vbg(bot, trigger):
    bot.say("{}{}{}: [VBG] Enemies at the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBJJ$")
def vgs_vbjj(bot, trigger):
    bot.say("{}{}{}: [VBJJ] Enemies in the jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBJ1$")
def vgs_vbj1(bot, trigger):
    bot.say("{}{}{}: [VBJ1] Enemies in the left jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBJ2$")
def vgs_vbj3(bot, trigger):
    bot.say("{}{}{}: [VBJ3] Enemies in the right jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBM$")
def vgs_vbm(bot, trigger):
    bot.say("{}{}{}: [VBM] Enemies at our Titan!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VBS$")
def vgs_vbs(bot, trigger):
    bot.say("{}{}{}: [VBS] Enemy spotted!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VB1$")
def vgs_vb1(bot, trigger):
    bot.say("{}{}{}: [VB1] Enemies in left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VB2$")
def vgs_vb2(bot, trigger):
    bot.say("{}{}{}: [VB2] Enemies in middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VB3$")
def vgs_vb3(bot, trigger):
    bot.say("{}{}{}: [VB3] Enemies in right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VB – Enemy>


# <VC – Careful>
@module.rule("^VCB$")
def vgs_vcb(bot, trigger):
    bot.say("{}{}{}: [VCB] Return to base!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VCC$")
def vgs_vcc(bot, trigger):
    bot.say("{}{}{}: [VCC] Be careful!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VCJ$")
def vgs_vcj(bot, trigger):
    bot.say("{}{}{}: [VCJ] Be careful in the jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VC1$")
def vgs_vc1(bot, trigger):
    bot.say("{}{}{}: [VC1] Be careful left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VC2$")
def vgs_vc2(bot, trigger):
    bot.say("{}{}{}: [VC2] Be careful middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VC3$")
def vgs_vc3(bot, trigger):
    bot.say("{}{}{}: [VC3] Be careful right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VC – Careful>


# <VD – Defend>
@module.rule("^VDD$")
def vgs_vdd(bot, trigger):
    bot.say("{}{}{}: [VDD] Defend!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VDF$")
def vgs_vdf(bot, trigger):
    bot.say("{}{}{}: [VDF] Defend the Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VDG$")
def vgs_vdg(bot, trigger):
    bot.say("{}{}{}: [VDG] Defend the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VD1$")
def vgs_vd1(bot, trigger):
    bot.say("{}{}{}: [VD1] Defend left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VD2$")
def vgs_vd2(bot, trigger):
    bot.say("{}{}{}: [VD2] Defend middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VD3$")
def vgs_vd3(bot, trigger):
    bot.say("{}{}{}: [VD3] Defend right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VDM$")
def vgs_vdm(bot, trigger):
    defend=[
        "Titan",
        "Portal"
    ]
    bot.say("{}{}{}: [VDM] Defend the {}!".format("\x0311", "\u200B".join(trigger.nick), "\x0315", random.choice(defend)))
# </VD – Defend>


# <VE – Emote>
# VEJ = No solution for God jokes atm
# VEL = No solution for God laughs atm
# VET = No solution for God taunts atm
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
# </VE – Emote>


# <VF – MIA>
@module.rule("^VFF$")
def vgs_vff(bot, trigger):
    bot.say("{}{}{}: [VFF] Enemy missing!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VF1$")
def vgs_vf1(bot, trigger):
    bot.say("{}{}{}: [VF1] Enemy missing left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VF2$")
def vgs_vf2(bot, trigger):
    bot.say("{}{}{}: [VF2] Enemy missing middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VF3$")
def vgs_vf3(bot, trigger):
    bot.say("{}{}{}: [VF3] Enemy missing right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VF – MIA>


# <VF – Gank>
@module.rule("^VGG$")
def vgs_vgg(bot, trigger):
    bot.say("{}{}{}: [VGG] Gank!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VG1$")
def vgs_vg1(bot, trigger):
    bot.say("{}{}{}: [VG1] Gank left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VG2$")
def vgs_vg2(bot, trigger):
    bot.say("{}{}{}: [VG2] Gank middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VG2$")
def vgs_vg2(bot, trigger):
    bot.say("{}{}{}: [VG2] Gank right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VF – Gank>


# <VH – Help>
@module.rule("^VHH$")
def vgs_vhh(bot, trigger):
    bot.say("{}{}{}: [VHH] Help!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VHS$")
def vgs_vhs(bot, trigger):
    bot.say("{}{}{}: [VHS] Need healing!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VH1$")
def vgs_vh1(bot, trigger):
    bot.say("{}{}{}: [VH1] Help left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VH2$")
def vgs_vh2(bot, trigger):
    bot.say("{}{}{}: [VH2] Help middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VH3$")
def vgs_vh3(bot, trigger):
    bot.say("{}{}{}: [VH3] Help right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VH – Help>


# <VI – Incoming>
@module.rule("^VII$")
def vgs_vii(bot, trigger):
    bot.say("{}{}{}: [VII] Enemies incoming!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VI1$")
def vgs_vi1(bot, trigger):
    bot.say("{}{}{}: [VI1] Enemies incoming left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VI2$")
def vgs_vi2(bot, trigger):
    bot.say("{}{}{}: [VI2] Enemies incoming middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VI3$")
def vgs_vi3(bot, trigger):
    bot.say("{}{}{}: [VI3] Enemies incoming right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VI – Incoming>


# <VQ – Ward>
@module.rule("^VQF$")
def vgs_vqf(bot, trigger):
    bot.say("{}{}{}: [VQF] Ward Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQG$")
def vgs_vqg(bot, trigger):
    bot.say("{}{}{}: [VQG] Ward Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQN$")
def vgs_vqn(bot, trigger):
    bot.say("{}{}{}: [VQN] Need Wards!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQQ$")
def vgs_vqq(bot, trigger):
    bot.say("{}{}{}: [VQQ] Ward Here!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQ1$")
def vgs_vq1(bot, trigger):
    bot.say("{}{}{}: [VQ1] Ward Left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQ2$")
def vgs_vq2(bot, trigger):
    bot.say("{}{}{}: [VQ2] Ward middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VQ3$")
def vgs_vq3(bot, trigger):
    bot.say("{}{}{}: [VQ3] Ward Right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VQ – Ward>


# <VR – Retreat>
@module.rule("^VRJ$")
def vgs_vrj(bot, trigger):
    bot.say("{}{}{}: [VRJ] Retreat from the Jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VRR$")
def vgs_vrr(bot, trigger):
    bot.say("{}{}{}: [VRR] Retreat!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VRS$")
def vgs_vrs(bot, trigger):
    bot.say("{}{}{}: [VRS] Save yourself!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VR1$")
def vgs_vr1(bot, trigger):
    bot.say("{}{}{}: [VR1] Retreat left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VR2$")
def vgs_vr2(bot, trigger):
    bot.say("{}{}{}: [VR2] Retreat middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VR3$")
def vgs_vr3(bot, trigger):
    bot.say("{}{}{}: [VR3] Retreat right late!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VR – Retreat>


# <VS – Self>
@module.rule("^VSO$")
def vgs_vso(bot, trigger):
    bot.say("{}{}{}: [VSO] I'm on it!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSR$")
def vgs_vsr(bot, trigger):
    bot.say("{}{}{}: [VSR] Falling back!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSS$")
def vgs_vss(bot, trigger):
    bot.say("{}{}{}: [VSS] I'm building Stacks!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# <VSA – Self Attack>
@module.rule("^VSAA$")
def vgs_vsaa(bot, trigger):
    bot.say("{}{}{}: [VSAA] I'll attack!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSAF$")
def vgs_vsaf(bot, trigger):
    bot.say("{}{}{}: [VSAF] I'll attack Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSAG$")
def vgs_vsag(bot, trigger):
    bot.say("{}{}{}: [VSAG] I'll attack the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSAM$")
def vgs_vsam(bot, trigger):
    bot.say("{}{}{}: [VSAM] I'll attack the Titan!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSA1$")
def vgs_vsa1(bot, trigger):
    bot.say("{}{}{}: [VSA1] I'll attack left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSA2$")
def vgs_vsa2(bot, trigger):
    bot.say("{}{}{}: [VSA2] I'll attack middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSA3$")
def vgs_vsa3(bot, trigger):
    bot.say("{}{}{}: [VSA3] I'll attack right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VSA – Self Attack>
# <VSB – Self Buff>
@module.rule("^VSBB$")
def vgs_vsbb(bot, trigger):
    bot.say("{}{}{}: [VSBB] I'm going for jungle buff!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSBN$")
def vgs_vsbn(bot, trigger):
    bot.say("{}{}{}: [VSBN] I need the jungle buff!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSBT$")
def vgs_vsbt(bot, trigger):
    bot.say("{}{}{}: [VSBT] Take this jungle buff!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VSB – Self Buff>
# <VSD – Self Defend>
@module.rule("^VSDD$")
def vgs_vsdd(bot, trigger):
    bot.say("{}{}{}: [VSDD] I'll defend!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSDF$")
def vgs_vsdf(bot, trigger):
    bot.say("{}{}{}: [VSDF] I'll defend the Fire Giant!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSDG$")
def vgs_vsdg(bot, trigger):
    bot.say("{}{}{}: [VSDG] I'll defend the Gold Fury!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSDM$")
def vgs_vsdm(bot, trigger):
    bot.say("{}{}{}: [VSDM] I'll defend the Titan!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSD1$")
def vgs_vsd1(bot, trigger):
    bot.say("{}{}{}: [VSD1] I'll defend left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSD2$")
def vgs_vsd2(bot, trigger):
    bot.say("{}{}{}: [VSD2] I'll defend middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSD3$")
def vgs_vsd3(bot, trigger):
    bot.say("{}{}{}: [VSD3] I'll defend right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VSD – Self Defend>
# <VSG – Self Gank>
@module.rule("^VSGG$")
def vgs_vsgg(bot, trigger):
    bot.say("{}{}{}: [VSGG] I'll gank!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSG1$")
def vgs_vsg1(bot, trigger):
    bot.say("{}{}{}: [VSG1] I'll gank left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSG2$")
def vgs_vsg2(bot, trigger):
    bot.say("{}{}{}: [VSG2] I'll gank middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSG3$")
def vgs_vsg3(bot, trigger):
    bot.say("{}{}{}: [VSG3] I'll gank right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VSG – Self Gank>
# <VSQ – Self Ward>
@module.rule("^VSQQ$")
def vgs_vsqq(bot, trigger):
    bot.say("{}{}{}: [VSQQ] I will ward!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSQ1$")
def vgs_vsq1(bot, trigger):
    bot.say("{}{}{}: [VSQ1] I will ward left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSQ2$")
def vgs_vsq2(bot, trigger):
    bot.say("{}{}{}: [VSQ2] I will ward middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSQ3$")
def vgs_vsq3(bot, trigger):
    bot.say("{}{}{}: [VSQ3] I will ward right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VSQ – Self Ward>
# <VST – Self Returned>
@module.rule("^VSTB$")
def vgs_vstb(bot, trigger):
    bot.say("{}{}{}: [VSTB] I'm returning to base!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VSTT$")
def vgs_vstt(bot, trigger):
    bot.say("{}{}{}: [VSTT] I have returned!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VST1$")
def vgs_vst1(bot, trigger):
    bot.say("{}{}{}: [VST1] I'm returning left lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VST2$")
def vgs_vst2(bot, trigger):
    bot.say("{}{}{}: [VST2] I'm returning middle lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VST3$")
def vgs_vst3(bot, trigger):
    bot.say("{}{}{}: [VST3] I'm returning right lane!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VST – Self Returned>
# </VS – Self>


# <VT – Enemies Returned>
@module.rule("^VTT$")
def vgs_vtt(bot, trigger):
    bot.say("{}{}{}: [VTT] Enemies have returned!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VT1$")
def vgs_vt1(bot, trigger):
    bot.say("{}{}{}: [VT1] Enemies have returned left!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VT2$")
def vgs_vt2(bot, trigger):
    bot.say("{}{}{}: [VT2] Enemies have returned middle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VT3$")
def vgs_vt3(bot, trigger):
    bot.say("{}{}{}: [VT3] Enemies have returned right!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VT – Enemies Returned>


# <VV – Other>
@module.rule("^VVA$")
def vgs_vva(bot, trigger):
    bot.say("{}{}{}: [VVA] Ok!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVB$")
def vgs_vvb(bot, trigger):
    bot.say("{}{}{}: [VVB] Be right back!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVC$")
def vgs_vvc(bot, trigger):
    bot.say("{}{}{}: [VVC] Completed!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVK$")
def vgs_vvk(bot, trigger):
    bot.say("{}{}{}: [VVK] Stepping away for a moment.".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVM$")
def vgs_vvm(bot, trigger):
    bot.say("{}{}{}: [VVM] Out of mana!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

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
# <VVG – General>
@module.rule("^VVGB$")
def vgs_vvgb(bot, trigger):
    bot.say("{}{}{}: [VVGB] Bye!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGF$")
def vgs_vvgf(bot, trigger):
    bot.say("{}{}{}: [VVGF] Have fun!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGG$")
def vgs_vvgg(bot, trigger):
    bot.say("{}{}{}: [VVGG] Good game!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVGH$")
def vgs_vvgh(bot, trigger):
    bot.say("{}{}{}: [VVGH] Hi!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

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
# </VVG – General>
# <VVV – Position>
@module.rule("^VVVA$")
def vgs_vvva(bot, trigger):
    bot.say("{}{}{}: [VVVA] Set up an ambush here!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVB$")
def vgs_vvvb(bot, trigger):
    bot.say("{}{}{}: [VVVB] Behind us!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVC$")
def vgs_vvvc(bot, trigger):
    bot.say("{}{}{}: [VVVC] Chase the enemy!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVD$")
def vgs_vvvd(bot, trigger):
    bot.say("{}{}{}: [VVVD] Ultimate is down! ({} remaining)".format("\x0311", "\u200B".join(trigger.nick), "\x0315", decimal.Decimal(random.randrange(141)) / 100)

@module.rule("^VVVE$")
def vgs_vvve(bot, trigger):
    bot.say("{}{}{}: [VVVE] On my way!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVF$")
def vgs_vvvf(bot, trigger):
    bot.say("{}{}{}: [VVVF] Follow me!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVG$")
def vgs_vvvg(bot, trigger):
    bot.say("{}{}{}: [VVVG] Group up!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVJ$")
def vgs_vvvj(bot, trigger):
    bot.say("{}{}{}: [VVVJ] Going into the jungle!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVP$")
def vgs_vvvp(bot, trigger):
    bot.say("{}{}{}: [VVVP] Split push!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVR$")
def vgs_vvvr(bot, trigger):
    bot.say("{}{}{}: [VVVR] Ultimate is ready!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVS$")
def vgs_vvvs(bot, trigger):
    bot.say("{}{}{}: [VVVS] Stay here!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVT$")
def vgs_vvvt(bot, trigger):
    bot.say("{}{}{}: [VVVT] It's a trap!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVW$")
def vgs_vvvw(bot, trigger):
    bot.say("{}{}{}: [VVVW] Place a Ward for teleport!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))

@module.rule("^VVVX$")
def vgs_vvvx(bot, trigger):
    bot.say("{}{}{}: [VVVX] Spread Out!".format("\x0311", "\u200B".join(trigger.nick), "\x0315"))
# </VVV – Position>
# </VV – Other>


# <VX – Social Emotes>
# VXW = No solution for [Wave] atm
# VXD = No solution for [Dance] atm
# VXC = No solution for [Clap] atm
# VXS = No solution for [Special] atm
# VXF = No solution for [Furious] atm
# VXG = No solution for [Special 2] atm
# VXE = No solution for [Global Emote] atm
# </VX – Social Emotes>
