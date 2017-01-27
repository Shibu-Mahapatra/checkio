#  You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.
#
# Input: A string with words.
#
# Output: The answer as a boolean.
#
# Example:
#
# checkio("Hello World hello") == True
#
# checkio("He is 123 man") == False
#
# checkio("1 2 3 4") == False
#
# checkio("bla bla bla bla") == True
#
# checkio("Hi") == False


def checkio(words):
    count = 0
    for word in words.split(' '):
        if word.isalpha():
            if count == 2:
                return True
            count += 1
        else:
            count = 0
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
