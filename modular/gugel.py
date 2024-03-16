################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup

from Mix import *


__modles__ = "Wiki"
__help__ = "Wiki"



def scrape_wikipedia(query):
    try:
        url = f"https://en.wikipedia.org/wiki/{query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find('p').text.strip()
        return result
    except Exception as e:
        print("Error:", e)
        return None


@ky.ubot("dimanakah|apakah|siapakah|bagaimanakah", sudo=True)
async def handle_question(client, message):
    query = message.text.lower()
    response = ""

    if "dimanakah" in query or "apakah" in query or "siapakah" in query or "bagaimanakah" in query:
        query = query.replace("apakah", "").replace("siapakah", "").replace("bagaimanakah", "").replace("dimanakah", "").replace(" ", "_")
        result = scrape_wikipedia(query)
        if result:
            response = result
        else:
            response = "Maaf, tidak dapat menemukan informasi yang relevan."

    await message.reply(response)