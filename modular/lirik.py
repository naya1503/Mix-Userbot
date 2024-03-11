import requests
from lyricsgenius import Genius
from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Lyric"
__help__ = "Lyrics"


api = Genius(
    "mJIaLonIWBIhEVZrclZIGtBdrIdSKpxa2ODPwIJMp3hxYxUlAt5ZS6-Z4nXWMH6V", verbose=False
)


@ky.ubot("lyric", sudo=True)
async def get_lyrics(c, m):
    em = Emojik()
    em.initialize()
    song_title = " ".join(m.command[1:])
    search_url = f"https://api.genius.com/search?q={song_title}"
    headers = {
        "Authorization": "Bearer mJIaLonIWBIhEVZrclZIGtBdrIdSKpxa2ODPwIJMp3hxYxUlAt5ZS6-Z4nXWMH6V"
    }
    response = requests.get(search_url, headers=headers)
    data = response.json()
    p = await m.reply(f"{em.proses} Bentar, sabar njing!")
    if len(m.command) < 1:
        return await m.reply(f"{em.gagal} Kasih tau judulnya apaan kek GOBLOK AMAT!")
    if data["response"]["hits"]:
        song_url = data["response"]["hits"][0]["result"]["url"]
        lyrics_response = requests.get(song_url)
        lyrics_text = lyrics_response.text
        await m.reply_text(lyrics_text)
        with open("lyrics.txt", "w", encoding="utf-8") as file:
            file.write(lyrics_text)
        await m.reply_document("lyrics.txt", caption=f"Lirik lagu {song_title}")
    else:
        await m.reply_text("Maaf, lirik lagu tidak ditemukan.")
        await p.delete()


"""
async def _(c, m):
    em = Emojik()
    em.initialize()
    if len(m.command) == 1:
        return await m.reply(f"{em.gagal} <b> Berikan judul lagu</b>")

    load = await m.reply(f"{em.proses} <b>Sedang proses...</>")
    song_name = m.text.split(None, 1)[1]

    lirik = api.search_song(song_name)

    if lirik is None:
        return await load.edit(
            f"{em.gagal} <b>Tidak dapat menemukan lyric untuk : </b> {song_name}"
        )

    lyric_title = lirik.title
    lyric_artist = lirik.artist
    lyrics_text = lirik.lyrics

    try:
        await load.edit_text(
            f"{em.sukses} --**{lyric_title}**--\n{lyric_artist}\n\n\n{lyrics_text}\nExtracted by {bot.me.username}"
        )

    except MessageTooLong:
        with open(f"downloads/{lyric_title}.txt", "w") as f:
            f.write(f"{lyric_title}\n{lyric_artist}\n\n\n{lyrics_text}")

        await load.edit_text(
            f"{em.gagal} <b>Lyric too long. Sending as a text file...</b>"
        )
        await m.reply_chat_action(action="upload_document")
        await m.reply_document(
            document=f"downloads/{lyric_title}.txt",
            thumb="https://telegra.ph//file/43cec0ae0ded594b55247.jpg",
            caption=f"\n{em.sukses} --{lyric_title}--\n{lyric_artist}\n\nExtracted by {bot.me.username}",
        )

        await load.delete()

        os.remove(f"downloads/{lyric_title}.txt")
"""
