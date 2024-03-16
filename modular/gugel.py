import requests
from urllib.parse import quote
from pyrogram import *

from Mix import *

__modles__ = "Wiki"
__help__ = "Wiki"

def search_duckduckgo(query):
    try:
        query_encoded = quote(query).replace(" ", "%20")
        url = f"https://api.duckduckgo.com/?q={query_encoded}&format=json&pretty=1"
        response = requests.get(url)
        data = response.json()
        search_text = data.get('AbstractText', None)
        if not search_text and 'RelatedTopics' in data and data['RelatedTopics']:
            search_text = data['RelatedTopics'][0].get('Text', None)
        
        return search_text
    except Exception as e:
        print("Error:", e)
        return None

@ky.ubot("apa|siapa|dimana|bagaimana|kapan", sudo=True)
async def handle_command(client, message):
    try:
        query = message.text.split(maxsplit=1)[1].strip()
        if query:
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
