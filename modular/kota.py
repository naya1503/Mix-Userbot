# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import flag
from countryinfo import CountryInfo

from Mix import *

__modles__ = "Kota"
__help__ = """
 Kota
• Perintah: `{p}kota` [query]
• Penjelasan: Untuk mencari info tentang kota tersebut.
"""


@ky.ubot("kota", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    msg_ = await m.reply(cgr("proses").format(em.proses))
    lol = c.get_text(m)
    if not lol:
        await msg_.edit(f"{em.gagal}` **Kasih kota nya Goblok!!**")
        return
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await msg_.edit(
            f"{em.gagal}` **Lu sekolah kaga si nyet? Kota model begini `{lol}` kaga ada Tolol!! **"
        )
        return
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = "".join(p + ",  " for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(fk + ",  " for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(what + "  " for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(FKer + ",  " for FKer in fker)
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += po + ",  "
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)
    languages = a.get("languages")
    lMAO = "".join(lmao + ",  " for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(jerry + ",   " for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(targaryen + ",   " for targaryen in GOT)
    wiki = a.get("wiki")
    caption = f"""<b><u>Informasi</b></u>
**Nama negara:- `{name}`
Ejaan Alternatif:- `{hu}`
Wilayah Negara:- `{area}` kilometer persegi
Perbatasan:- `{borders}`
Kode Panggilan:- `{call}`
Ibukota Negara:- `{capital}`
Mata uang negara:- `{currencies}`
Bendera Negara:- `{okie}`
Demonim:- `{HmM}`
Jenis Negara:- `{EsCoBaR}`
Nama ISO:- `{iso}`
Bahasa:- `{lMAO}`
Nama Asli:- `{nonive}`
Populasi:- `{waste}`
Wilayah:- `{reg}`
Sub Wilayah:- `{sub}`
Zona waktu:- `{tom}`
Top Level Domain:- `{lanester}`
Wikipedia:- `{wiki}`**
"""
    await msg_.edit(caption, disable_web_page_preview=True)
