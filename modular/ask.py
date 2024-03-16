import requests
from bs4 import BeautifulSoup
from pyrogram import *
import re
from googletrans import Translator

from Mix import *

__modles__ = "ask"
__help__ = "ask"

async def get_duckduckgo_answer(query):
    url = f"https://duckduckgo.com/html/?q={'+'.join(query.split())}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = await requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    answer = soup.find("a", class_="result__snippet")
    if answer:
        return answer.text
    else:
        return "Maaf, tidak dapat menemukan jawaban untuk pertanyaan tersebut."

async def translate_text(text, target_language='id'):
    translator = Translator()
    translated_text = await translator.translate(text, dest=target_language)
    return translated_text.text

@ky.ubot("ask", sudo=True)
async def _(c, m):
    message_text = m.text.lower()
    question_pattern = r"^/ask (.+)$"
    match = re.match(question_pattern, message_text)
    if match:
        query = match.group(1)
        answer = await get_duckduckgo_answer(query)
        translated_answer = await translate_text(answer)
        response = f"Pertanyaan: {query}\n\nJawaban:\n{translated_answer}"
        await m.reply_text(response)
    else:
        await m.reply_text("Format perintah salah. Gunakan /ask pertanyaan untuk mencari jawaban.")