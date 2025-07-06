import json

user_languages = {}

def load_translations(lang_code):
    path = f"locales/{lang_code}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

translations = {
    "ru": load_translations("ru"),
    "uz": load_translations("uz"),
    "kk": load_translations("kk")
}

def translate(key, lang="ru"):
    return translations.get(lang, translations["ru"]).get(key, key)

async def get_user_language(user_id):
    return user_languages.get(user_id, "ru")

async def set_user_language(user_id, lang):
    user_languages[user_id] = lang