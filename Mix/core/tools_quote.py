################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################

from .http import *


class QuotlyException(Exception):
    pass


loanjing = [
    "White",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "Black",
]


async def get_sender(m):
    if m.forward_date:
        if m.forward_sender_name:
            return 1
        elif m.forward_from:
            return m.forward_from.id
        elif m.forward_from_chat:
            return m.forward_from_chat.id
        else:
            return 1
    elif m.from_user:
        return m.from_user.id
    elif m.sender_chat:
        return m.sender_chat.id
    else:
        return 1


async def sender_name(m):
    if m.forward_date:
        if m.forward_sender_name:
            return m.forward_sender_name
        elif m.forward_from:
            return (
                f"{m.forward_from.first_name} {m.forward_from.last_name or ''}"
                if m.forward_from.last_name
                else m.forward_from.first_name
            )

        elif m.forward_from_chat:
            return m.forward_from_chat.title
        else:
            return ""
    elif m.from_user:
        if m.from_user.last_name:
            return f"{m.from_user.first_name} {m.from_user.last_name or ''}"
        else:
            return m.from_user.first_name
    elif m.sender_chat:
        return m.sender_chat.title
    else:
        return ""


async def sender_emoji(m):
    if m.forward_date:
        return (
            ""
            if m.forward_sender_name
            or not m.forward_from
            and m.forward_from_chat
            or not m.forward_from
            else m.forward_from.emoji_status.custom_emoji_id
        )

    return m.from_user.emoji_status.custom_emoji_id if m.from_user else ""


async def sender_username(m):
    if m.forward_date:
        if (
            not m.forward_sender_name
            and not m.forward_from
            and m.forward_from_chat
            and m.forward_from_chat.username
        ):
            return m.forward_from_chat.username
        elif (
            not m.forward_sender_name
            and not m.forward_from
            and m.forward_from_chat
            or m.forward_sender_name
            or not m.forward_from
        ):
            return ""
        else:
            return m.forward_from.username or ""
    elif m.from_user and m.from_user.username:
        return m.from_user.username
    elif (
        m.from_user or m.sender_chat and not m.sender_chat.username or not m.sender_chat
    ):
        return ""
    else:
        return m.sender_chat.username


async def sender_photo(m):
    if m.forward_date:
        if (
            not m.forward_sender_name
            and not m.forward_from
            and m.forward_from_chat
            and m.forward_from_chat.photo
        ):
            return {
                "small_file_id": m.forward_from_chat.photo.small_file_id,
                "small_photo_unique_id": m.forward_from_chat.photo.small_photo_unique_id,
                "big_file_id": m.forward_from_chat.photo.big_file_id,
                "big_photo_unique_id": m.forward_from_chat.photo.big_photo_unique_id,
            }
        elif (
            not m.forward_sender_name
            and not m.forward_from
            and m.forward_from_chat
            or m.forward_sender_name
            or not m.forward_from
        ):
            return ""
        else:
            return (
                {
                    "small_file_id": m.forward_from.photo.small_file_id,
                    "small_photo_unique_id": m.forward_from.photo.small_photo_unique_id,
                    "big_file_id": m.forward_from.photo.big_file_id,
                    "big_photo_unique_id": m.forward_from.photo.big_photo_unique_id,
                }
                if m.forward_from.photo
                else ""
            )

    elif m.from_user and m.from_user.photo:
        return {
            "small_file_id": m.from_user.photo.small_file_id,
            "small_photo_unique_id": m.from_user.photo.small_photo_unique_id,
            "big_file_id": m.from_user.photo.big_file_id,
            "big_photo_unique_id": m.from_user.photo.big_photo_unique_id,
        }
    elif m.from_user or m.sender_chat and not m.sender_chat.photo or not m.sender_chat:
        return ""
    else:
        return {
            "small_file_id": m.sender_chat.photo.small_file_id,
            "small_photo_unique_id": m.sender_chat.photo.small_photo_unique_id,
            "big_file_id": m.sender_chat.photo.big_file_id,
            "big_photo_unique_id": m.sender_chat.photo.big_photo_unique_id,
        }


async def t_or_c(m):
    if m.text:
        return m.text
    elif m.caption:
        return m.caption
    else:
        return ""


async def quotly(messages, kolor):
    if not isinstance(messages, list):
        messages = [messages]
    # payload = {
    #    "type": "quote",
    #    "format": "png",
    #    "backgroundColor": kolor,
    #    "messages": [],
    # }
    payload = {
        "type": "quote",
        "format": "webp",
        "backgroundColor": kolor,
        "messages": [],
    }

    for m in messages:
        m_dict = {}
        if m.entities:
            m_dict["entities"] = [
                {
                    "type": entity.type.name.lower(),
                    "offset": entity.offset,
                    "length": entity.length,
                }
                for entity in m.entities
            ]
        elif m.caption_entities:
            m_dict["entities"] = [
                {
                    "type": entity.type.name.lower(),
                    "offset": entity.offset,
                    "length": entity.length,
                }
                for entity in m.caption_entities
            ]
        else:
            m_dict["entities"] = []
        m_dict["chatId"] = await get_sender(m)
        m_dict["text"] = await t_or_c(m)
        m_dict["avatar"] = True
        m_dict["from"] = {}
        m_dict["from"]["id"] = await get_sender(m)
        m_dict["from"]["name"] = await sender_name(m)
        m_dict["from"]["username"] = await sender_username(m)
        m_dict["from"]["type"] = m.chat.type.name.lower()
        m_dict["from"]["photo"] = await sender_photo(m)
        if m.reply_to_message:
            m_dict["replyMessage"] = {
                "name": await sender_name(m.reply_to_message),
                "text": await t_or_c(m.reply_to_message),
                "chatId": await get_sender(m.reply_to_message),
            }
        else:
            m_dict["replyMessage"] = {}
        payload["messages"].append(m_dict)
    # r = await http.post("https://bot.lyo.su/quote/generate.png", json=payload)
    r = await http.post("https://api.safone.dev/quotly", json=payload)

    if not r.is_error:
        return r.read()
    else:
        raise QuotlyException(r.json())


def isArgInt(txt) -> list:
    count = txt
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]
