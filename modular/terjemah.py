################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os

import gtts
from gpytranslate import Translator

from Mix import *
from Mix.core.parser import kode_bahasa

__modles__ = "Translate"
__help__ = """
 Help Command Translate

• Perintah : <code>{0}tts</code>
• Penjelasan : Untuk membuat teks menjadi voice.

• Perintah : <code>{0}tr</code>
• Penjelasan : Untuk menerjemahkan teks bahasa.

• Perintah : <code>{0}lang</code>
• Penjelasan : Untuk melihat daftar dan kode bahasa.

• Perintah : <code>{0}setlang</code>
• Penjelasan : Untuk mengatur kode bahasa menyangkut tts dan tr.
"""


@ky.ubot("tts", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(f"{em.proses} Processing...")
    if m.reply_to_message:
        bhs = c._translate[c.me.id]["negara"]
        kata = m.reply_to_message.text or m.reply_to_message.caption
    else:
        if len(m.command) < 2:
            await pros.edit(
                f"{em.gagal} Gunakan format :`{m.command}` [berikan teks/balas pesan]"
            )
        else:
            bhs = c._translate[c.me.id]["negara"]
            kata = m.text.split(None, 1)[1]
    gts = gtts.gTTS(kata, lang=bhs)
    gts.save("trs.oog")
    rep = m.reply_to_message or m
    try:
        await c.send_voice(
            chat_id=m.chat.id,
            voice="trs.oog",
            reply_to_message_id=rep.id,
        )
        await pros.delete()
        os.remove("trs.oog")
        return
    except Exception as er:
        await pros.edit(f"{em.gagal} Error: {er}")
        return
    except FileNotFoundError:
        pass


@ky.ubot("tr", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    trans = Translator()
    pros = await m.reply(f"{em.proses} Processing...")
    if m.reply_to_message:
        bhs = c._translate[c.me.id]["negara"]
        txt = m.reply_to_message.text or m.reply_to_message.caption
        src = await trans.detect(txt)
    else:
        if len(m.command) < 2:
            await m.reply(f"{em.gagal} `{m.command}` [balas ke pesan]")
            return
        else:
            bhs = c._translate[c.me.id]["negara"]
            txt = m.text.split(None, 1)[1]
            src = await trans.detect(txt)
    trsl = await trans(txt, sourcelang=src, targetlang=bhs)
    reply = f"{em.sukses} `{trsl.text}`"
    rep = m.reply_to_message or m
    await pros.delete()
    await c.send_message(m.chat.id, reply, reply_to_message_id=rep.id)


@ky.ubot("lang", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    try:
        bhs_list = "\n".join(
            f"- **{lang}**: `{code}`" for lang, code in kode_bahasa.items()
        )
        await m.reply(f"{em.sukses} **Daftar Kode Bahasa:**\n{bhs_list}")
        return
    except Exception as e:
        await m.reply(f"{em.gagal} Error: {e}")
        return


@ky.ubot("setlang", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(f"{em.proses} Processing...")
    if len(m.command) < 2:
        await pros.edit(
            f"{em.gagal} Silahkan berikan kode bahasa!\nContoh : `{m.command}` id."
        )
        return
    for lang, code in kode_bahasa.items():
        kd = m.text.split(None, 1)[1]
        if kd.lower() == code.lower():
            c._translate[c.me.id] = {"negara": kd}
            await pros.edit(f"{em.sukses} Kode bahasa diganti ke : `{kd}` - **{lang}**")
            return
    await pros.edit(f"{em.gagal} Kode bahasa tidak valid atau tidak ditemukan.")
            return
            
