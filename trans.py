import yaml
import asyncio
from gpytranslate import Translator

async def translate_yaml(input_file, output_file, target_language):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    translator = Translator()

    for key, value in data.items():
        if isinstance(value, str):
            parts = value.split('"')
            for i in range(1, len(parts), 2):
                translation = await translator.translate(parts[i], target_language=target_language)
                parts[i] = translation
            data[key] = '"'.join(parts)
        elif isinstance(value, list):
            translated_list = []
            for item in value:
                if isinstance(item, str):
                    parts = item.split('"')
                    for i in range(1, len(parts), 2):
                        translation = await translator.translate(parts[i], target_language=target_language)
                        parts[i] = translation
                    translated_list.append('"'.join(parts))
                else:
                    translated_list.append(item)
            data[key] = translated_list

    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True, Dumper=yaml.SafeDumper)

async def main():
    await translate_yaml('langs/strings/id.yml', 'langs/strings/en.yml', 'en')

if __name__ == "__main__":
    asyncio.run(main())
