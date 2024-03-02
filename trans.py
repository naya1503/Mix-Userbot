import os

import yaml
from gpytranslate import Translator


async def translate_file(file_path, translator, target_lang):
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    translated_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            key_parts = key.split(":")
            translated_key = key_parts[0].strip() + ":"
            translated_value = await translator.translate(
                value.strip(), target_lang=target_lang
            )
            translated_data[translated_key] = translated_value
        elif isinstance(value, dict):
            translated_data[key] = await translate_nested(
                value, translator, target_lang
            )
        else:
            translated_data[key] = value

    return translated_data


async def translate_nested(data, translator, target_lang):
    translated_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            translated_value = await translate_nested(value, translator, target_lang)
        else:
            translated_value = await translator.translate(
                value.strip(), target_lang=target_lang
            )
        translated_data[key] = translated_value
    return translated_data


async def main():
    translator = Translator()
    # Ganti dengan kode bahasa target Anda
    target_lang = "en"

    files_to_translate = [
        file
        for file in os.listdir("langs/strings")
        if file.endswith(".yml") and file != "id.yml"
    ]

    for file_name in files_to_translate:
        input_file = os.path.join("langs/strings", file_name)
        output_file = os.path.join("langs/strings", f"{target_lang}_{file_name}")

        translated_data = await translate_file(input_file, translator, target_lang)

        with open(output_file, "w", encoding="utf-8") as output:
            yaml.dump(translated_data, output, allow_unicode=True)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
