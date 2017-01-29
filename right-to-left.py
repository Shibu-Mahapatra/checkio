# You are given a sequence of strings. You should join these strings into chunk of text
# where the initial strings are separated by commas.
# you should replace all cases of the words "right" with the word "left",
# even if it's a part of another word. All strings are given in lowercase.
#
# Input: A sequence of strings as a tuple of strings (unicode).
#
# Output: The text as a string.
#
# Example:
#
# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
#
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
#
# left_join(("brightness wright",)) == "bleftness wleft"
#
# left_join(("enough", "jokes")) == "enough,jokes"



def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return ','.join(phrases).replace("right", "left")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
