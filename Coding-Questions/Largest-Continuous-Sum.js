/* **** Question ****
* Given an array of integers(positive and negative), find the largest continuous sum.
* 
* e.g. : given [1, 2, -1, 3, 4, -1], largest continuous sum = (1 + 2 + (-1) + 3 + 4) = 9
*
* ********

* **** Approach ****
* We iterate over the array once storing and updating the maximum sum obtained.

* Let us initialize 1 variables 'max_sum' and 'current_sum' with the first element of the array.
*
* We iterate the array from index 1 (if available). For each element in the array from index 1, we add it to 'current_sum'
* and compare the 'current_sum' with the recently visited element to find maximum. 
* Then we campare the 'max_sum' and the 'current_sum' to find the maximum among these 2.
*
* Return 'max_sum' at the end of the loop
*
*/

const longest_continuous_sum = (array) => {
	let curr_sum = array[0];
	let max_sum = array[0];

	for(let i = 1; i < array.length; i++) {

		curr_sum = Math.max(curr_sum + array[i], array[i]);

		max_sum = Math.max(curr_sum, max_sum);
	}

	return max_sum;
}

/* **** Complexities ****
*
* Time Complexity: O(n)
* Space Complexity: O(1)
*
* ********
*/



const assert = require('assert');
const test = () => {
	test_cases = [
		[1, 2, -1, 3, 4, -1],
		[1,2,-1, 3, 4, 10, 10, -10, -1],
		[-1, -1, 4, 3, -1, -1]
	];
	answers = [9, 29, 7];

	for (let i = 0; i < test_cases.length; i++) {
		let expected = answers[i];
		let actual = longest_continuous_sum(test_cases[i]);
		assert(expected == actual, "Wrong answer. Expected: ${expected}. Actual: ${actual}");
	}
	console.log("All test cases passed");

}


test();