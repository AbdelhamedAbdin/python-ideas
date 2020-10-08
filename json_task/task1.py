from googletrans import Translator
import json


def search_words(word):
    while True:
        input_word = input(word)
        data = json.load(open("text.json", "r", encoding='utf-8'))

        if input_word in data['words']:
            translator = Translator()
            print(translator.translate(str(input_word), dest='ar').text)
        else:
            data['words'].append(input_word)
            json.dump(data, open("text.json", "w+"), indent=4)
            data = json.load(open("text.json", "r+"))
            print("Word not found. please input a definition")
        # turn off the loop
        if input_word == '':
            return


search_words("your word: ")