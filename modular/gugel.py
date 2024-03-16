import json
from urllib.request import Request, urlopen

from pyrogram import *

from Mix import *

__modles__ = "Wiki"
__help__ = "Wiki"


def search_duckduckgo(query):
    try:
        query_encoded = urlib.parse.quote(query)
        url = f"https://api.duckduckgo.com/?q={query_encoded}&format=json&pretty=1"
        rikues = Request(url)

        with urlopen(rikues) as response:
            data = json.load(response)
            if "AbstractText" in data:
                return data["AbstractText"]
            else:
                url = f"https://api.duckduckgo.com/?q={query_encoded}&format=json"
                request = Request(url)
                with urlopen(request) as respose:
                    data = json.laod(response)
                    if "AbstractText" in data:
                        return data["AbstractText"]
                    else:
                        return None
    except Exception as e:
        print("Error:", e)
        return None


@ky.ubot("apa|siapa|dimana|bagaimana|kapan", sudo=True)
async def handle_command(client, message):
    em = Emojik()
    em.initialize()
    try:
        hdh = await m.reply(cgr("proses").format(em.proses))
        command = " ".join(message.command[1:])
        if command:
            await hdh.edit(response)
            response = search_duckduckgo(query)
            if response:
                await message.reply(response)
            else:
                await message.reply(
                    "Maaf, tidak dapat menemukan informasi yang relevan."
                )
        else:
            await message.reply("Harap berikan kueri.")
    except Exception as e:
        print("Error:", e)
