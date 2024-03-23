import asyncio

from aiohttp import ClientSession
from proxybroker import Broker

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def get_best_proxy(proxy_type):
    proxies = []

    broker = Broker()
    await broker.start()

    try:
        proxies = await broker.find(types=[proxy_type], limit=10)

        async with ClientSession() as session:
            tasks = []
            for proxy in proxies:
                task = asyncio.create_task(check_proxy(session, proxy))
                tasks.append(task)
            await asyncio.gather(*tasks)

        best_proxy = max(proxies, key=lambda x: x.score)
        return best_proxy
    finally:
        await broker.stop()


async def check_proxy(session, proxy):
    try:
        async with session.get(
            "https://api.ipify.org?format=json", proxy=f"{proxy.host}:{proxy.port}"
        ) as response:
            if response.status == 200:
                proxy.score = proxy.score + 1
    except Exception:
        pass


async def send_proxy(client, chat_id, proxy):
    await client.send_message(chat_id, f"{proxy.host}:{proxy.port}")


@ky.ubot("getproxy", sudo=True)
async def get_proxy_command(client, message):
    try:
        command = message.text.split()[1].lower()
        if command not in ["http", "socks4", "socks5"]:
            await client.send_message(message.chat.id, "Perintah tidak valid.")
            return

        proxy_type = command.upper()
        best_proxy = await get_best_proxy(proxy_type)
        await send_proxy(client, message.chat.id, best_proxy)
    except IndexError:
        await client.send_message(message.chat.id, "Perintah tidak valid.")
