"""
A message has been encoded as a text stream that is to be read character by
character. The stream contains a series of comma-delimited integers, each a
positive number capable of being represented by a C++ int. However, the
character represented by a particular integer depends on the current decoding
mode.

There are three modes:
uppercase, lowercase, and punctuation.

In uppercase mode, each integer represents an uppercase letter: The integer
modulo 27 indicates the letter of the alphabet (where 1 = A and so on).
So an input value of 143 in uppercase mode would yield the letter H because 143
modulo 27 is 8 and H is the eighth letter in the alphabet.

The lowercase mode works the same but with lowercase letters; the remainder of
dividing the integer by 27 represents the lowercase letter (1 = a and so on).
So an input value of 56 in lowercase mode would yield the letter b because 56
modulo 27 is 2 and b is the second letter in the alphabet.

In punctuation mode, the integer is instead considered modulo 9, with the
interpretation given by Table below. So 19 would yield an exclamation
point because 19 modulo 9 is 1.

---------------
|1 |  !       |
|2 |  ?       |
|3 |  ,       |
|4 |  .       |
|5 |  (space) |
|6 |  ;       |
|7 |  "       |
|8 |  '       |
---------------

At the beginning of each message, the decoding mode is uppercase letters.
Each time the modulo operation (by 27 or 9, depending on mode) results in 0,
the decoding mode switches.
If the current mode is uppercase, the mode switches to lowercase letters.
If the current mode is lowercase, the mode switches to punctuation, and
if it is punctuation, it switches back to uppercase.

Input

The input consists of a series of comma-delimited integers.

Output

The output should consist of the decoded message.


Example:

Input:
18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10

------------------
|18   |U|27|18|R  |
|12312|U|27|10|-> | L
|171  |L|27|6 |i  |
|763  |L|27|7 |g  |
|98423|L|27|8 |h  |
|1208 |L|27|20|t  |
|216  |L|27|0 |-> | P
|11   |P|9 |2 |?  |
|500  |P|9 |5 |' '|
|18   |P|9 |0 |-> | U
|241  |U|27|25|Y  |
|0    |U|27|0 |-> | L
|32   |L|27|5 |e  |
|20620|L|27|19|s  |
|27   |L|27|0 |-> | P
|10   |P|9 |1 |!  |
------------------

Output:
Right? Yes!
"""


def decode_upper_mode(value: str) -> str:
    value = int(value)
    return chr(value % 27 + 64)


def decode_lower_mode(value: str) -> str:
    value = int(value)
    return chr(value % 27 + 96)


def decode_punctuation_mode(value: str) -> str:
    punctuations = {
        1: "!",
        2: "?",
        3: ",",
        4: ".",
        5: " ",
        6: ";",
        7: '"',
        8: "'",
    }

    value = int(value)
    return punctuations[value % 9]


def decode_message(message: str) -> str:
    mode = "U"
    decoded = ""
    for value in message.split(","):
        if mode == "U":
            if int(value) % 27 == 0:
                mode = "L"
            else:
                decoded += decode_upper_mode(value)
        elif mode == "L":
            if int(value) % 27 == 0:
                mode = "P"
            else:
                decoded += decode_lower_mode(value)
        elif mode == "P":
            if int(value) % 9 == 0:
                mode = "U"
            else:
                decoded += decode_punctuation_mode(value)
    return decoded
