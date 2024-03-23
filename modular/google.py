import urllib.parse

import requests
from pyrogram import *

from Mix import *

__modles__ = "Google"
__help__ = "Google"


async def google_search(query, limit=3):
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.safone.dev/google?query={encoded_query}&limit={limit}"

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
    await m.reply(cgr("proses").format(em.proses))
    query = m.command[1]

    if query:
        results = await google_search(query)
        if results["results"]:
            for result in results["results"]:
                await c.send_message(
                    chat_id=m.chat.id,
                    text=f"{em.sukses} {result['title']}\n\n{result['link']}\n{result['description']}\n",
                )
        else:
            await c.send_message(
                chat_id=m.chat.id,
                text=f"{em.gagal} Maaf, tidak dapat menemukan hasil untuk pencarian ini.",
            )
    else:
        await c.send_message(
            chat_id=m.chat.id,
            text=f"{em.gagal} Silakan berikan query untuk pencarian Google.",
        )
