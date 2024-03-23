import requests

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def scrape_proxies(country="Singapore", limit=10):
    proxies = []
    try:
        url = f"https://api.safone.dev/proxy/socks5?country={country}&limit={limit}"
        response = requests.get(url)
        data = response.json()  # Assuming API returns JSON data
        for proxy_data in data:
            host = proxy_data.get("ip")
            port = proxy_data.get("port")
            country = proxy_data.get("country")
            proxies.append((host, port, country))
            print(f"Host: {host}, Port: {port}, Country: {country}")
    except Exception as e:
        print(f"Failed to scrape proxies: {e}")
    return proxies


@ky.ubot("proxy", sudo=True)
async def get_proxies_command(client, message):
    try:
        command_parts = message.text.split(" ")
        if len(command_parts) == 1:
            country = "Singapore"
            limit = 10
        elif len(command_parts) == 2:
            country = command_parts[1]
            limit = 10
        elif len(command_parts) == 3:
            country = command_parts[1]
            limit = int(command_parts[2])
        else:
            await message.reply_text(
                "Format perintah salah. Gunakan: /getproxy [country] [limit]"
            )
            return
    except ValueError:
        await message.reply_text("Limit harus berupa bilangan bulat.")
        return

    proxies = await scrape_proxies(country, limit)
    if proxies:
        response = f"**Daftar Proxy SOCKS5 dari {country} (Limit: {limit}):**\n"
        for i, (host, port, _) in enumerate(proxies, start=1):
            response += f"**{i}. Host: `{host}` | Port: `{port}`\n"
        await message.reply(response)
    else:
        await message.reply("Gagal mendapatkan daftar proxy. Silakan coba lagi nanti.")


"""
async def measure_latency(proxy_address):
    try:
        start_time = time.time()
        with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.set_proxy(socks.SOCKS5, proxy_address[0], int(proxy_address[1]))
            sock.settimeout(5)
            sock.connect(("www.google.com", 80))
        latency = time.time() - start_time
        return latency
    except Exception as e:
        print(f"Failed to measure latency for {proxy_address}: {e}")
        return float("inf")


def scrape_proxies(query):
    proxies = []
    try:
        url = "https://api.safone.dev/proxy/socks5?country={country}&limit={limit}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        proxy_rows = soup.find_all("tr")
        for row in proxy_rows[1:]:
            columns = row.find_all("td")
            if len(columns) >= 2:
                host = columns[0].text.strip()
                port = columns[1].text.strip()
                country = columns[3].text.strip()
                proxies.append((host, port, country))
                print(f"Host: {host}, Port: {port}, Country: {country}")
    except Exception as e:
        print(f"Failed to scrape proxies: {e}")
    return proxies


async def find_best_proxies(proxies):
    best_proxies = []

    for proxy in proxies:
        host, port, country = proxy
        latency = await measure_latency((host, port))
        best_proxies.append((host, port, latency, country))

    best_proxies.sort(key=lambda x: x[2])

    return best_proxies


@ky.ubot("proxy", sudo=True)
async def get_proxies(client, message):
    em = Emojik()
    em.initialize()
    pros = await message.reply(cgr("proses").format(em.proses))
    try:
        scraped_proxies = scrape_proxies()

        best_proxies = await find_best_proxies(scraped_proxies)

        if best_proxies:
            response = f"**{em.sukses} Top 2 best of list Proxy:**\n"
            for i, (proxy, port, latency, country) in enumerate(best_proxies, start=1):
                response += f"**{i}. Negara : `{country}` | `{proxy}:{port}` - Latensi: `{round(latency, 2)}` detik\n"

            await message.reply_text(response)
            await pros.delete()
        else:
            await message.reply(cgr("err").format(em.gagal))
            await pros.delete()
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        await pros.delete()
    await pros.delete()
"""
