
from deep_translator import MyMemoryTranslator

def englishTofrench(english_text):
    french_text = MyMemoryTranslator(source= 'en', target='fr').translate(english_text)
    print(french_text)
    return french_text
def frenchToenglish(french_text):
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text

    