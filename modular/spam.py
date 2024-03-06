################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio

from pyrogram.errors import *

from Mix import *

dispam = []

berenti = False

__modles__ = "Spam"
__help__ = """
Help Command Spam 

• Perintah: <code>{0}dspam</code> [jumlah] [waktu delay] [balas pesan]
• Penjelasan: Untuk melakukan delay spam.

• Perintah: <code>{0}spam</code> [jumlah] [kata]
• Penjelasan: Untuk melakukan spam.

• Perintah: <code>{0}cspam</code>
• Penjelasan: Untuk stop spam.

• Perintah: <code>{0}dspamfw</code> [jumlah] [waktu delay] [link channel public]
• Penjelasan: Untuk melakukan delay spam forward link channel.
"""


@ky.ubot("spam", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    global berenti
    reply = m.reply_to_message
    msg = await m.reply(f"{em.proses} Processing...")
    berenti = True

    if reply:
        try:
            count_message = int(m.command[1])
            for i in range(count_message):
                if not berenti:
                    break
                await reply.copy(m.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            return await msg.edit(str(error))
    else:
        if len(m.command) < 2:
            return await msg.edit(
                f"{em.gagal} Silakan ketik <code>{m.command}</code> untuk bantuan perintah."
            )
        else:
            try:
                count_message = int(m.command[1])
                for i in range(count_message):
                    if not berenti:
                        break
                    await m.reply(
                        m.text.split(None, 2)[2],
                    )
                    await asyncio.sleep(0.1)
            except Exception as error:
                return await msg.edit(str(error))
    berenti = False

    await msg.delete()
    await m.delete()


@ky.ubot("dspam", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    global berenti

    reply = m.reply_to_message
    msg = await m.reply(f"{em.proses} Processing...")
    berenti = True
    if reply:
        try:
            count_message = int(m.command[1])
            count_delay = int(m.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        for i in range(count_message):
            if not berenti:
                break
            try:
                await reply.copy(m.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
    else:
        if len(m.command) < 4:
            return await msg.edit(
                f"{em.gagal} Silakan ketik <code>{m.command}</code> untuk bantuan perintah."
            )
        else:
            try:
                count_message = int(m.command[1])
                count_delay = int(m.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            for i in range(count_message):
                if not berenti:
                    break
                try:
                    await m.reply(m.text.split(None, 3)[3])
                    await asyncio.sleep(count_delay)
                except:
                    pass

    berenti = False

    await msg.delete()
    await m.delete()


@ky.ubot("cspam", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    global berenti
    if not berenti:
        return await m.reply(f"{em.gagal} Sedang tidak ada perintah spam disini.")
    berenti = False
    await m.reply(f"{em.sukses} Ok spam berhasil dihentikan.")
    return


@ky.ubot("dspamfw", sudo=True)
async def _(c: user, message):
    em = Emojik()
    em.initialize()
    global berenti
    message.reply_to_message
    reply = await message.reply(f"{em.proses} Processing...")
    berenti = True

    try:
        _, count_str, delay_str, link = message.text.split(maxsplit=3)
        count = int(count_str)
        delay = int(delay_str)
    except ValueError:
        await reply.reply(
            "Format perintah tidak valid. Gunakan: /ldlpm <jumlah> <delay> <link>"
        )
        return

    chat_id, message_id = link.split("/")[-2:]

    try:
        chat_id = int(chat_id)
    except ValueError:
        pass

    message_id = int(message_id)

    for _ in range(count):
        try:
            if not berenti:
                break
            forwarded_message = await c.get_messages(chat_id, message_id)
            await c.forward_messages(message.chat.id, chat_id, message_ids=message_id)
            await reply.delete()
            await asyncio.sleep(delay)
        except (MessageNotModified, MediaEmpty, BadRequest, Forbidden) as e:
            if isinstance(e, Forbidden) and "is restricted" in str(e):
                await reply.reply("Anda dibatasi untuk melakukan tindakan ini.")
            elif isinstance(e, Forbidden) and "can't send media messages" in str(e):
                await reply.reply("Anda tidak dapat mengirim pesan media.")
            elif isinstance(e, Forbidden) and "can't send photos" in str(e):
                await reply.reply("Anda tidak dapat mengirim foto.")
            else:
                reply.delete()
                break
        except Exception as e:
            await reply.reply(f"Gagal meneruskan pesan: {str(e)}")
            break

        if forwarded_message.media:
            continue
        text = forwarded_message.text
        await reply.edit(text)
    berenti = False
    reply.delete()
