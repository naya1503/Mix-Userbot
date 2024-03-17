import random

from pyrogram.enums import MessagesFilter

from Mix import *

__modles__ = "Asupan"
__help__ = get_cgr("help_asupan")


@ky.ubot("asupan", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    y = await m.reply_text(cgr("proses").format(em.proses))
    try:
        asupannya = []
        async for asupan in c.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(m.chat.id, reply_to_message_id=m.id)
        await y.delete()
    except Exception as error:
        await y.edit(cgr("err").format(em.gagal, error))


@ky.ubot("cewek|cewe", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    y = await m.reply_text(cgr("proses").format(em.proses))
    try:
        ayangnya = []
        async for ayang in c.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(m.chat.id, reply_to_message_id=m.id)
        await y.delete()
    except Exception as error:
        await y.edit(cgr("err").format(em.gagal, error))


@ky.ubot("cowok|cowo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    y = await m.reply_text(cgr("proses").format(em.proses))
    try:
        ayang2nya = []
        async for ayang2 in c.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(m.chat.id, reply_to_message_id=m.id)
        await y.delete()
    except Exception as error:
        await y.edit(cgr("err").format(em.gagal, error))


@ky.ubot("anime", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    y = await m.reply_text(cgr("proses").format(em.proses))
    anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in c.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(m.chat.id, reply_to_message_id=m.id)
        await y.delete()
    except Exception as error:
        await y.edit(cgr("err").format(em.gagal, error))


@ky.ubot("bokep", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    y = await m.reply_text(cgr("proses").format(em.proses))
    if m.chat.id in NO_GCAST:
        await y.edit("**Ini GC Support GOBLOK!!**")
        return
    try:
        await c.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in c.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(m.chat.id, reply_to_message_id=m.id)
        await y.delete()
    except Exception as error:
        await y.edit(cgr("err").format(em.gagal, error))
    if c.me.id == OWNER_ID:
        return
    await c.leave_chat(-1001867672427)
