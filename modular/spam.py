################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio

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


@ky.ubot("dlpm", sudo=True)
async def _(c: user, message):
    em = Emojik()
    em.initialize()

    reply_to_message = message.reply_to_message
    reply = await message.reply(f"{em.proses} Processing...")

    try:
        _, count_str, delay_str, link = message.text.split(maxsplit=3)
        count = int(count_str)
        delay = int(delay_str)
    except ValueError:
        await reply.edit(
            "Format perintah tidak valid. Gunakan: /ldlpm <jumlah> <delay> <link>"
        )
        return

    chat_id, message_id = link.split("/")[-2:]
    
    try:
        chat_id = int(chat_id)  # Coba ubah ke integer
    except ValueError:
        pass  # Biarkan chat_id tetap string jika tidak dapat diubah menjadi integer

    message_id = int(message_id)

    # Forward pesan dari tautan
    for _ in range(count):
        await asyncio.sleep(delay)
        try:
            forwarded_message = await client.get_messages(chat_id, message_id)
            await client.forward_messages(
                message.chat.id, chat_id, message_ids=message_id
            )
        except Exception as e:
            await reply.edit(f"Gagal meneruskan pesan: {str(e)}")
            break

        # Mengekstrak pesan dari tautan
        if forwarded_message.media:
            await reply.edit("Tidak bisa mengekstrak pesan yang berisi media.")
        else:
            text = forwarded_message.text
            await reply.edit(text)