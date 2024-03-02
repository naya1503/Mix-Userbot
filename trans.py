import yaml
from gpytranslate import Translator


def translate_yaml(input_file, output_file):
    translator = Translator()

    with open(input_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    for key, value in data.items():
        if isinstance(value, str):
            translated_text = translator.translate(value, source="id", target="en")
            data[key] = translated_text

    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True)


translate_yaml("langs/strings/id.yml", "langs/strings/en.yml")
