# Frequency Analysis of Words

Module return  on console fisrt ten most frequences words which occures in text.

# How use

Module contains 2 functions:
```python
def load_data(filepath):
    ...
    return text
  
  
def get_most_frequent_words(text):
    ...
    return most_freq_words

```
Where filepath, it's path to load text file. Example:
```python
import lang_frequency
filepath = "./text_file.txt"
loaded_text = load_data(filepath)
most_freq_words = get_most_frequent_words(loaded_text)
for word_count_couples in most_freq_words:
    print(word_count_couples[0])
```

# Quickstart

Example of script launch on Linux, Python 3.5:
```bash
$ python lang_frequency.py <path to file>
# output example
#
#Top 10 most frequent word in order ascrement in loaded text:
#the and you to a of alice i it in
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
