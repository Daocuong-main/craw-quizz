import os
from deep_translator import GoogleTranslator

input_dir = "Raw"
output_dir = "translated_markdown"

os.makedirs(output_dir, exist_ok=True)

translator = GoogleTranslator(source='en', target='vi')

for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with open(input_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        translated = translator.translate(text=content)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(translated)