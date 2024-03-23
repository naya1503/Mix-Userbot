import aiohttp
from bs4 import BeautifulSoup
from Mix import *

__modles__ = "Joke"
__help__ = "Joke"

async def get_joke():
    async with aiohttp.ClientSession() as session:
        url = "https://api.safon.dev/joke"
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            joke = soup.find('p').text.strip()
            return joke

@ky.ubot("joke", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    joke = await get_joke()
    await pros.edit(f"{joke}")
