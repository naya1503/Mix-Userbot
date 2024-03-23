import socket
import time
import requests
import socks
from bs4 import BeautifulSoup

from Mix import *

__modles__ = "Proxy"
__help__ = "Proxy"


async def measure_latency(proxy_address):
    try:
        start_time = time.time()
        with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.set_proxy(socks.SOCKS5, proxy_address[0], int(proxy_address[1]))  # Mengonversi port ke integer
            sock.settimeout(5)
            sock.connect(("www.google.com", 80))
        latency = time.time() - start_time
        return latency
    except Exception as e:
        print(f"Failed to measure latency for {proxy_address}: {e}")
        return float("inf")


def scrape_proxies():
    proxies = []
    try:
        url = "https://www.proxy-list.download/SOCKS5"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        proxy_rows = soup.find_all("tr")
        for row in proxy_rows[1:]:
            columns = row.find_all("td")
            if len(columns) >= 2:
                host = columns[0].text.strip()
                port = columns[1].text.strip()
                proxies.append((host, port))
    except Exception as e:
        print(f"Failed to scrape proxies: {e}")
    return proxies


async def find_best_proxies(proxies):
    best_proxies = []

    for proxy in proxies:
        latency = await measure_latency(proxy)
        best_proxies.append((proxy, latency))

    best_proxies.sort(key=lambda x: x[1])

    return best_proxies[:2]


@ky.ubot("proxy", sudo=True)
async def get_proxies(client, message):
    try:
        scraped_proxies = scrape_proxies()

        best_proxies = await find_best_proxies(scraped_proxies)

        if best_proxies:
            response = "**Top 2 best proxies:**\n"
            for i, (proxy, latency) in enumerate(best_proxies, start=1):
                response += f"**{i}. `{proxy[0]}:{proxy[1]}` - Latency: {round(latency, 2)} seconds\n"
            await message.reply_text(response)
        else:
            await message.reply_text("Failed to find suitable proxies.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

