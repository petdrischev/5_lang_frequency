import collections
from sys import argv


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as text_file:
            text = text_file.read()
        return text
    except FileNotFoundError:
        return ''


def get_most_frequent_words(text):
    words = [word.strip(',.:;"-()').lower() for word in text.split()]
    most_freq_words = collections.Counter(words)
    top_ten = 10
    for word, count in most_freq_words.most_common(top_ten):
        print("Word '{0}' occures: {1} times.".format(word, count))


if __name__ == '__main__':
    filepath = argv[1]
    loaded_text = load_data(filepath)
    get_most_frequent_words(loaded_text)
