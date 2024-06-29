import requests

from bs4 import BeautifulSoup

from googletrans import Translator

translator = Translator()

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def translate_to_russian(text):
    try:
        translated = translator.translate(text, src = 'en', dest = 'ru')
        return translated.text
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        russian_word = translate_to_russian(word)
        russian_definition = translate_to_russian(word_definition)

        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово")
        if user == russian_word:
            print("Верон")
        else:
            print(f"Ответ не верно, загадано слово - {russian_word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру")
            break

word_game()