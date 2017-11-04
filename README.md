# Frequency Analysis of Words

Module return fisrt ten most frequences words which occures in text.

# How use

Module contains 2 functions:
```python
def load_data(filepath):
    ...
    return text
  
  
def get_most_frequent_words(text):
    ...
    print(f"Word '{word}' occures: {count} times.")

```
Where filepath, it's path to load text file. Example:
```python
import lang_frequency
filepath = "./text_file.txt"
loaded_text = load_data(filepath)
get_most_frequent_words(loaded_text)
```

# Quickstart

Example of script launch on Linux, Python 3.5:
```bash
$ python lang_frequency.py <path to file>
# output example
#Word 'the' occures: 839 times.
#Word 'and' occures: 460 times.
#Word 'you' occures: 444 times.
#Word 'to' occures: 400 times.
#Word 'a' occures: 387 times.
#Word 'of' occures: 382 times.
#Word 'alice' occures: 370 times.
#Word 'i' occures: 338 times.
#Word 'it' occures: 238 times.
#Word 'in' occures: 216 times.
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
