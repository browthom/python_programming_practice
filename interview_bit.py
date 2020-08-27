# Coding Questions from InterviewBit website
from math import floor


def get_starting_gas_station(a, b):
    # a -> amount of gas at gas station a[i]
    # b -> b[i] is the amount of gas to get from i to i+1

    gas_in_tank = 0

    # Continually iterate through possible starting indices
    for i in range(len(a)):
        # j is the starting index
        j = i
        # Initial fill up
        gas_in_tank = a[i]

        # Continue on path until you aren't able to make
        # it to the next gas station
        while gas_in_tank >= b[j]:
            # Burn gas traveling to a[j+1]
            gas_in_tank -= b[j]

            # Increment j accordingly
            # Cycle around to index=0 if need be
            if j < len(a)-1:
                j += 1
            else:
                j = 0

            # Fill up gas at a[j+1] gas station
            gas_in_tank += a[j]

            # If we have made it to starting point
            # return index
            if j == i:
                return j

    # No possible path found
    return -1


##
# An intuitive way to find the majority
# element is to first sort the numbers in the
# array in ascending order. That way we can
# easily count the number of successive
# integers that are identical to each other in the array
##
def find_majority_element(array):
    array.sort()
    count = 1
    prev = array[0]

    for i in range(1, len(array)):
        # count successive elements that are equal
        if prev == array[i]:
            count += 1
        # if the previous element doesn't equal the current element
        # then reset count as that element was not the majority element
        else:
            count = 1

        # If we have found the majority element, return element
        if count > floor(len(array)/2):
            print(count)
            return array[i]

        # rewrite 'prev' for next go-around
        prev = array[i]

    # No majority element in array
    return -1
