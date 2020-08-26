##
# https://codingbat.com/prob/p170842
# Given a string, return a string where for every
# char in the original, there are two chars.
##
def double_char(string):
    new_string = ''

    for i in range(len(string)):
        new_string += string[i] + string[i]

    return new_string


##
# https://codingbat.com/prob/p167246
# Return the number of times that the string "hi"
# appears anywhere in the given string.
##
def count_hi(string):
    count = 0

    for i in range(len(string) - 1):
        if str[i:i + 2] == 'hi':
            count += 1

    return count


##
# https://codingbat.com/prob/p164876
# Return True if the string "cat" and "dog" appear
# the same number of times in the given string.
##
def cat_dog(string):
    count_cat = 0
    count_dog = 0

    for i in range(len(string) - 2):
        if str[i:i + 3] == 'cat':
            count_cat += 1
        elif str[i:i + 3] == 'dog':
            count_dog += 1

    if count_cat == count_dog:
        return True
    else:
        return False


##
# https://codingbat.com/prob/p186048
# Return the number of times that the string "code" appears
# anywhere in the given string, except we'll accept any
# letter for the 'd', so "cope" and "cooe" count.
##
def count_code(string):
    count = 0

    for i in range(len(string) - 3):
        if str[i:i + 2] == 'co' and str[i + 3:i + 4] == 'e':
            count += 1

    return count


##
# https://codingbat.com/prob/p174314
# Given two strings, return True if either of the strings appears
# at the very end of the other string, ignoring upper/lower case
# differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
##
def end_other(a, b):
    # Find the shorter length string and retrieve that length
    short_len = len(a) if len(a) < len(b) else len(b)

    # Compare the shorter string with 'n' number of chars with the last
    # 'n' chars of the longer string
    if a[len(a) - short_len:].lower() == b[len(b) - short_len:].lower():
        return True
    else:
        return False


##
# https://codingbat.com/prob/p149391
# Return True if the given string contains an appearance of "xyz" where
# the xyz is not directly preceeded by a period (.). So "xxyz" counts
# but "x.xyz" does not.
##
def xyz_there(string):
    # Test for beginning of string
    # as this would be awkward to include in the
    # for-loop
    if str[0:3] == 'xyz':
        return True

    for i in range(len(string) - 2):
        if str[i] != '.' and str[i + 1:i + 4] == 'xyz':
            return True

    return False
