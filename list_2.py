##
# https://codingbat.com/prob/p189616
# Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder,
# e.g. 5 % 2 is 1.
##
def count_evens(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1

    return count


##
# https://codingbat.com/prob/p184853
# Given an array length 1 or more of ints, return the
# difference between the largest and smallest values
# in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger
# of two values.
##
def big_diff(nums):
    smallest = nums[0]
    largest = nums[0]

    for i in range(len(nums) - 1):
        smallest = min(smallest, nums[i + 1])
        largest = max(largest, nums[i + 1])

    return largest - smallest


##
# https://codingbat.com/prob/p126968
# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in
# the array. If there are multiple copies of the smallest
# value, ignore just one copy, and likewise for the
# largest value. Use int division to produce the final
# average. You may assume that the array is length 3 or more.
##
def centered_average(nums):
    # Initial setting of largest and smallest values
    smallest = nums[0]
    largest = nums[0]

    total_sum = nums[0]

    # Iterate through to sum all values in list
    # Also keep track of the smallest and largest integers
    for i in range(len(nums) - 1):
        smallest = min(smallest, nums[i + 1])
        largest = max(largest, nums[i + 1])
        total_sum += nums[i + 1]

    # Remove smallest and largest ints before returning
    # the average of remaining integers
    total_sum -= (smallest + largest)

    return int(total_sum / (len(nums) - 2))


##
# https://codingbat.com/prob/p167025
# Return the sum of the numbers in the array, returning
# 0 for an empty array. Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately
# after a 13 also do not count.
##
def sum13(nums):
    total_sum = 0
    i = 0

    while i < len(nums):
        if nums[i] != 13:
            total_sum += nums[i]
            i += 1
        else:
            i += 2

    return total_sum


##
# https://codingbat.com/prob/p108886
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting
# with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7).
# Return 0 for no numbers.
##
def sum67(nums):
    seq_67 = False

    total_sum = 0

    for i in range(len(nums)):

        # If not a 6 and not currently in skip zone
        if nums[i] != 6 and not seq_67:
            total_sum += nums[i]
        # If a 6 appears then start skip zone
        elif nums[i] == 6 and not seq_67:
            seq_67 = True
        # If 7 found and in skip zone, then end skip zone
        elif nums[i] == 7 and seq_67:
            seq_67 = False

    return total_sum


##
# https://codingbat.com/prob/p119308
# Given an array of ints, return True if the array
# contains a 2 next to a 2 somewhere.
##
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False
