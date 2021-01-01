def insertionSort(array):

    for i in range(1, len(array)):
        j = i - 1
        key = array[i]

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key


def test():

	test_cases = [[3, 2, 1], [3, 5, 6, 2, 1, 5], [1, 2, 3]]
	answers = [sorted(array) for array in test_cases]

	for test_case, expected in zip(test_cases, answers):

		insertionSort(test_case)

		assert test_case == expected, f"Wrong Answer.\nExpected: {expected}.\nActual: {actual}"

	print("All test cases passed.")


test()