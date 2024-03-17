################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || William Butcher
 
 EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import asyncio

from pyrogram import *
from pyrogram.types import *
from SafoneAPI import SafoneAPI

from Mix import *
from Mix.core import http

__modles__ = "IpSearch"
__help__ = get_cgr("help_ips")


@ky.ubot("ipf|ipfake", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if len(m.command) == 1 and not rep:
        return await m.reply_text(f"{em.gagal} **Kasih kota nya Kontol!!**")
    if rep:
        ipf = rep.text
    else:
        ipf = m.command[1]
    msg = await m.reply_text(cgr("proses").format(em.proses))
    try:
        meki = SafoneAPI()
        fkip = await meki.fakeinfo(ipf)
        output = f"**Country Info:**\n\n"
        output += f"Name: {fkip['name']['title']} {fkip['name']['first']} {fkip['name']['last']}\n"
        output += f"Gender: {fkip['gender']}\n"
        output += f"Date of Birth: {fkip['dob']['date']}\n"
        output += f"Age: {fkip['dob']['age']}\n"
        output += f"Phone: {fkip['phone']}\n"
        output += f"Cell: {fkip['cell']}\n"
        output += f"Email: {fkip['email']}\n"
        output += (
            f"Location: {fkip['location']['city']}, {fkip['location']['country']}\n"
        )
        output += f"State: {fkip['location']['state']}\n"
        output += f"Postcode: {fkip['location']['postcode']}\n"
        output += f"Timezone: {fkip['location']['timezone']['description']} ({fkip['location']['timezone']['offset']})\n"
    except Exception as er:
        return await msg.edit(cgr("err").format(em.gagal, er))
    await msg.edit(output)
    return


@ky.ubot("ips|ipsearch|ip", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    if len(m.command) == 1 and not rep:
        return await m.reply_text(f"{em.gagal} **Kasih Ip nya Kontol!!**")
    if rep:
        ip_address = rep.text
    else:
        ip_address = m.command[1]
    msg = await m.reply_text(cgr("proses").format(em.proses))
    try:
        res = await http.get(f"https://ipinfo.io/{ip_address}/json", timeout=5)
    except asyncio.TimeoutError:
        return await msg.edit(f"{em.gagal} Timeout Error!!")
    except Exception as e:
        return await msg.edit(cgr("err").format(em.gagal, e))
    hostname = res.get("hostname", "N/A")
    city = res.get("city", "N/A")
    region = res.get("region", "N/A")
    country = res.get("country", "N/A")
    location = res.get("loc", "N/A")
    org = res.get("org", "N/A")
    await msg.edit(
        (
            f"**Details of `{ip_address}`**\n\n"
            f"HostName: `{hostname}`\n"
            f"City: `{city}`\n"
            f"Region: `{region}`\n"
            f"Country: `{country}`\n"
            f"Org: `{org}`\n"
            f"Map: https://www.google.fr/maps?q={location}\n"
        ),
        disable_web_page_preview=True,
    )
    return
