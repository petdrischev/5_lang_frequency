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
    count_words = {word: words.count(word) for word in words}
    counts = [count for count in count_words.values()]
    most_freq_words = {}
    for _ in range(len(counts)):
        for word in count_words:
            if len(most_freq_words) >= 10:
                break
            if count_words[word] == max(counts):
                most_freq_words[word] = max(counts)
        counts.remove(max(counts))
    for word, count in most_freq_words.items():
        print("Word '{0}' occures: {1} times.".format(word, count))


if __name__ == '__main__':
    script, filepath = argv
    loaded_text = load_data(filepath)
    get_most_frequent_words(loaded_text)
