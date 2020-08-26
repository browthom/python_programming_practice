##
# https://codingbat.com/prob/p193507
# Given a string and a non-negative int n, return
# a larger string that is n copies of the original
# string.
##
def string_times(string, n):
    new_string = ''

    for i in range(n):
        new_string += string

    return new_string


##
# https://codingbat.com/prob/p165097
# Given a string and a non-negative int n, we'll say
# that the front of the string is the first 3 chars,
# or whatever is there if the string is less than
# length 3. Return n copies of the front;
##
def front_times(string, n):
    new_str = ''
    for i in range(n):
        new_str += string[:3]

    return new_str


##
# https://codingbat.com/prob/p113152
# Given a string, return a new string made of every
# other char starting with the first, so "Hello"
# yields "Hlo".
##
def string_bits(string):
    i = 0
    new_str = ''

    while i < len(string):
        new_str += string[i:i + 1]
        i += 2

    return new_str


##
# https://codingbat.com/prob/p118366
# Given a non-empty string like "Code" return a
# string like "CCoCodCode".
##
def string_splosion(string):
    new_str = ''

    for i in range(len(string)):
        new_str += string[0:i + 1]

    return new_str


##
# https://codingbat.com/prob/p145834
# Given a string, return the count of the number of
# times that a substring length 2 appears in the
# string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).
##
def last2(string):
    end = string[-2:]
    count = 0

    for i in range(len(string) - 2):
        if string[i:i + 2] == end:
            count += 1

    return count


##
# https://codingbat.com/prob/p166170
# Given an array of ints, return the number of 9's in the array.
##
def array_count9(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1

    return count


##
# https://codingbat.com/prob/p110166
# Given an array of ints, return True if one of the
# first 4 elements in the array is a 9. The array
# length may be less than 4.
##
def array_front9(nums):
    size = 4 if (len(nums) > 4) else len(nums)

    for i in range(size):
        if nums[i] == 9:
            return True

    return False


##
# https://codingbat.com/prob/p193604
# Given an array of ints, return True if the sequence
# of numbers 1, 2, 3 appears in the array somewhere.
##
def array123(nums):
    for i in range(len(nums) - 2):
        if (nums[i] == 1 and
                nums[i + 1] == 2 and
                nums[i + 2] == 3):
            return True

    return False


##
# https://codingbat.com/prob/p182414
# Given 2 strings, a and b, return the number of
# the positions where they contain the same length
# 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
# since the "xx", "aa", and "az" substrings appear
# in the same place in both strings.
##
def string_match(a, b):
    count = 0

    size = a if (a < b) else b

    for i in range(len(size) - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1

    return count
