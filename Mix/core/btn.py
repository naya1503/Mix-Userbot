import re
from datetime import datetime, timedelta
from html import escape
from re import findall
from typing import List

from pykeyboard import InlineKeyboard
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton as Ikb
from pyrogram.types import InlineKeyboardMarkup, Message

from .parser import escape_markdown

# NOTE: the url \ escape may cause double escapes
# match * (bold) (don't escape if in url)
# match _ (italics) (don't escape if in url)
# match ` (code)
# match []() (markdown link)
# else, escape *, _, `, and [

# Gojo
# William


BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))")
NAN_REGEX = re.compile(r"(\[([^\[]+?)\] - (-(?:/{0,2})(.+?)&&?\)")


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
            Ikb(text=str(i[0]), callback_data=str(i[1]))
            if not is_url(i[1])
            else Ikb(text=str(i[0]), url=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)


def parse_button(text):
    markdown_note = text
    prev = 0
    note_data = ""
    buttons = []
    for match in BTN_URL_REGEX.finditer(markdown_note):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            # create a thruple with button label, url, and newline status
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)
        # if odd, escaped -> move along
        else:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
    else:
        note_data += markdown_note[prev:]

    return note_data, buttons


################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


def parse_mark(tk: str, kk):
    buttons = []
    if kk and kk.inline_keyboard:
        for i, row in enumerate(kk.inline_keyboard):
            for j, but in enumerate(row):
                button_str = f"{but.text} - {but.url}"
                if j > 0 and i > 0:
                    prev_button = kk.inline_keyboard[i][j - 1]
                    if prev_button.text != but.text:
                        button_str = f"{but.text} - {but.url} &&"
                elif j > 0:
                    button_str += f"&&"
                buttons.append(button_str)
    return f"{tk} {' '.join(buttons)}"


def nan_parse(text):
    markdown_note = text
    prev = 0
    note_data = ""
    buttons = []
    for match in NAN_REGEX.finditer(markdown_note):
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1
        if n_escapes % 2 == 0:
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)
        else:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
    else:
        note_data += markdown_note[prev:]

    return note_data, buttons


def nan_kibor(buttons):
    keyb = []
    for als in buttons:
        if "&&" in als[0]:
            row = [
                Ikb(label.strip(), url=url)
                for label, url in [button.split(" - ") for button in als[0].split("&&")]
            ]
            keyb.append(row)
        else:
            keyb.append([Ikb(als[0], url=als[1])])

    return keyb


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


def build_keyboard(buttons):
    keyb = []
    for als in buttons:
        if als[-1] and keyb:
            keyb[-1].append(Ikb(als[0], url=als[1]))
        else:
            keyb.append([Ikb(als[0], url=als[1])])

    return keyb


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


SMART_OPEN = "“"
SMART_CLOSE = "”"
START_CHAR = ("'", '"', SMART_OPEN)


async def escape_invalid_curly_brackets(text: str, valids: List[str]) -> str:
    new_text = ""
    idx = 0
    while idx < len(text):
        if text[idx] == "{":
            if idx + 1 < len(text) and text[idx + 1] == "{":
                idx += 2
                new_text += "{{{{"
                continue
            success = False
            for v in valids:
                if text[idx:].startswith("{" + v + "}"):
                    success = True
                    break
            if success:
                new_text += text[idx : idx + len(v) + 2]
                idx += len(v) + 2
                continue
            new_text += "{{"

        elif text[idx] == "}":
            if idx + 1 < len(text) and text[idx + 1] == "}":
                idx += 2
                new_text += "}}}}"
                continue
            new_text += "}}"

        else:
            new_text += text[idx]
        idx += 1

    return new_text


async def escape_mentions_using_curly_brackets(
    m: Message,
    text: str,
    parse_words: list,
) -> str:
    if m.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
        chat_name = escape(m.chat.title)
    else:
        chat_name = escape(m.from_user.first_name)
    teks = await escape_invalid_curly_brackets(text, parse_words)
    if teks:
        teks = teks.format(
            first=escape(m.from_user.first_name),
            last=escape(m.from_user.last_name or m.from_user.first_name),
            mention=m.from_user.mention,
            username=(
                "@" + (await escape_markdown(escape(m.from_user.username)))
                if m.from_user.username
                else m.from_user.mention
            ),
            fullname=" ".join(
                (
                    [
                        escape(m.from_user.first_name),
                        escape(m.from_user.last_name),
                    ]
                    if m.from_user.last_name
                    else [escape(m.from_user.first_name)]
                ),
            ),
            chatname=chat_name,
            id=m.from_user.id,
        )
    else:
        teks = ""

    return teks


async def split_quotes(text: str):
    """Split quotes in text."""
    if not any(text.startswith(char) for char in START_CHAR):
        return text.split(None, 1)
    counter = 1  # ignore first char -> is some kind of quote
    while counter < len(text):
        if text[counter] == "\\":
            counter += 1
        elif text[counter] == text[0] or (
            text[0] == SMART_OPEN and text[counter] == SMART_CLOSE
        ):
            break
        counter += 1
    else:
        return text.split(None, 1)

    # 1 to avoid starting quote, and counter is exclusive so avoids ending
    key = await remove_escapes(text[1:counter].strip())
    # index will be in range, or `else` would have been executed and returned
    rest = text[counter + 1 :].strip()
    if not key:
        key = text[0] + text[0]
    return list(filter(None, [key, rest]))


async def remove_escapes(text: str) -> str:
    """Remove the escaped from message."""
    res = ""
    is_escaped = False
    for counter in range(len(text)):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
    return res
