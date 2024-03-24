import requests

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def fetch_proxies(proxy_type):
    url = f"https://www.proxy-list.download/api/v1/get?type={proxy_type}"
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.text.split("\r\n")
        proxies.sort()
        formatted_proxies = [
            f"**{i})** `{proxy}`" for i, proxy in enumerate(proxies, start=1)
        ]

        if not formatted_proxies[0]:
            formatted_proxies[0] = "1) No valid proxy found"

        return formatted_proxies[:10]
    else:
        return None


async def send_proxy(c: nlx, chat_id, proxies):
    if proxies:
        await c.send_message(chat_id, "\n".join(proxies))
    else:
        em = Emojik()
        em.initialize()
        await c.send_message(
            chat_id, f"{em.gagal} Tidak dapat menemukan proxy yang valid."
        )


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
        proxies = await fetch_proxies(proxy_type)
        await send_proxy(c, m.chat.id, proxies)
        await pros.delete()
    except IndexError:
        await c.send_message(m.chat.id, f"{em.gagal} Perintah tidak valid.")
        await pros.delete()
