import requests
from gpytranslate import Translator

from Mix import *

__modles__ = "Joke"
__help__ = """
 Joke

• Perintah: `{0}joke`
• Penjelasan: Untuk generate random joke.
"""


async def kitatr(txt):
    cokk = Translator()
    gasin = await cokk.translate(txt, "en", "id")
    sukses = []
    for gs in gasin["raw"]["sentences"]:
        sukses.append(gs["trans"])
    return sukses[0]


async def get_joke():
    url = "https://api.safone.dev/joke"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()["joke"]
    else:
        print(f"Error: {res.status_code} - {res.text}")
        return None


@ky.ubot("joke", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    joke = await get_joke()
    trbang = await kitatr(joke)
    await pros.edit(f"{trbang}")
