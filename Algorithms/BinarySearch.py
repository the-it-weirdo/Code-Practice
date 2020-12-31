def binarySearch(array, element, minimum, maximum):

	if maximum >= minimum:
		mid = minimum + ((maximum - minimum) // 2)

		if array[mid] == element:
			return mid
		elif array[mid] > element:
			return binarySearch(array, element, minimum, mid-1)
		else:
			return binarySearch(array, element, mid+1, maximum)
	else:
		return -1


def iterativeBinarySearch(array, element):

	minimum = 0
	maximum = len(array) -1

	while minimum <= maximum:
		mid = minimum + ((maximum - minimum) // 2)

		if array[mid] == element:
			return mid
		elif array[mid] > element:
			maximum = mid-1
		else:
			minimum = mid+1

	return -1


def test():

	array = [i for i in range(100)]

	elements = [8, 9, 89, 0, 1]
	expecteds = [8, 9, 89, 0, 1]

	for element, expected in zip(elements, expecteds):
		actual = binarySearch(array, element, 0, len(array)-1)
		iterativeActual = iterativeBinarySearch(array, element)

		assert expected == actual, f"Wrong answer.\nExpected: {expected}\nActual: {actual}"
		assert expected == iterativeActual, f"Wrong answer.\nExpected: {expected}\nActual: {iterativeActual}"

	print("All test cases passed.")

test()