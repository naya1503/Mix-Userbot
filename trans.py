import yaml
from gpytranslate import Translator

# Fungsi untuk menerjemahkan teks menggunakan Google Translate API
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, target_language=target_language)
    return translated_text

# Fungsi untuk menerjemahkan string YAML
def translate_yaml(yaml_file, target_language):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Menerjemahkan nilai teks di dalam tanda kutip menggunakan Google Translate
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = translate_text(value, target_language)
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, str):
                    value[sub_key] = translate_text(sub_value, target_language)

    # Menghasilkan string YAML yang telah diterjemahkan
    translated_yaml = yaml.dump(data, allow_unicode=True)

    return translated_yaml

# Menjalankan fungsi untuk menerjemahkan string YAML dan menyimpannya ke file
translated_yaml = translate_yaml('langs/strings/id.yml', 'en')
with open('translated_strings.yml', 'w') as file:
    file.write(translated_yaml)
