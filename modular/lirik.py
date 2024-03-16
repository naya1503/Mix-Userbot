import json
import urllib.parse
from urllib.request import Request, urlopen

from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Lyric"
__help__ = get_cgr("help_lirk")


async def search_lyrics(penyanyi, judul):
    try:
        penyanyi = urllib.parse.quote(penyanyi)
        judul = urllib.parse.quote(judul)

        url = f"https://api.lyrics.ovh/v1/{penyanyi}/{judul}"
        request = Request(url)

        with urlopen(request) as response:
            data = json.load(response)

            if "lyrics" in data:
                return data["lyrics"]
            else:
                url = f"https://api.lyrics.ovh/v1/{judul}/{penyanyi}"
                request = Request(url)
                with urlopen(request) as response:
                    data = json.load(response)
                    if "lyrics" in data:
                        return data["lyrics"]
                    else:
                        return None
    except Exception as e:
        return None


@ky.ubot("lyrics", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    try:
        pft = await m.reply(cgr("proses").format(em.proses))
        command = " ".join(m.command[1:])
        parts = command.split("-")
        if len(parts) != 2:
            await pft.edit(
                cgr("lirk_1").format(
                    em.gagal, em.sukses, m.command, em.sukses, m.command
                )
            )
            return

        penyanyi = parts[0].strip().capitalize()
        judul = parts[1].strip().capitalize()
        lyrics_text = await search_lyrics(penyanyi, judul)
        if not lyrics_text:
            penyanyi = parts[0].strip().lower()
            judul = parts[1].strip().lower()
            lyrics_text = await search_lyrics(penyanyi, judul)

        if lyrics_text:
            await pft.edit(f"{em.sukses} <code>{lyrics_text}</code>")
        else:
            await pft.edit(cgr("lirk_2").format(em.gagal))
    except Exception as e:
        await pft.edit(cgr("err").format(em.gagal, e))
