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
    counted_words = collections.Counter(words)
    top_ten = 10
    most_freq_words = counted_words.most_common(top_ten)
    return most_freq_words


if __name__ == '__main__':
    filepath = argv[1]
    loaded_text = load_data(filepath)
    most_freq_words = get_most_frequent_words(loaded_text)
    print("\nTop 10 most frequent word in order ascrement in loaded text:")
    for word_count_couples in most_freq_words:
        print('{}'.format(word_count_couples[0]), end=' ')
    print('\n')
