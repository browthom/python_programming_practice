
##
# https://codingbat.com/prob/p118406
# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks
# (5 inches each). Return True if it is possible to make the goal
# by choosing from the given bricks. This is a little harder than
# it looks and can be done without any loops. See also:
# Introduction to MakeBricks
##
def make_bricks(small, big, goal):
    max_size = small + big * 5

    # If there's not enough length to begin with
    if goal > max_size:
        return False
    else:
        # Amount of big bricks that can be added to goal
        remove_big = int(goal / 5)

        # Add as many big bricks as you can to goal
        goal -= remove_big * 5
        # If there are enough small bricks to complete goal
        if goal <= small:
            return True
        else:
            return False


##
# https://codingbat.com/prob/p143951
# Given 3 int values, a b c, return their sum.
# However, if one of the values is the same as
# another of the values, it does not count
# towards the sum.
##
def lone_sum(a, b, c):
    if a == b and b != c:
        return c
    elif a != b and b == c:
        return a
    elif a == c and a != b:
        return b
    elif a == b and b == c and a == c:
        return 0
    else:
        return a+b+c


##
# https://codingbat.com/prob/p107863
# Given 3 int values, a b c, return their sum.
# However, if one of the values is 13 then it
# does not count towards the sum and values to
# its right do not count. So for example,
# if b is 13, then both b and c do not count.
##
def lucky_sum(a, b, c):
    return ((a if (a != 13) else 0) +
            (b if (a != 13 and b != 13) else 0) +
            (c if (a != 13 and b != 13 and c != 13) else 0))


##
# https://codingbat.com/prob/p100347
# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen -- in
# the range 13..19 inclusive -- then that value
# counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in
# an int value and returns that value fixed for the teen
# rule. In this way, you avoid repeating the teen code 3
# times (i.e. "decomposition"). Define the helper below
# and at the same indent level as the main no_teen_sum().
##
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


##
# Helper function for 'no_teen_sum'
##
def fix_teen(n):
    if (13 <= n < 15) or (16 < n <= 19):
        return 0
    else:
        return n


##
# https://codingbat.com/prob/p179960
# For this problem, we'll round an int value up
# to the next multiple of 10 if its rightmost
# digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple
# of 10 if its rightmost digit is less than 5,
# so 12 rounds down to 10. Given 3 ints, a b c,
# return the sum of their rounded values.
# To avoid code repetition, write a separate
# helper "def round10(num):" and call it 3 times.
# Write the helper entirely below and at the same
# indent level as round_sum().
##
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


##
# Helper function for 'round_sum'
def round10(num):
    if num % 10 >= 5:
        return int(num / 10) * 10 + 10
    else:
        return int(num / 10) * 10


##
# https://codingbat.com/prob/p160533
# Given three ints, a b c, return True if
# one of b or c is "close" (differing from
# a by at most 1), while the other is "far",
# differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of
# a number.
##
def close_far(a, b, c):
    return ((abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2) or
            (abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2))


##
# https://codingbat.com/prob/p190859
# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always
# use big bars before small bars. Return -1 if it can't be done.
##
def make_chocolate(small, big, goal):
    total = small + big * 5

    # Determine if there is enough kilos to complete goal
    if total >= goal:
        # Determine how many big bars can be added the total goal
        big_needed = int(goal / 5)

        # Determine how many big bars will actually be added to total goal
        if big_needed <= big:
            small_needed = goal - big_needed * 5
        else:
            small_needed = goal - big * 5

        # Determine and return the number small bars that will be added to goal
        if small_needed <= small:
            return small_needed
        # Not enough small bars
        else:
            return -1

    # Not enough kilos
    else:
        return -1
