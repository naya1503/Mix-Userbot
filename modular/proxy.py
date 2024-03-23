import random

import requests

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def fetch_proxies(proxy_type):
    url = f"https://www.proxy-list.download/api/v1/get?type={proxy_type}"
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.text.split("\r\n")
        return proxies
    else:
        return None


# async def get_best_proxy(proxy_type):
#     proxies = fetch_proxies(proxy_type)
#     if proxies:
#         return random.choice(proxies)
#     else:
#         return None


async def send_proxy(c: nlx, chat_id, proxy):
    if proxy:
        await c.send_message(chat_id, proxy)
    else:
        await c.send_message(chat_id, f"{em.gagal} Tidak dapat menemukan proxy yang valid.")


@ky.ubot("getproxy", sudo=True)
async def get_proxy_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    try:
        pros = await m.reply(cgr("proses").format(em.proses))
        command = m.text.split()[1].lower()
        if command not in ["http", "socks4", "socks5"]:
            await c.send_message(m.chat.id, f"{em.gagal} Perintah tidak valid.")
            return

        proxy_type = command
        best_proxy = await fetch_proxies(proxy_type)
        await send_proxy(c, m.chat.id, best_proxy)
        await pros.delete()
    except IndexError:
        await c.send_message(m.chat.id, f"{em.gagal} Perintah tidak valid.")
        await pros.delete()