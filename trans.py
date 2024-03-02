import asyncio

import yaml
from gpytranslate import Translator


async def translate_text(text):
    translator = Translator()
    translated_text = await translator.translate(text, source="id", target="en")
    return translated_text


async def translate_yaml(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    tasks = []
    for key, value in data.items():
        if isinstance(value, str):
            tasks.append(translate_text(value))

    translated_texts = await asyncio.gather(*tasks)

    translated_data = {}
    index = 0
    for key, value in data.items():
        if isinstance(value, str):
            translated_data[key] = translated_texts[index]
            index += 1
        else:
            translated_data[key] = value

    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(translated_data, file, allow_unicode=True)


asyncio.run(translate_yaml("langs/strings/id.yml", "langs/strings/en.yml"))
