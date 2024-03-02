################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || PART OF ULTROID
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

import json
import random
import sys
from glob import glob
from typing import Any, Dict, List, Union

import requests
from team.nandev.class_log import LOGGER
from team.nandev.database import ndB
from yaml import safe_load

from Mix.core.http import http

cek_bahasa = ndB.get_key("bahasa")
from urllib.parse import quote, unquote

bahasa_ = {}
loc_lang = "langs/strings/{}.yml"




def load(file):
    if not file.endswith(".yml"):
        return
    file = loc_lang.format("id")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        bahasa_[code] = safe_load(
            open(file, encoding="UTF-8"),
        )
    except Exception as er:
        LOGGER.info(f"Error in {file[:-4]}\n\n{er} language file")


load(loc_lang.format(cek_bahasa))


def cgr(key, _res: bool = True):
    lang = cek_bahasa
    try:
        return bahasa_[lang][key]
    except KeyError:
        try:
            id_ = bahasa_["id"][key]
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
        return bahasa_["id"].get(key) or LOGGER.info(
            f"Failed to load language string '{key}'"
        )


def get_cgr(key):
    doc = cgr(f"cgr_{key}", _res=False)
    if doc:
        return cgr("cmds") + doc


def get_bahasa_():
    for file in glob("langs/strings/*yml"):
        load(file)
    return {
        code: {
            "nama": bahasa_[code]["nama"],
            "penulis": bahasa_[code]["penulis"],
        }
        for code in bahasa_
    }
