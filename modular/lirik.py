from lyricsgenius import Genius
from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Lyric"
__help__ = "Lyrics"


api = Genius(
    "mJIaLonIWBIhEVZrclZIGtBdrIdSKpxa2ODPwIJMp3hxYxUlAt5ZS6-Z4nXWMH6V", verbose=False
)


import json
import urllib.parse
from urllib.request import Request, urlopen


# Fungsi untuk menangani perintah /lirik
@ky.ubot("lirik", sudo=True)
async def _(c, m):
    try:
        # Mendapatkan nama penyanyi dan judul lagu dari pesan
        command = " ".join(m.command[1:])
        # Memisahkan nama penyanyi dan judul lagu dengan tanda "-"
        parts = command.split("-")

        # Memastikan bahwa terdapat tepat satu tanda "-" untuk memisahkan
        if len(parts) != 2:
            await m.reply_text(
                "Format perintah salah. Gunakan format: /lirik nama-penyanyi - judul-lagu"
            )
            return

        # Menghapus spasi tambahan jika ada
        penyanyi = parts[0].strip()
        judul = parts[1].strip()

        # Jika posisi terbalik, tukar nama penyanyi dan judul lagu
        if judul.lower() < penyanyi.lower():
            penyanyi, judul = judul, penyanyi

        # Mengganti spasi dengan karakter pengganti "%20" dalam URL
        penyanyi = urllib.parse.quote(penyanyi)
        judul = urllib.parse.quote(judul)

        url = f"https://api.lyrics.ovh/v1/{penyanyi}/{judul}"
        request = Request(url)

        with urlopen(request) as response:
            data = json.load(response)

            if "lyrics" in data:
                lyrics_text = data["lyrics"]
                await m.reply_text(lyrics_text)
            else:
                await m.reply_text("Maaf, lirik lagu tidak ditemukan.")
    except Exception as e:
        await m.reply(f"error : `{e}`")


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
