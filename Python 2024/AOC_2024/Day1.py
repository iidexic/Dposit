# Advent of Code Day 1
#* - General Notes -
# Location ID (unique) - I believe there are 50 locations
#* INPUT:
# Two lists of numbers side by side:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# TODO: PART 1: Pair up smallest number in left list with smallest number in right list, and so on.
# TODO: Within each pair, determine how far apart numbers are. Finally, sum these distances
# TODO: PART 2: Calculate similarity score : Sum of full list 1*frequency list2

# Imports
import numpy as np
from read_input import load_input

input_file = 'input.txt'


def d1p1_sum_difference(input: np.array) -> int:
    """Advent of Code: Day 1 Part 1. sorts 2 arrays low to high, then calculates absolute difference of each index

    Args:
        input (np.array): numpy array, containing 2 lists (arrays?) of numbers to compare

    Returns:
        int: summed absolute difference between numbers in input[0] and input[1] after sorting low to high
    """
#    a_low2hi = np.sort(input)
#    a_diff = np.abs(np.subtract(a_low2hi[0],a_low2hi[1]))
#    return a_low2hi, np.sum(a_diff)
    pass

def d1p2_similarity_score(input: np.array) -> int:
    #Notes/Thinking:
    #! Biggest issue will be lack of understanding of efficiency with specific numpy operations
    # I know that I learned some shit like this in the past that was super fast. I feel like it was something with ndarray
    # Our arrays are already sorted so for any given number we just need a start and end index
    # I swear there has to be some shit with knowing the difference.
    # > If our subtract is(?)
    # oh fuck brain blast: using the difference, we can just shift shit around.
    # if diff neg:[0]<[1], pos:[0]>[1], 0:equal. BUT we don't know the start point
    # on shift, + to -:none and vice versa, - to 0=start, 0 to +=end. or the other way, whatever.
    # we can start with this? I feel like knowing distances between each value in array will let us immediately eliminate shit.
    distinct0 = np.unique(input[0])
    diff = np.diff(input) # array where each diff[n] = [n+1] - [n]. len is (orig len - 1)
    print(diff)
    return distinct0

# Get our original format raw data in np array
arr_id = np.column_stack(load_input(input_file,load_type='day1'))
#* Day 1 Part 1
arr_sorted = np.sort(arr_id)
arr_subtr = np.subtract(arr_sorted[0],arr_sorted[1])
sumdist = np.sum(np.abs(arr_subtr)) #* day 1 part 1 answer

#* Day 1 Part 2
freqscore = d1p2_similarity_score(arr_id)


print(len(arr_id[0]))
print("----")
print(5%30)
print("----")
print(len(freqscore))
