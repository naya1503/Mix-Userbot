from html import escape
from re import compile as compilere
from re import sub


async def cleanhtml(raw_html: str) -> str:
    """Clean html data."""
    cleanr = compilere("<.*?>")
    return sub(cleanr, "", raw_html)


async def escape_markdown(text: str) -> str:
    """Escape markdown data."""
    escape_chars = r"\*_`\["
    return sub(r"([%s])" % escape_chars, r"\\\1", text)


async def mention_html(name: str, user_id: int) -> str:
    """Mention user in html format."""
    name = escape(name)
    return f'<a href="tg://user?id={user_id}">{name}</a>'


async def mention_markdown(name: str, user_id: int) -> str:
    """Mention user in markdown format."""
    return f"[{(await escape_markdown(name))}](tg://user?id={user_id})"


async def clean_html(text: str) -> str:
    return (
        text.replace("<code>", "")
        .replace("</code>", "")
        .replace("<b>", "")
        .replace("</b>", "")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("<u>", "")
        .replace("</u>", "")
    )


async def clean_markdown(text: str) -> str:
    return text.replace("`", "").replace("**", "").replace("__", "")


async def remove_markdown_and_html(text: str) -> str:
    return await clean_markdown(await clean_html(text))


kode_bahasa = {
    "Afrikaans": "af",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "Czech": "cs",
    "German": "de",
    "Greek": "el",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Indonesian": "id",
    "Icelandic": "is",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Korean": "ko",
    "Latin": "la",
    "Myanmar": "my",
    "Nepali": "ne",
    "Dutch": "nl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Sundanese": "su",
    "Swedish": "sv",
    "Thailand": "th",
    "Filipino": "tl",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Catalan": "ca",
    "Danish": "da",
    "Finnish": "fi",
    "Hungarian": "hu",
    "Polish": "pl",
    "Ukrainian": "uk",
    "Taiwan": "zh-tw",
}
