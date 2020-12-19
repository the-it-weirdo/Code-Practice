# #### Question ####
# An alternate sort of a list contains alternarte elements(starting from the first position) after sorting in ascending order.
# Given, a list of unsorted elements, write an algorithm to find the alternate sort of the given list.

# E.g.:
# Input: [3, 5, 1, 5, 9, 10, 2, 6]
# Output: [1, 3, 5, 9]

# ########

def solve(array):
	array = sorted(array)
	answer = []
	for i in range(0, len(array), 2):
		answer.append(array[i])

	return answer


def test():
	test_cases = [[3, 5, 1, 5, 9, 10, 2, 6], [4, 7, 1, 2, 5, 9, 10, 34, 5, 6, 3]]
	answers = [[1, 3, 5, 9], [1, 3, 5, 6, 9, 34]]

	for case, expected in zip(test_cases, answers):
		actual = solve(case)
		assert actual == expected, f"Wrong answer.\nExpected: {expected}.\nActual: {actual}"

	print("All test cases passed.")


test()