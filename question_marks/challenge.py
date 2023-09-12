"""
Questions Marks

Have the function QuestionsMarks(str) take the str string parameter, which will 
contain single digit numbers, letters, and question marks, and check if there 
are exactly 3 question marks between every pair of two numbers that 
add up to 10. 
If so, then your program should return the string true, otherwise it should 
return the string false. 
If there aren't any two numbers that add up to 10 in the string, then your 
program should return false as well.

For example: 
if str is "arrb6???4xxbl5???eee5" 
then your program should return true 
because there are exactly 3 question marks between 6 and 4, and 3 question marks 
between 5 and 5 at the end of the string.

Examples

Input: "aa6?9"
Output: false

Input: "acc?7??sss?3rr1??????5"
Output: true
"""
import re


def QuestionsMarks(strParam):
    numbers = re.findall(r'\d', strParam)
    if len(numbers) < 2:
        return False
    digits_indexes = get_digits_indexes(strParam)
    for index, item in enumerate(digits_indexes):
        try:
            if item[1] + digits_indexes[index + 1][1] >= 10:
                str_slice = strParam[item[0]:digits_indexes[index + 1][0]]
                if count_question_marks(str_slice) == 3:
                    return True
        except IndexError:
            return False
    return False

def get_digits_indexes(string):
    digits = []
    for index, char in enumerate(string):
        if char.isdigit():
            digits.append((index, int(char)))
    return digits

def count_question_marks(str_slice):
    count = 0
    for char in str_slice:
        if char == '?':
            count += 1
    return count


if __name__ == '__main__':
    print(QuestionsMarks("aa6?9"))
    print(QuestionsMarks("acc?7??sss?3rr1??????5"))
    print(QuestionsMarks("arrb6???4xxbl5???eee5"))
    print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))
    print(QuestionsMarks("9???1???9???1???9"))
    print(QuestionsMarks("aa6?9"))
    print(QuestionsMarks("4?5?4?aamm9"))
    print(QuestionsMarks("5??a"))
    print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))