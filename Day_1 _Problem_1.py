# 1) Estimate the distribution of vowels, stopwords, and punctuations from a given corpus of text files
from stop_words import get_stop_words
import string
import re
from matplotlib import pyplot as plt

with open("Alice_in_wonderland.txt", 'r') as txt_file:
    all_chars = txt_file.read()
    all_words_list = all_chars.split()

punt_symbols_list = list(string.punctuation)
all_vowels = ['a', 'e', 'i', 'o', 'u']
stop_words_list = get_stop_words('english')


def vowels():

    vowels_dictionary = {vowel: all_chars.lower().count(vowel)for vowel in all_vowels}
    return vowels_dictionary


def stop_words():

    stop_words_dictionary = {stop_word: all_words_list.count(stop_word)for stop_word in stop_words_list}
    return stop_words_dictionary


def punt_symbols():

    punt_symbols_dictionary = {punc_word: all_chars.count(punc_word) for punc_word in punt_symbols_list}
    return punt_symbols_dictionary


def caps():

    caps_dictionary = {}
    for word in all_words_list:
        match = re.search('[A-Z]', word)
        if match:
            if word in caps_dictionary.keys():
                caps_dictionary[word] += 1
            else:
                caps_dictionary[word] = 1
    return caps_dictionary


if __name__ == "__main__":

    vowels_dict = vowels()
    stop_words_dict = stop_words()
    caps_dict = caps()
    punt_symbols_dict = punt_symbols()

    # To print vowels histogram
    plt.bar(vowels_dict.keys(), vowels_dict.values())
    plt.xlabel('vowels')
    plt.ylabel('No of vowels')
    plt.title('Vowels Histogram')
    plt.show()

    # To print stop_words histogram
    plt.bar(stop_words_dict.keys(), stop_words_dict.values())
    plt.xlabel('stop_words')
    plt.ylabel('No of stop_words')
    plt.title('stop_words Histogram')
    plt.show()

    # To print Caps histogram
    plt.bar(caps_dict.keys(), caps_dict.values())
    plt.xlabel('Words in caps')
    plt.ylabel('No of Words in caps')
    plt.title('Words in caps Histogram')
    plt.show()

    # To print punt_symbols histogram
    plt.bar(punt_symbols_dict.keys(), punt_symbols_dict.values())
    plt.xlabel('Punctuation Symbols')
    plt.ylabel('No of Punctuation Symbols')
    plt.title('Punctuation Symbols Histogram')
    plt.show()
