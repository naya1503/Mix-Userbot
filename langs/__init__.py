################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || PART OF ULTROID
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
import json
################################################################
import os
import random
import sys
from glob import glob
from typing import Any, Dict, List, Union
from urllib.parse import quote, unquote

import requests
import yaml
from team.nandev.class_log import LOGGER
from team.nandev.database import ndB
from yaml import safe_load

from config import def_bahasa

cek_bahasa = ndB.get_key("bahasa") or def_bahasa

bahasa_ = {}
bahasa_present = {}
loc_lang = "langs/strings/{}.yml"


def _totr(text, lang_src="auto", lang_tgt="auto"):
    GOOGLE_TTS_RPC = ["MkEWBc"]
    parameter = [[text.strip(), lang_src, lang_tgt, True], [1]]
    escaped_parameter = json.dumps(parameter, separators=(",", ":"))
    rpc = [[[random.choice(GOOGLE_TTS_RPC), escaped_parameter, None, "generic"]]]
    espaced_rpc = json.dumps(rpc, separators=(",", ":"))
    freq = "f.req={}&".format(quote(espaced_rpc))
    return freq


def translate(*args, **kwargs):
    headers = {
        "Referer": "https://translate.google.co.in",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/47.0.2526.106 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    x = requests.post(
        "https://translate.google.co.in/_/TranslateWebserverUi/data/batchexecute",
        headers=headers,
        data=_totr(*args, **kwargs),
    ).text
    response = ""
    data = json.loads(json.loads(x[4:])[0][2])[1][0][0]
    subind = data[-2]
    if not subind:
        subind = data[-1]
    for i in subind:
        response += i[0]
    return response


def load(file):
    if not file.endswith(".yml"):
        return
    elif not os.path.exists(file):
        file = loc_lang.format("toxic")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        with open(file, encoding="UTF-8") as f:
            bahasa_data = safe_load(f)
            bahasa_[code] = bahasa_data
    except Exception as er:
        LOGGER.info(f"Error in {file[:-4]}\n\n{er} language file")


load(loc_lang.format(cek_bahasa))


def cgr(key, _res: bool = True):
    lang = cek_bahasa or "toxic"
    try:
        return bahasa_[lang][key]
    except KeyError:
        try:
            en_ = bahasa_["toxic"][key]
            tr = translate(en_, lang_tgt=lang).replace("\ N", "\n")
            if en_.count("{}") != tr.count("{}"):
                tr = en_
            if bahasa_.get(lang):
                bahasa_[lang][key] = tr
            else:
                bahasa_.update({lang: {key: tr}})
            return tr
        except KeyError as e:
            if not _res:
                LOGGER.info(
                    f"Warning: could not load any string with the key `{key}` {e}"
                )
                return
        except TypeError:
            pass
        except Exception as er:
            LOGGER.info(f"Warning: could not load any string with the key `{er}`")
        if not _res:
            return None
        return bahasa_["toxic"].get(key) or LOGGER.info(
            f"Failed to load language string '{key}'"
        )


def get_cgr(key):
    doc = cgr(f"{key}", _res=False)
    if doc:
        return cgr("cmds") + doc


def get_bahasa_() -> List[Dict[str, Union[str, List[str]]]]:
    bahasa_list = []
    for file in glob("langs/strings/*yml"):
        load(file)
    try:
        for code, data in bahasa_.items():
            if data is not None:
                bahasa_list.append(
                    {
                        "code": code,
                        "name": data.get("name", ""),
                        "natively": data.get("natively", ""),
                        "authors": data.get("authors", []),
                    }
                )
        return bahasa_list
    except KeyError as e:
        LOGGER.error(f"KeyError: {e} not found in language file")


for filename in os.listdir(r"./langs/strings/"):
    if "toxic" not in bahasa_:
        bahasa_["toxic"] = yaml.safe_load(
            open(r"./langs/strings/toxic.yml", encoding="utf8")
        )
        bahasa_present["toxic"] = bahasa_["toxic"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "toxic":
            continue
        bahasa_[language_name] = yaml.safe_load(
            open(r"./langs/strings/" + filename, encoding="utf8")
        )
        for item in bahasa_["toxic"]:
            if item not in bahasa_[language_name]:
                bahasa_[language_name][item] = bahasa_["toxic"][item]
    try:
        bahasa_present[language_name] = bahasa_[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        sys.exit(1)
