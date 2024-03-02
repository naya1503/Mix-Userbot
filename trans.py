import yaml
import asyncio
from gpytranslate import Translator

async def translate_yaml(input_file, output_file, target_language):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    translator = Translator()

    for key, value in data.items():
        if isinstance(value, str):
            translated_value = await translate_text_within_quotes(value, translator, target_language)
            data[key] = translated_value
        elif isinstance(value, list):
            translated_list = []
            for item in value:
                if isinstance(item, str):
                    translated_item = await translate_text_within_quotes(item, translator, target_language)
                    translated_list.append(translated_item)
                else:
                    translated_list.append(item)
            data[key] = translated_list

    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)

async def translate_text_within_quotes(text, translator, target_language):
    parts = text.split('"')
    translated_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not within quotes
            translated_part = await translator.translate(part, target_language=target_language)
            translated_parts.append(translated_part)
        else:  # Within quotes
            translated_parts.append(part)
    return ''.join(translated_parts)

async def main():
    await translate_yaml('langs/strings/id.yml', 'langs/strings/en.yml', 'en')

if __name__ == "__main__":
    asyncio.run(main())
