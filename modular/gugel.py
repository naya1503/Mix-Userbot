import requests
from gpytranslate import Translator

from Mix import *

trans = Translator()


async def translate_text(text, target_language):
    translation = await trans.translate(text, targetlang=target_language)
    return translation.text


async def get_duckduckgo_answer(query, bahasa):
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json"}
        response = requests.get(url, params=params)
        data = response.json()
        if data["AbstractText"]:
            answer = data["AbstractText"]
            if not answer.isascii():
                answer = await translate_text(answer, "id")
            return answer
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


@ky.ubot("siapa|apa|dimana|bagaimana|kenapa|kapan", sudo=True)
async def handle_command(client, message):
    em = Emojik()
    em.initialize()
    try:
        proses = await message.reply(cgr("proses").format(em.proses))
        command = message.text.split()[0][1:]
        query = " ".join(message.command[1:])
        if query:
            bahasa = "id"
            command_map = {
                "siapa": f"siapa {query}?",
                "apa": f"apa {query}?",
                "dimana": f"dimana {query}",
                "bagaimana": f"bagaimana {query}",
                "kenapa": f"kenapa {query}?",
                "kapan": f"kapan {query}?",
            }
            if command in command_map:
                query = command_map[command]
            response = await get_duckduckgo_answer(query, bahasa)
            if response:
                await message.reply(f"{em.sukses} {response}")
            else:
                await message.reply(
                    f"{em.gagal} Maaf, tidak dapat menemukan informasi yang relevan."
                )
        else:
            await message.reply(f"{em.gagal} Harap berikan kueri!")
        await proses.delete()
    except Exception as e:
        print("Error:", e)
        await proses.delete()


"""
import requests
from gpytranslate import Translator
from pyrogram import *

from Mix import *

__modles__ = "Wiki"
__help__ = "Wiki"

trans = Translator()


async def translate_text(text, target_language):
    translation = await trans.translate(text, targetlang=target_language)
    return translation.text


async def search_wikipedia(query, bahasa):
    try:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "titles": query,
        }

        response = requests.get(url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        article_content = page.get("extract")

        if article_content:
            translated_content = await translate_text(article_content, bahasa)
            return translated_content
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None


@ky.ubot("apa|siapa|dimana|bagaimana|kapan|kenapa", sudo=True)
async def handle_command(client, message):
    em = Emojik()
    em.initialize()
    try:
        proses = await message.reply(cgr("proses").format(em.proses))
        query = " ".join(message.command[1:])
        if query:
            bahasa = "id"
            response = await search_wikipedia(query, bahasa)
            if response:
                await message.reply(
                    f"{em.sukses} <b>Berikut hasil dari <code>{query}</code> :</b> \n\n<code>{response}</code>"
                )
            else:
                await message.reply(
                    f"{em.gagal} <b>Maaf, tidak dapat menemukan informasi yang relevan.</b>"
                )
        else:
            await message.reply(f"{em.gagal} <b>Harap berikan kueri!</b>")
        await proses.delete()
    except Exception as e:
        print("Error:", e)
        await proses.delete()


async def search_duckduckgo(query, bahasa):
    try:
        query_encoded = quote(query)
        url = f"https://api.duckduckgo.com/?q={query_encoded}&format=json&pretty=1"
        request = Request(url)

        with urlopen(request) as response:
            data = json.load(response)
            if "AbstractText" in data:
                translated_text = await translate_text(data["AbstractText"], bahasa)
                return translated_text
            else:
                url = f"https://api.duckduckgo.com/?q={query_encoded}&format=json"
                request = Request(url)
                with urlopen(request) as response:
                    data = json.load(response)
                    if "AbstractText" in data:
                        translated_text = await translate_text(
                            data["AbstractText"], bahasa
                        )
                        return translated_text
                    else:
                        return None
    except Exception as e:
        print("Error:", e)
        return None
        """
