import glob
import os
import random

from PIL import Image, ImageDraw, ImageFont
from pyrogram import *
from pyrogram.types import *

from Mix import Emojik, cgr, get_cgr, ky, nlx
from Mix.core.tools_media import dl_font

__modles__ = "Logo"
__help__ = get_cgr("help_logo")


@ky.ubot("logo", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    await dl_font()
    name = c.get_arg(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if not name:
        await xx.edit(cgr("logo_1").format(em.gagal, m.command))
        return
    bg_, font_ = "", ""
    if m.reply_to_message:
        temp = m.reply_to_message
        if temp.media:
            if temp.document:
                if "font" in temp.document.mime_type:
                    font_ = await temp.download()
                elif (".ttf" in temp.document.file_name) or (
                    ".otf" in temp.document.file_name
                ):
                    font_ = await temp.download()
            elif temp.photo:
                bg_ = await temp.download()
    else:
        pics = []
        async for i in c.search_messages(
            "AllLogoHyper", filter=enums.MessagesFilter.PHOTO
        ):
            if i.photo:
                pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download()
        fpath_ = glob.glob("font-module/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in c.search_messages(
            "AllLogoHyper", filter=enums.MessagesFilter.PHOTO
        ):
            if i.photo:
                pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download()
    if not font_:
        fpath_ = glob.glob("font-module/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 170
        strke = 15
    elif len(name) >= 9:
        fnt_size = 100
        strke = 10
    else:
        fnt_size = 200
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), name, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    flnme = f"logo.png"
    img.save(flnme, "png")
    await xx.edit(cgr("upload").format(em.proses))
    if os.path.exists(flnme):
        await c.send_photo(
            chat_id=m.chat.id,
            photo=flnme,
            caption=cgr("logo_2").format(em.sukses, c.me.mention),
        )

        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("font-module"):
            os.remove(font_)
