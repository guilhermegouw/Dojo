"""
The Challenge

We are given m words. The words are not necessarily distinct;
For example:
The word brook could appear multiple times.
We are also given an integer k.
Our task is to find the kth most common words.
A word w is a kth most common word if exactly k – 1 distinct words occur more
often than does w.
Depending on the dataset, the kth most common words could be no words,
one word, or more than one word.
Let’s make sure we’re clear on this definition of the kth most common words.
If k = 1, then we’re being asked for the words for which exactly 0 words
occur more often; that is, we’re being asked for the words that occur most
often.
If k = 2, then we’re being asked for the words for which exactly 1 word
occurs more often.
If k = 3, then we’re being asked for the words for which exactly two distinct
words occur more often, and so on.

Input
- A list of words.
- k

Output
- A list with the kth most common words.
"""
from collections import Counter


def get_kth_most_common_words(words, k):
    words_freq = Counter(words)
    frequencies = sorted(set(words_freq.values()), reverse=True)
    kth_most_common_words = []
    if k > len(frequencies):
        return []
    else:
        for word, freq in words_freq.items():
            if freq == frequencies[k-1]:
                kth_most_common_words.append(word)
    return kth_most_common_words
