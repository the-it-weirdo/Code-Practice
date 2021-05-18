# Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

def twoSum(arr, k):
    seen = set()
    for i in arr:
        if (k - i) in seen: # check compliment in set
            return True
        else:
            seen.add(i) # add this number to set as we are checking complement
    return False # loop ended and not exited, return False



def test():
    testCases = [([1, 3, 8, 2], 10), ([3, 9, 13, 7], 8), ([4, 2, 6, 5 ,2], 4)]
    expecteds = [True, False, True]
    for case, expected in zip(testCases, expecteds):
        actual = twoSum(*case) # same as twoSum(case[0], case[1])
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()
