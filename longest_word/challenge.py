"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and 
return the longest word in the string. 
If there are two or more words that are the same length, return the first word 
from the string with that length. Ignore punctuation and assume sen will not 
be empty. 
Words may also contain numbers
For example "Hello world123 567"

Examples
Input: "fun&!! time"
Output: time

Input: "I love dogs"
Output: love
"""
import re


def LongestWord(sen):
    words = sen.split()
    longest_word = ''
    for word in words:
        if len(remove_punctuation(word)) > len(longest_word):
            longest_word = remove_punctuation(word)
    return longest_word

def remove_punctuation(word):
  cleaned_word = re.sub(r'[^a-zA-Z0-9_]', '', word)
  return cleaned_word


if __name__ == '__main__':
    print(LongestWord("fun&!! time"))
    print(LongestWord("I love dogs"))
    print(LongestWord("Hello world123 567"))
