/*
* **** Question ****
* Given an array, find the sum of k elements such that it is maximum.
*
* E.g.: array = [80, -50, 90, 100] and k = 2
* 	answer = 190 (sum of 90 and 100).
*
* ********
*/

/*
**** Approach ****

* We take a Sliding window approach. At first, we find the sum of the first window i.e. the first k elements. 
* Then, we assign a variable 'max_sum' equal to window sum.
* Then for each remaining element, we add it to the window sum while simaltaneously subtracting the kth previous
* element to maintain the window length. We compare the new window sum with the 'max_sum' and update accordingly.

********
*/

const max_k_sum = (array, k) => {
	let window_sum = 0;
	let max_sum = 0;

	for (let i = 0; i < k; i++) {
		window_sum+=array[i];
	}
		
	max_sum = window_sum;

	for(let i = k; i < array.length; i++) {
		// Add the next element in the window and subtract the previous kth element to maintain the window length.
		window_sum = window_sum + array[i] - array[i-k];
		max_sum = Math.max(max_sum, window_sum);
	}

	return max_sum;
};

/*
* **** Complexities ****

* Time Complexity: O(n)
* Space Complexity: O(1)

* ********
*/


const assert = require('assert');
const test = () => {
	test_cases = [
		[80, -50, 90, 100], 
		[40, 50, 10, 90, 100], 
		[-1, 1, -1, 1, -1, 1]
	];
	ks = [2, 3, 3];
	answers = [190, 200, 1];

	for (let i = 0; i < test_cases.length; i++) {
		let array = test_cases[i];
		let k = ks[i];
		let expected = answers[i];
		let actual = max_k_sum(array, k);
		assert(expected == actual, "Wrong answer. Expected: ${expected}. Actual: ${actual}");
	}

	console.log("All test cases passed.");
};


test();