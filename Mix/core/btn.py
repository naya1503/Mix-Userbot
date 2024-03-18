################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru || William Butcher
 
 EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT LO BAJINGAN!!
"""
################################################################


import re
from datetime import datetime, timedelta
from re import findall

from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton as Ikb
from pyrogram.types import InlineKeyboardMarkup

# NOTE: the url \ escape may cause double escapes
# match * (bold) (don't escape if in url)
# match _ (italics) (don't escape if in url)
# match ` (code)
# match []() (markdown link)
# else, escape *, _, `, and [

# Gojo
# William


BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))")


def is_url(text: str) -> bool:
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
    return [x[0] for x in findall(regex, str(text))]


def keyboard(buttons_list, row_width: int = 2):
    buttons = InlineKeyboard(row_width=row_width)
    data = [
        (
            Ikb(text=str(i[0]), url=str(i[1]))
            if is_url(i[1])
            else Ikb(text=str(i[0]), callback_data=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)


"""
def text_keyb(ikb, text: str, row_width: int = 2):
    keyboard = {}
    try:
        text = text.strip()
        if text.startswith("`"):
            text = text[1:]
        if text.endswith("`"):
            text = text[:-1]

        text, keyb = text.split("-")

        keyb = findall(r"\[([^|]+)\|([^]]+)\]", keyb)
        for btn_str in keyb:

            btn_str = btn_str.strip("[]")
            btn_txt, btn_data = btn_str.split("|")
            btn_txt = btn_txt.strip()
            btn_data = btn_data.strip()

            if not is_url(btn_data):
                continue
            keyboard[btn_txt] = btn_data
        keyboard = ikb(keyboard, row_width)
    except Exception as e:
        print(f"Error in text_keyb: {e}")
        return None, None
    return text, keyboard
"""


def text_keyb(ikb, text: str, row_width: int = 2):
    keyboard = {}
    try:
        text_parts = text.split("~")
        if len(text_parts) != 2:
            return None, None

        main_text = text_parts[0].strip()
        button_text = text_parts[1].strip()
        main_text = main_text.replace("<b>", "**").replace("</b>", "**")
        main_text = main_text.replace("<i>", "__").replace("</i>", "__")
        main_text = main_text.replace("<strike>", "~~").replace("</strike>", "~~")
        main_text = main_text.replace("<spoiler>", "||").replace("</spoiler>", "||")
        main_text = main_text.replace("<u>", "--").replace("</u>", "--")

        keyb_texts = findall(r"\[([^]]+)\]", button_text)
        for keyb_text in keyb_texts:
            keyb_parts = keyb_text.split("|")
            if len(keyb_parts) == 2:
                btn_txt, btn_data = keyb_parts[0].strip(), keyb_parts[1].strip()
                if not is_url(btn_data):
                    btn_data = f"{btn_data}"
                keyboard[btn_txt] = btn_data

        keyboard = ikb(keyboard, row_width)
    except Exception as e:
        print(f"Error in text_keyb: {e}")
        return None, None
    return main_text, keyboard


def extract_time(time_val):
    if any(time_val.endswith(unit) for unit in ("s", "m", "h", "d")):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            return None

        if unit == "s":
            bantime = datetime.now() + timedelta(seconds=int(time_num))
        elif unit == "m":
            bantime = datetime.now() + timedelta(minutes=int(time_num))
        elif unit == "h":
            bantime = datetime.now() + timedelta(hours=int(time_num))
        elif unit == "d":
            bantime = datetime.now() + timedelta(days=int(time_num))
        else:
            # how even...?
            return None
        return bantime
    else:
        return None


def format_welcome_caption(html_string, chat_member):
    return html_string.format(
        dc_id=chat_member.dc_id,
        first_name=chat_member.first_name,
        id=chat_member.id,
        last_name=chat_member.last_name,
        mention=chat_member.mention,
        username=chat_member.username,
    )


def okb(rows=None, back=False, todo="closeru"):
    """
    rows = pass the rows
    back - if want to make back button
    todo - callback data of back button
    """
    if rows is None:
        rows = []
    lines = []
    try:
        for row in rows:
            line = []
            for button in row:
                btn_text = button.split(".")[1].capitalize()
                button = btn(btn_text, button)  # InlineKeyboardButton
                line.append(button)
            lines.append(line)
    except AttributeError:
        for row in rows:
            line = []
            for button in row:
                button = btn(*button)  # Will make the kb which don't have "." in them
                line.append(button)
            lines.append(line)
    except TypeError:
        # make a code to handel that error
        line = []
        for button in rows:
            button = btn(*button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    if back:
        back_btn = [(btn("Back", todo))]
        lines.append(back_btn)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})
