import asyncio
import random
from aiohttp import ClientSession

from Mix import *


__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def fetch_proxies():
    url = 'https://www.proxy-list.download/api/v1/get?type=http'
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            proxies = data.split('\r\n')
            return proxies


async def test_proxy(session, proxy):
    try:
        async with session.get("https://api.ipify.org?format=json", proxy=f"http://{proxy}") as response:
            if response.status == 200:
                return True
    except Exception:
        pass
    return False


async def get_best_proxy(proxy_type):
    proxies = await fetch_proxies()
    async with ClientSession() as session:
        tasks = [test_proxy(session, proxy) for proxy in proxies]
        results = await asyncio.gather(*tasks)
        valid_proxies = [proxy for proxy, result in zip(proxies, results) if result]
        if valid_proxies:
            return random.choice(valid_proxies)
    return None


async def send_proxy(client, chat_id, proxy):
    if proxy:
        await client.send_message(chat_id, proxy)
    else:
        await client.send_message(chat_id, "Tidak dapat menemukan proxy yang valid.")


@ky.ubot("getproxy", sudo=True)
async def get_proxy_command(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    try:
        command = m.text.split()[1].lower()
        if command not in ["http", "socks4", "socks5"]:
            await c.send_message(m.chat.id, "Perintah tidak valid.")
            return
        await pros.delete()

        proxy_type = command.upper()
        best_proxy = await get_best_proxy(proxy_type)
        await send_proxy(c, m.chat.id, best_proxy)
    except IndexError:
        await c.send_message(m.chat.id, "Perintah tidak valid.")
        await pros.delete()