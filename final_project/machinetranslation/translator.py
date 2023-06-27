from deep_translator import MyMemoryTranslator

"""this function translate english to french"""
def englishToFrench(english_text):
    french_text = MyMemoryTranslator(source= 'en', target='fr').translate(english_text)
    return french_text
"""this function translate french to english"""
def frenchToEnglish(french_text):
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
