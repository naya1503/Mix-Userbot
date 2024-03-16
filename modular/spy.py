################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os

from Mix import *

__modles__ = "Curi"
__help__ = get_cgr("help_spy")


@ky.ubot("curi|spy", sudo=True)
async def _(c: nlx, m):
    dia = m.reply_to_message
    if not dia:
        return
    anjing = dia.caption or ""
    await m.delete()

    if dia.photo or dia.video or dia.audio or dia.voice or dia.document:
        anu = await c.download_media(dia)

        if os.path.getsize(anu) == 0:
            os.remove(anu)
            if TAG_LOG:
                await c.send_message(TAG_LOG, cgr("spy_1").format(em.gagal))
            else:
                await c.send_message("me", cgr("spy_1").format(em.gagal))
            return

        try:
            if dia.photo:
                if TAG_LOG:
                    await c.send_photo(TAG_LOG, anu, anjing)
                else:
                    await c.send_photo("me", anu, anjing)
            elif dia.video:
                if TAG_LOG:
                    await c.send_video(TAG_LOG, anu, anjing)
                else:
                    await c.send_video("me", anu, anjing)
            elif dia.audio:
                if TAG_LOG:
                    await c.send_audio(TAG_LOG, anu, anjing)
                else:
                    await c.send_audio("me", anu, anjing)
            elif dia.voice:
                if TAG_LOG:
                    await c.send_voice(TAG_LOG, anu, anjing)
                else:
                    await c.send_voice("me", anu, anjing)
            elif dia.document:
                if TAG_LOG:
                    await c.send_document(TAG_LOG, anu, anjing)
                else:
                    await c.send_document("me", anu, anjing)
        except Exception as e:
            if TAG_LOG:
                await c.send_message(TAG_LOG, cgr("err").format(em.gagal, e))
            else:
                await c.send_message("me", cgr("err").format(em.gagal, e))
        finally:
            os.remove(anu)
    else:
        if TAG_LOG:
            await c.send_message(TAG_LOG, cgr("spy_2").format(em.sukses))
        else:
            await c.send_message("me", cgr("spy_2").format(em.sukses))
