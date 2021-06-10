# Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

# Ex: Given the following arrays...

# nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
# nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
# nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []


def intersectionOfArray(arr1, arr2):
    return list(set(arr1) & set(arr2))


def test():
    testCases = [([2, 4, 4, 2],[2, 4]), ([1, 2, 3, 3],[3, 3]), ([2, 4, 6, 8],[1, 3, 5, 7])]
    expecteds = [[2, 4], [3], []]
    for case, expected in zip(testCases, expecteds):
        actual = intersectionOfArray(*case) # same as jewelsAndStones(case[0], case[1])
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()