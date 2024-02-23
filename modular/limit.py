from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from Mix import *

__modles__ = "Spambot"
__help__ = """
Help Command Spambot

• Perintah: <code>{0}limit</code>
• Penjelasan: Untuk melihat status akun anda dibatasi atau tidak.
"""


@ky.ubot("limit")
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    await c.unblock_user("SpamBot")
    xin = await c.resolve_peer("SpamBot")
    msg = await m.reply(f"{em.proses} <b>Processing...</b>")
    response = await c.invoke(
        StartBot(
            bot=xin,
            peer=xin,
            random_id=c.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await c.get_messages("SpamBot", response.updates[1].message.id + 1)
    if status:
        result = status.text
        emoji = None
        if "Good news" in result or "Kabar baik" in result:
            emoji = f"{em.sukses}"
        if "I'm afraid" in result or "Saya khawatir" in result:
            emoji = f"{em.gagal}"
        await c.send_message(
            m.chat.id, f"{emoji} <b>{result}</b>\n\n ~ {em.alive} <b>{x.first_name}</b>"
        )
        await c.invoke(DeleteHistory(peer=xin, max_id=0, revoke=True))
        await msg.delete()
        return
