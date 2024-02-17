################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

__modles__ = "Emoji"
__help__ = """
 Help Command Emoji

• Perintah: <code>{0}emoji</code> [variable] [value]
• Penjelasan: Untuk mengubah tampilan emoji.

• Perintah: <code>{0}emoid</code> [reply emoji]
• Penjelasan: Untuk mengubah tampilan emoji.

• Perintah: <code>{0}getemo</code>
• Penjelasan: Untuk melihat tampilan emoji.

• Contoh pengunaan set emoji :

<code>{0}emoji ping 🏓</code>
<code>{0}emoji pong 🥵</code>
<code>{0}emoji proses 🔄</code>
<code>{0}emoji sukses ✅</code>
<code>{0}emoji gagal ❌</code>
<code>{0}emoji profil 👤</code>
<code>{0}emoji alive ⭐</code>
"""

@ky.ubot("emoid", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    xx = await m.edit(f"{emo.proses} <b>Processing...</b>")
    emoji = m.reply_to_message
    if emoji.entities:
        for entot in emoji.entities:
            if entot.custom_emoji_id:
                emoid = entot.custom_emoji_id
                await xx.edit(
                    f"{emo.sukses} <b>Custom Emoji ID : <code>{emoid}</code>.</b>"
                )
            else:
                await xx.edit(f"{emo.gagal} <b>Reply ke Custom Emoji.</b>")


@ky.ubot("emoji", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    gua = c.me.is_premium
    jing = await m.reply(f"{emo.proses} <b>Processing...</b>")
    if len(m.command) < 3:
        return await jing.edit(
            f"{emo.gagal} <b>Gunakan Format : <code>setvar variable value</code>.</b>"
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
                        f"{emo.sukses} <b>Emoji ping diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_ping", value)
            await jing.edit(f"{emo.sukses} <b>Emoji ping diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji pong diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_pong", value)
            await jing.edit(f"{emo.sukses} <b>Emoji pong diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji proses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_proses", value)
            await jing.edit(f"{emo.sukses} <b>Emoji proses diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji gagal diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_gagal", value)
            await jing.edit(f"{emo.sukses} <b>Emoji gagal diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji sukses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_sukses", value)
            await jing.edit(f"{emo.sukses} <b>Emoji sukses diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji profil diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_profil", value)
            await jing.edit(f"{emo.sukses} <b>Emoji profil diset ke :</b> {value}")
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
                        f"{emo.sukses} <b>Emoji profil diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            udB.set_var(c.me.id, "emo_alive", value)
            await jing.edit(f"{emo.sukses} <b>Emoji profil diset ke :</b> {value}")
    else:
        await jing.edit(
            f"{emo.gagal} <b>Silakan ketik <code>help {m.text}<code>.</b>"
        )


@ky.ubot("getemo", sudo=True)
async def _(c: user, m):
    xx = await m.reply(f"{emo.proses} <b>Processing...</b>")
    await xx.edit(
        f"{emo.sukses} <b>๏ Emoji Yang Digunakan :</b>\n\n Ping : {emo.ping}\n Pong : {emo.pong}\n Proses : {emo.proses}\n Sukses : {emo.sukses}\n Gagal : {emo.gagal}\n Profil : {emo.profil}\n Alive : {emo.alive}"
    )
