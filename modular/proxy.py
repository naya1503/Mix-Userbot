import asyncio
import random

from aiohttp import ClientSession

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def fetch_proxies(command):
    url = f"https://www.proxy-list.download/api/v1/get?type={command}&country=SG"
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            proxies = data.split("\r\n")
            return proxies


async def test_proxy(session, proxy):
    try:
        async with session.get(
            "https://api.ipify.org?format=json", proxy=f"http://{proxy}"
        ) as response:
            if response.status == 200:
                return True
    except Exception:
        pass
    return False


async def get_best_proxy(proxy_type):
    proxies = await fetch_proxies(proxy_type)
    if proxies:
        return random.choice(proxies)
    else:
        return None


async def send_proxy(c: nlx, chat_id, proxy):
    if proxy:
        await c.send_message(chat_id, proxy)
    else:
        await c.send_message(chat_id, "Tidak dapat menemukan proxy yang valid.")


@ky.ubot("getproxy", sudo=True)
async def get_proxy_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    try:
        command = m.text.split()[1].lower()
        if command not in ["http", "socks4", "socks5"]:
            await c.send_message(m.chat.id, "Perintah tidak valid.")
            return

        proxy_type = command.upper()
        best_proxy = await get_best_proxy(proxy_type)
        await send_proxy(c, m.chat.id, best_proxy)
    except IndexError:
        await c.send_message(m.chat.id, "Perintah tidak valid.")
