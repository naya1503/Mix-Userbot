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
        sukses.append(gas["trans"])
    return sukses


async def get_joke():
    url = "https://api.safone.dev/joke"
    res = requests.get(url)
    if res.status_code == 200:
        mak = res.json()["joke"]
        trbang = await kitatr(mak)
        return trbang
    else:
        print(f"Error: {res.status_code} - {res.text}")
        return None


@ky.ubot("joke", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    joke = await get_joke()
    await pros.edit(f"{joke}")
