from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from Mix import *

__modles__ = "Spambot"
__help__ = get_cgr("help_limt")


@ky.ubot("limit", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    await c.unblock_user("SpamBot")
    xin = await c.resolve_peer("SpamBot")
    msg = await m.reply(cgr("proses").format(em.proses))
    rsp = await c.invoke(
        StartBot(
            bot=xin,
            peer=xin,
            random_id=c.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await c.get_messages("SpamBot", rsp.updates[1].message.id + 1)
    if status:
        result = status.text
        emoji = None
        if "Good news" in result or "Kabar baik" in result:
            emoji = f"{em.sukses}"
        if "We afraid" in result or "Kami khawatir" in result:
            emoji = f"{em.warn}"
        await c.send_message(
            m.chat.id, cgr("lmt_1").format(emoji, result, em.alive, c.me.first_name)
        )
        await c.invoke(DeleteHistory(peer=xin, max_id=0, revoke=True))
        await msg.delete()
        return
