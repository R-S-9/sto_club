import enchant
import difflib


class SuggestWord:
    @staticmethod
    def get_search_word_by_guess(right_word: str) -> list:
        list_of_search_word = []  # Список возможных введенных услуг
        sim = dict()
        dictionary = enchant.Dict("ru_RU")
        suggestions = set(dictionary.suggest(right_word))

        for word in suggestions:
            measure = difflib.SequenceMatcher(None, right_word, word).ratio()
            sim[measure] = word

        for probability, value in sim.items():
            if probability > 0.9:
                list_of_search_word.append(value)

        if len(list_of_search_word) < 2:
            list_of_search_word = set(list_of_search_word + list(suggestions))

        return list(list_of_search_word)
