from googletrans import Translator

# Supported languages dictionary
SUPPORTED_LANGUAGES = {
    'hindi': 'hi',
    'tamil': 'ta',
    'bengali': 'bn',
    'gujarati': 'gu',
    'telugu': 'te',
    'punjabi': 'pa',
    'kannada': 'kn',
    'malayalam': 'ml',
    'marathi': 'mr',
    'urdu': 'ur',
}

# ✅ Function to load translator based on language
def load_translator(target_language):
    lang_code = SUPPORTED_LANGUAGES.get(target_language.lower())
    if not lang_code:
        raise ValueError(f"Unsupported language: {target_language}")

    translator = Translator()

    def translate_fn(text):
        result = translator.translate(text, dest=lang_code)
        return result.text

    return translate_fn

# ✅ Function to run translation
def translate_text(translate_fn, text):
    return translate_fn(text)
