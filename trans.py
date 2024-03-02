import ruamel.yaml
from gpytranslate import Translator


def translate_quoted_text(data, translator):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = translate_quoted_text(value, translator)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = translate_quoted_text(data[i], translator)
    elif isinstance(data, str) and data.startswith('"') and data.endswith('"'):
        # Terjemahkan teks di dalam tanda kutip
        translated_text = translator.translate(data[1:-1], src="id", dest="en").text
        data = f'"{translated_text}"'
    return data


def main():
    input_yaml_file = "id.yml"
    output_yaml_file = "en.yml"

    yaml = ruamel.yaml.YAML()
    with open(input_yaml_file, "r") as file:
        data = yaml.load(file)

    translator = Translator()
    data = translate_quoted_text(data, translator)

    with open(output_yaml_file, "w") as file:
        yaml.dump(data, file)


if __name__ == "__main__":
    main()
