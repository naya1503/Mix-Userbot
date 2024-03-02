import os
import sys
from glob import glob
from typing import Any, Dict, List, Union

from yaml import safe_load
from team.nandev.database import ndB
from team.nandev.class_log import LOGGER

cek_bahasa = ndB.get_key("bahasa")

bahasa_ = {}
loc_lang = "langs/{}.yml"


def load(file):
    if not file.endswith(".yml"):
        return
    elif not os.loc_lang.exists(file):
        file = loc_lang.format("id")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        bahasa_[code] = safe_load(
            open(file, encoding="UTF-8"),
        )
    except Exception as er:
        LOGGER.info(f"Error in {file[:-4]}\n\n{er} language file")


load(loc_lang.format(cek_bahasa))


def bahasa(key: str, _res: bool = True) -> Any:
    lang = cek_bahasa or "id"
    try:
        return bahasa_[lang][key]
    except KeyError:
        try:
            id_ = bahasa_["id"][key]
            tr = translate(id_, lang_tgt=lang).replace("\ N", "\n")
            if id_.count("{}") != tr.count("{}"):
                tr = id_
            if bahasa_.get(lang):
                bahasa_[lang][key] = tr
            else:
                bahasa_.update({lang: {key: tr}})
            return tr
        except KeyError:
            if not _res:
                return
            LOGGER.info(f"Warning: could not load any string with the key `{key}`")
            return
        except TypeError:
            pass
        except Exception as er:
            LOGGER.error(f"{er}")
        if not _res:
            return None
        return bahasa_["id"].get(key) or LOGGER.info(f"Failed to load language string '{key}'")


def get_help(key):
    doc = get_string(f"cgr_{key}", _res=False)
    if doc:
        return get_string("cmds") + doc


def get_bahasa_() -> Dict[str, Union[str, List[str]]]:
    for file in glob("langs/*yml"):
        load(file)
    return {
        code: {
            "nama": bahasa_[code]["nama"],
            "penulis": bahasa_[code]["penulis"],
        }
        for code in bahasa_
    }
