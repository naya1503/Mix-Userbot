################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from pyrogram.types import *

from Mix import *

__modles__ = "Emoji"
__help__ = get_cgr("help_emo")


@ky.ubot("setemo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()

    xx = await m.edit(cgr("proses").format(em.proses))
    rep = m.reply_to_message
    if not rep:
        rep = m

    emoji_id = None
    if rep.entities:
        for entity in rep.entities:
            if entity.custom_emoji_id:
                emoji_id = entity.custom_emoji_id
                await c.set_emoji_status(EmojiStatus(custom_emoji_id=emoji_id))
                await xx.edit(cgr("em_25").format(em.sukses, emoji_id))
                return
    await xx.edit(cgr("em_5").format(em.gagal))
    return

    prem = c.me.is_premium
    if prem:
        if emoji_id:
            await c.set_emoji_status(EmojiStatus(custom_emoji_id=emoji_id))
            await xx.edit(cgr("em_25").format(em.sukses, emoji_id))
            return
        else:
            await xx.edit(cgr("em_5").format(em.gagal))
            return
    else:
        await xx.edit(cgr("em_2").format(em.gagal))
        return


"""
@ky.ubot("setemo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.edit(cgr("proses").format(em.proses))
    emoji = m.reply_to_message
    prem = c.me.is_premium
    if prem == True:
        if emoji.entities:
            for entity in emoji.entities:
                if entity.custom_emoji_id:
                    emoji_id = entity.custom_emoji_id
                    break
            if emoji_id:
                await c.set_emoji_status(EmojiStatus(custom_emoji_id=emoji_id))
                await xx.edit(cgr("em_25").format(em.sukses, emoji_id))
                return

    elif prem == False:
        await xx.edit(cgr("em_2").format(em.gagal))
        return
    else:
        await xx.edit(cgr("em_3").format(em.gagal))
        return
"""


@ky.ubot("emoid", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.edit(cgr("proses").format(em.proses))
    emoji = m.reply_to_message
    if emoji.entities:
        for entot in emoji.entities:
            if entot.custom_emoji_id:
                emoid = entot.custom_emoji_id
                await xx.edit(cgr("em_4").format(em.sukses, emoid))
                return
            else:
                await xx.edit(cgr("em_3").format(em.gagal))
                return


@ky.ubot("emoji", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    gua = c.me.is_premium
    jing = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) < 3:
        return await jing.edit(cgr("em_5").format(em.gagal, m.command))
    command, variable, value = m.command[:3]
    emoji_id = None
    if variable.lower() == "ping":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_ping", emoji_id)
                    await jing.edit(cgr("em_6").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_ping", value)
            await jing.edit(cgr("em_7").format(em.sukses, value))
            return
    elif variable.lower() == "pong":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_pong", emoji_id)
                    await jing.edit(cgr("em_8").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_pong", value)
            await jing.edit(cgr("em_9").format(em.sukses, value))
            return
    elif variable.lower() == "proses":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_proses", emoji_id)
                    await jing.edit(cgr("em_10").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_proses", value)
            await jing.edit(cgr("em_11").format(em.sukses, value))
            return
    elif variable.lower() == "gagal":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_gagal", emoji_id)
                    await jing.edit(cgr("em_12").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_gagal", value)
            await jing.edit(cgr("em_13").format(em.sukses, value))
            return
    elif variable.lower() == "sukses":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_sukses", emoji_id)
                    await jing.edit(cgr("em_14").format(em.sukses, emoji_id, value))
        elif gua == False:
            udB.set_var(c.me.id, "emo_sukses", value)
            await jing.edit(cgr("em_15").format(em.sukses, value))
            return
    elif variable.lower() == "profil":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_profil", emoji_id)
                    await jing.edit(cgr("em_16").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_profil", value)
            await jing.edit(cgr("em_17").format(em.sukses, value))
            return
    elif variable.lower() == "alive":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_alive", emoji_id)
                    await jing.edit(cgr("em_18").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_alive", value)
            await jing.edit(cgr("em_19").format(em.sukses, value))
            return
    elif variable.lower() == "warn":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_warn", emoji_id)
                    await jing.edit(cgr("em_20").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_warn", value)
            await jing.edit(cgr("em_21").format(em.sukses, value))
            return
    elif variable.lower() == "block":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_block", emoji_id)
                    await jing.edit(cgr("em_22").format(em.sukses, emoji_id, value))
                    return
        elif gua == False:
            udB.set_var(c.me.id, "emo_block", value)
            await jing.edit(cgr("em_23").format(em.sukses, value))
            return

    else:
        await jing.edit(cgr("em_5").format(em.gagal, m.command))
        return


@ky.ubot("getemo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(cgr("proses").format(em.proses))
    await xx.edit(
        cgr("em_24").format(
            em.sukses,
            em.ping,
            em.pong,
            em.proses,
            em.sukses,
            em.gagal,
            em.profil,
            em.alive,
            em.warn,
            em.block,
        )
    )
