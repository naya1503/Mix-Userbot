from pyrogram import *
import requests

from Mix import *

__modles__ = "Google"
__help__ = "Google"



async def google_search(query, limit=3):
    url = f"https://api.safone.dev/google?query={query}"
    response = await requests.get(url)
    data = response.json()
    return {
        "limit": limit,
        "results": [
            {
                "description": result["description"],
                "link": result["link"],
                "title": result["title"]
            }
            for result in data["results"][:limit]
        ]
    }

@ky.ubot("google", sudo=True)
async def google_command(c: nlx, m):
    query = " ".join(m.command[1:])
    
    if query:
        results = await google_search(query)
        if results['results']:
            for result in results['results']:
                await c.send_message(
                    chat_id=m.chat.id,
                    text=f"{result['title']}\n{result['link']}\n{result['description']}\n"
                )
        else:
            await c.send_message(
                chat_id=m.chat.id,
                text="Maaf, tidak dapat menemukan hasil untuk pencarian ini."
            )
    else:
        await c.send_message(
            chat_id=m.chat.id,
            text="Silakan berikan query untuk pencarian Google."
        )
