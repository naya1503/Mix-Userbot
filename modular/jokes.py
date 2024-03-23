import requests

from Mix import *

__modles__ = "Joke"
__help__ = "Joke"


def get_joke():
    url = "https://api.safon.dev/joke"
    response = requests.get(url)
    data = response.json()
    joke = data.get("joke")
    return joke


@ky.ubot("joke", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    joke = await c.get_joke(joke)
    await pros.edit(f"{joke}")
