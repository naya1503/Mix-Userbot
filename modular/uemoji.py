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
async def _(c: user, m):
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


@ky.ubot("emoid", sudo=True)
async def _(c: user, m):
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
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    gua = c.me.is_premium
    jing = await m.reply(f"{em.proses} <b>Processing...</b>")
    if len(m.command) < 3:
        return await jing.edit(
            f"{em.gagal} <b>Gunakan Format : <code>emoji variable value</code>.</b>"
        )
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
                    await jing.edit(
                        f"{em.sukses} <b>Emoji ping diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_ping", value)
            await jing.edit(f"{em.sukses} <b>Emoji ping diset ke :</b> {value}")
    elif variable.lower() == "pong":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_pong", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji pong diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_pong", value)
            await jing.edit(f"{em.sukses} <b>Emoji pong diset ke :</b> {value}")
    elif variable.lower() == "proses":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_proses", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji proses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_proses", value)
            await jing.edit(f"{em.sukses} <b>Emoji proses diset ke :</b> {value}")
    elif variable.lower() == "gagal":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_gagal", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji gagal diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_gagal", value)
            await jing.edit(f"{em.sukses} <b>Emoji gagal diset ke :</b> {value}")
    elif variable.lower() == "sukses":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_sukses", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji sukses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_sukses", value)
            await jing.edit(f"{em.sukses} <b>Emoji sukses diset ke :</b> {value}")
    elif variable.lower() == "profil":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_profil", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji profil diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_profil", value)
            await jing.edit(f"{em.sukses} <b>Emoji profil diset ke :</b> {value}")
    elif variable.lower() == "alive":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_alive", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji alive diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )

        elif gua == False:
            udB.set_var(c.me.id, "emo_alive", value)
            await jing.edit(f"{em.sukses} <b>Emoji alive diset ke :</b> {value}")
    elif variable.lower() == "warn":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_warn", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji alive diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )

        elif gua == False:
            udB.set_var(c.me.id, "emo_warn", value)
            await jing.edit(f"{em.sukses} <b>Emoji warn diset ke :</b> {value}")
    elif variable.lower() == "block":
        if gua == True:
            if m.entities:
                for entity in m.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    udB.set_var(c.me.id, "emo_block", emoji_id)
                    await jing.edit(
                        f"{em.sukses} <b>Emoji block diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )

        elif gua == False:
            udB.set_var(c.me.id, "emo_block", value)
            await jing.edit(f"{em.sukses} <b>Emoji block diset ke :</b> {value}")

    else:
        await jing.edit(
            f"{em.gagal} <b>Silakan ketik <code>help {m.command}<code>.</b>"
        )


@ky.ubot("getemo", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    xx = await m.reply(f"{em.proses} <b>Processing...</b>")
    await xx.edit(
        f"{em.sukses}<b>๏ Emoji Yang Digunakan :</b>\n\n Ping : {em.ping}\n Pong : {em.pong}\n Proses : {em.proses}\n Sukses : {em.sukses}\n Gagal : {em.gagal}\n Profil : {em.profil}\n Alive : {em.alive}\n Warning : {em.warn}\n Block : {em.block}"
    )
