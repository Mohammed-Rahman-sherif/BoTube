from googletrans import Translator

translator = Translator()

eng = translator.translate('இரண்டு.')
#tel = translator.translate('இரண்டு.', dest=en)
print(eng)