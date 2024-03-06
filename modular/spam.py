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

    reply = message.reply_to_message
    msg = await message.reply(f"{em.proses} Processing...")

    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
            link = message.text.split(None, 3)[3]
        except Exception as error:
            return await msg.edit(str(error))

        for i in range(count_message):
            try:
                await reply.copy(message.chat.id, text=link)
                await asyncio.sleep(count_delay)
            except:
                pass
    else:
        if len(message.command) < 4:
            return await msg.edit(
                f"{em.gagal} Please type <code>{message.command}</code> for command help."
            )
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
                link = message.text.split(None, 3)[3]
            except Exception as error:
                return await msg.edit(str(error))

            for i in range(count_message):
                try:
                    await message.reply(link)
                    await asyncio.sleep(count_delay)
                except:
                    pass

    await msg.delete()


"""
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
            link = m.text.split(None, [3])
        except Exception as error:
            return await msg.edit(str(error))
        for i in range(count_message):
            if not berenti:
                break
            try:
                await reply.copy(m.chat.id, text=link)
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
                link = m.text.split(m.command[3])
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
"""
