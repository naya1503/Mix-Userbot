import os

from pyrogram import *
from pyrogram.types import *
from lyricsgenius import genius
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from Mix import *

api = genius.Genius(genius_api,verbose=False)

@ky.ubot("lyric", sudo=True)
async def _(c ,m):
    em = Emojik()
    em.initialize()
    if len(m.command) == 1:
        return await m.reply(f"{em.gagal} <b> Berikan judul lagu</b>")

    load = await m.reply(f"{em.proses} <b>Sedang proses...</>")
    song_name = m.text.split(None, 1)[1]

    lirik = api.search_song(song_name)

    if lirik is None:return await load.edit("__No lyrics found for your query...__")

    lyric_title = lirik.title
    lyric_artist = lirik.artist
    lyrics_text = lirik.lyrics

    try:
        await load.edit_text(f"__--**{lyric_title}**--__\n__{lyric_artist}\n__\n\n__{lyrics_text}__\n__Extracted by {bot.me.username}")

    except MessageTooLong:
        with open(f"downloads/{lyric_title}.txt","w") as f:
            f.write(f"{lyric_title}\n{lyric_artist}\n\n\n{lyrics_text}")

        await load.edit_text("__Lyric too long. Sending as a text file...__")
        await m.reply_chat_action(
            action="upload_document"
        )
        await m.reply_document(
            document=f"downloads/{lyric_title}.txt",
            thumb="https://telegra.ph//file/43cec0ae0ded594b55247.jpg",
            caption=f"\n__--{lyric_title}--__\n__{lyric_artist}__\n\n__Extracted by {bot.me.username}__"
        )

        await load.delete()
        
        
        os.remove(f"downloads/{lyric_title}.txt")