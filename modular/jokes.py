import requests
from bs4 import BeautifulSoup
from Mix import *

__modles__ = "Joke"
__help__ = "Joke"

def get_joke():
    url = "https://api.safon.dev/joke"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    joke = soup.find('p').text.strip()
    return joke

@ky.ubot("joke", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    joke = get_joke()
    await pros.edit(f"{joke}")
