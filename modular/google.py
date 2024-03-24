import urllib.parse

import requests
from pyrogram import *

from Mix import *

__modles__ = "Google"
__help__ = "Google"


async def google_search(query, limit=3):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://api.safone.dev/google?query={encoded_query}&limit=3"
    response = requests.get(url)
    data = response.json()
    if "results" in data:
        results = data["results"]
    else:
        return {"limit": 0, "results": []}

    return {
        "limit": limit,
        "results": [
            {
                "description": result["description"],
                "link": result["link"],
                "title": result["title"],
            }
            for result in results[:limit]
        ],
    }


@ky.ubot("google", sudo=True)
async def google_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    query = m.text.split(maxsplit=1)[1]
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://api.safone.dev/llama?query={encoded_query}"
    response = requests.get(url)
    data = response.json()

    if "answer" in data:
        results = data["answer"]
        await c.send_message(
            chat_id=m.chat.id,
            text=f"{em.sukses} **Pertanyaan :** `{query}`\n\n{em.profil} **Hasil :** `{results}`",
        )
        await pros.delete()
    else:
        await c.send_message(
            chat_id=m.chat.id,
            text=f"{em.gagal} Maaf, tidak dapat menemukan hasil untuk pencarian ini.",
        )
        await pros.delete()
