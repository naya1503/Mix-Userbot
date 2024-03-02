################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MissKaty
"""
################################################################

import inspect
import json
import os.path
from functools import partial, wraps
from glob import glob
from typing import Dict, List

from team.nandev.database import udB

from Mix import user

list_bhs: List[str] = [
    "id-ID",  # Indonesian
]

def_bhs: str = "id-ID"


def load_bhs(files: List[str]) -> Dict[str, Dict[str, Dict[str, str]]]:
    ldict = {lang: {} for lang in list_bhs}
    for file in files:
        _, lname, pname = file.split(os.path.sep)
        pname = pname.split(".")[0]
        dic = json.load(open(file, encoding="utf-8"))
        dic.update(ldict[lname].get(pname, {}))
        ldict[lname][pname] = dic
    return ldict


jsons: List[str] = []

for locale in list_bhs:
    jsons += glob(os.path.join("langs", locale, "*.json"))

langdict = load_bhs(jsons)


def get_bhs_str(
    dic: dict, language: str, default_context: str, key: str, context: str = None
) -> str:
    if context:
        default_context = context
        dic = langdict[language].get(context, langdict[def_bhs][context])
    res: str = dic.get(key) or langdict[def_bhs][default_context].get(key) or key
    return res


async def get_bhsnya():
    lang = def_bhs or udB.get_bahasa(user.me.id)

    # User has a language_code without hyphen
    if len(lang.split("-")) == 1:
        # Try to find a language that starts with the provided language_code
        for locale_ in list_bhs:
            if locale_.startswith(lang):
                lang = locale_
    elif lang.split("-")[1].islower():
        lang = lang.split("-")
        lang[1] = lang[1].upper()
        lang = "-".join(lang)
    return lang if lang in list_bhs else def_bhs


def bahasa(context: str = None):
    if not context:
        cwd = os.getcwd()
        frame = inspect.stack()[1]

        fname = frame.filename

        if fname.startswith(cwd):
            fname = fname[len(cwd) + 1 :]
        context = fname.split(os.path.sep)[2].split(".")[0]

    def decorator(func):
        @wraps(func)
        async def wrapper(c, m):
            lang = await get_bhsnya(user.me.id)

            dic = langdict.get(lang, langdict[def_bhs])

            lfunc = partial(get_bhs_str, dic.get(context, {}), lang, context)
            return await func(c, m, lfunc)

        return wrapper

    return decorator
