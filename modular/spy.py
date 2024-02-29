################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

__modles__ = "Curi"
__help__ = """
Help Command Curi

• Perintah: <code>{0}curi or spy</code>
• Penjelasan: Untuk mencuri pap timer (bukan sekali lihat).
"""


import os

from Mix import *

"""

@ky.ubot("curi|spy", sudo=True)
async def _(c: user, m):
    dia = m.reply_to_message
    if not dia:
        return
    anjing = dia.caption or ""
    await m.delete()
    logs = udB.get_logger(c.me.id)
    if dia.photo:
        anu = await c.download_media(dia)
        if logs:
            await c.send_photo(logs, anu, anjing)
        else:
            await c.send_photo("me", anu, anjing)
        os.remove(anu)
    if dia.video:
        anu = await c.download_media(dia)
        if logs:
            await c.send_video(logs, anu, anjing)
        else:
            await c.send_video("me", anu, anjing)
        os.remove(anu)
    if dia.audio:
        anu = await c.download_media(dia)
        if logs:
            await c.send_audio(logs, anu, anjing)
        else:
            await c.send_audio("me", anu, anjing)
        os.remove(anu)
    if dia.voice:
        anu = await c.download_media(dia)
        if logs:
            await c.send_voice(logs, anu, anjing)
        else:
            await c.send_voice("me", anu, anjing)
        os.remove(anu)
    if dia.document:
        anu = await c.download_media(dia)
        if logs:
            await c.send_document(logs, anu, anjing)
        else:
            await c.send_document("me", anu, anjing)
        os.remove(anu)
    else:
        if logs:
            await c.send_message(logs, "Hasil Curi!")
        else:
            await c.send_message("me", "Hasil Curi!")
"""

@ky.ubot("curi|spy", sudo=True)
async def _(c: user, m):
    dia = m.reply_to_message
    if not dia:
        return
    anjing = dia.caption or ""
    await m.delete()
    logs = udB.get_logger(c.me.id)
    
    if dia.photo or dia.video or dia.audio or dia.voice or dia.document:
        anu = await c.download_media(dia)
        
        if os.path.getsize(anu) == 0:
            os.remove(anu)
            if logs:
                await c.send_message(logs, "Gagal mengunduh file. File kosong.")
            else:
                await c.send_message("me", "Gagal mengunduh file. File kosong.")
            return
        
        try:
            if dia.photo:
                if logs:
                    await c.send_photo(logs, anu, anjing)
                else:
                    await c.send_photo("me", anu, anjing)
            elif dia.video:
                if logs:
                    await c.send_video(logs, anu, anjing)
                else:
                    await c.send_video("me", anu, anjing)
            elif dia.audio:
                if logs:
                    await c.send_audio(logs, anu, anjing)
                else:
                    await c.send_audio("me", anu, anjing)
            elif dia.voice:
                if logs:
                    await c.send_voice(logs, anu, anjing)
                else:
                    await c.send_voice("me", anu, anjing)
            elif dia.document:
                if logs:
                    await c.send_document(logs, anu, anjing)
                else:
                    await c.send_document("me", anu, anjing)
        except Exception as e:
            print(f"Error saat mengirim media: {e}")
        finally:
            os.remove(anu)
    else:
        if logs:
            await c.send_message(logs, "Hasil Curi!")
        else:
            await c.send_message("me", "Hasil Curi!")
