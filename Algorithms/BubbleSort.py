def bubbleSort(array):

	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	return array


def test():

	test_cases = [[3, 2, 1], [3, 5, 6, 2, 1, 5], [1, 2, 3]]
	answers = [sorted(array) for array in test_cases]

	for test_case, expected in zip(test_cases, answers):

		actual = bubbleSort(test_case)

		assert actual == expected, f"Wrong Answer.\nExpected: {expected}.\nActual: {actual}"

	print("All test cases passed.")


test()	