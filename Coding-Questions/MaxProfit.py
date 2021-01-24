# #### Question ####
# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.

# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in the future
# to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Example:
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and
# sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1
# is not allowed because you must buy before you sell.

# ########


def maxProfit(prices):

	minPrice = prices[0]
	maxProft = 0

	for i in range(1, len(prices)):
		if prices[i] < minPrice:
			minPrice = prices[i]
		elif prices[i] - minPrice > maxProft:
			maxProft = prices[i] - minPrice

	return maxProft


def test():
	testCases = [[7, 1, 5, 3, 6, 4], [6, 5, 3, 2, 1], [9], [1, 5, 2, 7, 3, 8, 9]]
	answers = [5, 0, 0, 8]

	for testCase, expected in zip(testCases, answers):
		actual = maxProfit(testCase)

		assert expected == actual, f"Wrong answer.\
									\nExpected: {expected}.\
									\nActual: {actual}"

	print("All test cases passed.")

test()