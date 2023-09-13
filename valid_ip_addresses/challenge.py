"""
given a string of length 12 or smaller, containing only digits, return all the 
possible IP addresses that can be created by inserting three .s in the string.

An IP address is a sequence of four positive integers that are separated by .s,
where each individual integer is within the range 0-255, inclusive.

An IP address isn't valid if any of the individual integers contains leading 0s.

For example:

"192.168.0.1" is valid IP address, but "192.168.00.1" and "192.168.0.01" aren't
valid IP addresses, because they contain "00" and 01, respectively. 
Similarly, another example of a valid IP address is "99.1.1.10"; conversely,
"991.1.1.0" isn't valid IP address, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular
order. 
If no valid IP addresses can be created from the string, your function should
return an empty list.

Note: check out our Systems Design Fundamentals on SystemsExpert to learn more
about IP addresses!


Sample Input:
string = "1921680"

Sample Output:
[
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0"
]

if the input length is less than 4, return an empty list
if the input length is greater than 12, return an empty list

if the input length is 4, return the input string with 3 .s inserted
"1234" -> ["1.2.3.4"]

if the input length is 5, return the input string with 3 .s inserted
"12345" -> [
    "1.2.3.45",
    "1.2.34.5",
    "1.23.4.5",
    "12.3.4.5",
]

if the input length is 6, return the input string with 3 .s inserted
"123456" -> [
    "1.2.34.56",
    "1.23.45.6",
    "12.34.5.6",
    "123.4.5.6",
    "1.234.5.6",
]

...
"""


def validIPAddresses(string):
    if len(string) < 4 or len(string) > 12:
        return []

    result = []
    for i in range(1, len(string)):
        for j in range(i + 1, len(string)):
            for k in range(j + 1, len(string)):
                if isValid(string, i, j, k):
                    result.append(
                        string[:i] + "." + string[i:j] + "." + string[j:k] + "." + string[k:]
                    )

    return result

def isValid(string, i, j, k):
    first = string[:i]
    second = string[i:j]
    third = string[j:k]
    fourth = string[k:]

    if not isValidPart(first) or not isValidPart(second) or not isValidPart(third) or not isValidPart(fourth):
        return False

    return True

def isValidPart(string):
    if len(string) > 3:
        return False

    if string[0] == "0" and len(string) > 1:
        return False

    if int(string) > 255:
        return False

    return True
