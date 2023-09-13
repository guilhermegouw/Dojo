"""
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

list_of_anagrams = []

we are going to run through the list of words.
if the word is not inside one of the elements of list_of_anagrams, we are going 
to create a new element in list_of_anagrams.
        
words first item is "yo"
sorted("yo") is not equal to any sorted(item) inside of the elements from list_of_anagrams
we are going to create a new element in list_of_anagrams
list_of_anagrams = [["yo"]]
words second item is "act"
sorted("act") is not equal to any sorted(item) inside of the elements from list_of_anagrams
we are going to create a new element in list_of_anagrams
list_of_anagrams = [["yo"], ["act"]]
words third item is "flop"
sorted("flop") is not equal to any sorted(item) inside of the elements from list_of_anagrams
we are going to create a new element in list_of_anagrams
list_of_anagrams = [["yo"], ["act"], ["flop"]]
words fourth item is "tac"
sorted("tac") is equal to sorted("act") that is inside of the second element from list_of_anagrams
we are going to append "tac" to the second element from list_of_anagrams
list_of_anagrams = [["yo"], ["act", "tac"], ["flop"]]
words fifth item is "foo"
sorted("foo") is not equal to any sorted(item) inside of the elements from list_of_anagrams
we are going to create a new element in list_of_anagrams
list_of_anagrams = [["yo"], ["act", "tac"], ["flop"], ["foo"]]
words sixth item is "cat"
sorted("cat") is equal to sorted("act") that is inside of the second element from list_of_anagrams
we are going to append "cat" to the second element from list_of_anagrams
list_of_anagrams = [["yo"], ["act", "tac", "cat"], ["flop"], ["foo"]]
words seventh item is "oy"
sorted("oy") is equal to sorted("yo") that is inside of the first element from list_of_anagrams
we are going to append "oy" to the first element from list_of_anagrams
list_of_anagrams = [["yo", "oy"], ["act", "tac", "cat"], ["flop"], ["foo"]]
words eighth item is "olfp"
sorted("olfp") is equal to sorted("flop") that is inside of the third element from list_of_anagrams
we are going to append "olfp" to the third element from list_of_anagrams
list_of_anagrams = [["yo", "oy"], ["act", "tac", "cat"], ["flop", "olfp"], ["foo"]]
We ran through all the words and we have in words. So, we are done.
return list_of_anagrams
"""


def groupAnagrams(words):
    list_of_anagrams = []
    for word in words:
        sorted_word = sorted(word)
        for anagram in list_of_anagrams:
            if sorted_word == sorted(anagram[0]):
                anagram.append(word)
                break
        else:
            list_of_anagrams.append([word])
    return list_of_anagrams


if __name__ == '__main__':
    groupAnagrams(["zxc", "cxz"])