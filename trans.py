import asyncio

import yaml
from gpytranslate import Translator


async def translate_yaml(input_file, output_file, target_language):
    with open(input_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    translator = Translator()

    for key, value in data.items():
        if isinstance(value, str):
            translation = await translator.translate(
                value, target_language=target_language
            )
            data[key] = translation
        elif isinstance(value, list):
            translated_list = []
            for item in value:
                if isinstance(item, str):
                    translation = await translator.translate(
                        item, target_language=target_language
                    )
                    translated_list.append(translation)
                else:
                    translated_list.append(item)
            data[key] = translated_list

    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True, default_flow_style=False)


async def main():
    await translate_yaml("langs/strings/id.yml", "langs/strings/en.yml", "en")


if __name__ == "__main__":
    asyncio.run(main())
