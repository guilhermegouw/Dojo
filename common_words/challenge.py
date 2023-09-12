"""
The Challenge

We are given m words. The words are not necessarily distinct; 
For example: 
the word brook could appear multiple times. 
We are also given an integer k.
Our task is to ﬁnd the kth most common words. 
A word w is a kth most common word if exactly k - 1 distinct words occur more 
often than does w. 
Depending on the dataset, the kth most common words could be no words, 
one word, or more than one word.
Let's make sure we're clear on this deﬁnition of the kth most common words. 
If k = 1, then we're being asked for the words for which exactly 0 words occur 
more often; that is, we're being asked for the words that occur most often. 
If k = 2, then we're being asked for the words for which exactly 1 word occurs 
more often. 
If k = 3, then we're being asked for the words for which exactly two distinct 
words occur more often, and so on.

Input

The input contains a line giving the number of test cases, followed by the 
lines of the test cases themselves. 
Each test case contains the following lines:
- A line containing the integers m (the number of words in the test case) 
and k separated by a space. 
m is between 0 and 1,000; k is at least 1.
- m lines, each of which gives a word. 
Each word consists of at most 20 characters, and all characters are lowercase.

Output

For each test case, output the following lines:
- A line containing the following:
p most common word(s):
where p is 1st if k is 1, 2nd if k is 2, 3rd if k is 3, 4th if k is 4,
and so on.
- One line for each of the kth most common words. 
If there are no such words, there are no lines of output here.
- A blank line.
The time limit for solving the test cases is one second.
"""


def get_common_words(k, *words):
    word_freq = {}
    for word in words:
        freq = words.count(word)
        if freq in word_freq:
            if word not in word_freq[freq]:
                word_freq[freq].append(word)
        else:
            word_freq[freq] = [word]
    try:
        return word_freq[sorted(word_freq.keys())[-k]]
    except IndexError:
        return None