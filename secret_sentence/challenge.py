"""
The Challenge

Luka is writing a secret sentence in class.
He doesn’t want the teacher to be able to read it, so instead of
writing down the original sentence, he writes down an encoded version.
After each vowel in the sentence (a, e, i, o, or u), he adds the
letter p and that vowel again.

For example:
    Rather than write down the sentence "i like you"
    he would write "ipi lipikepe yopoupu".

The teacher acquires Luka’s encoded sentence.
Recover Luka’s original sentence for the teacher.

Input

The input is one line of text, Luka’s encoded sentence.
It consists of lowercase letters and spaces.
There is exactly one space between each pair of words.

Output

Output Luka’s original sentence.
"""

import time


def decode_luka(sentence):
    vowels = "aeiou"
    decode = ""
    i = 0
    while i < len(sentence):
        decode += sentence[i]
        if sentence[i] in vowels:
            i += 2
        i += 1
    return decode


def decode_luka_comprehension(sentence):
    vowels = "aeiou"
    return "".join(
        sentence[i]
        for i in range(len(sentence))
        if not (
            sentence[i] in vowels
            and i + 2 < len(sentence)
            and sentence[i + 1] == "p"
            and sentence[i + 2] == sentence[i]
        )
    )


def decode_luka_generator(sentence):
    vowels = "aeiou"
    i = 0
    while i < len(sentence):
        yield sentence[i]
        if sentence[i] in vowels:
            i += 2
        i += 1


if __name__ == "__main__":
    sentence = "ipi lipikepe yopoupu" * 1000000

    # common loop
    start = time.time()
    result = decode_luka(sentence)
    print("common loop:", time.time() - start)

    # comprehension
    start = time.time()
    result = decode_luka_comprehension(sentence)
    print("comprehension:", time.time() - start)

    # generator
    start = time.time()
    result = "".join(decode_luka_generator(sentence))
    print("generator:", time.time() - start)
