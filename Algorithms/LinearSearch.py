def linearSearch(array, element):

	for idx, obj in enumerate(array):
		if obj == element:
			return idx
	return -1


def test():
	test_cases = [[3, 2, 1], [3, 5, 6, 2, 1, 5], [1, 2, 3], [3, 6, 1, 4, 8]]
	elements = [2, 5, 3, 9]
	answers = [1, 1, 2, -1]

	for test_case, element, expected in zip(test_cases, elements, answers):

		actual = linearSearch(test_case, element)

		assert actual == expected, f"Wrong Answer.\nExpected: {expected}.\nActual: {actual}"

	print("All test cases passed.")


test()