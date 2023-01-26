from googletrans import Translator

# Initialize the translator
translator = Translator()

try:
    # Open the file for reading
    with open('../Contents/cWzjP.txt', 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
        
    # Translate the text
    translation = translator.translate(file_contents, dest='ta')

    # Open the file for writing
    with open('../Contents/ta/cWzjp.txt', 'w', encoding='utf-8') as file:
        # Write the translation to the file
        file.write(translation.text)

except Exception as e:
    print(f'An error occurred: {e}')
