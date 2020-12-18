/* 
**** Question ****
An alternate sort of a list contains alternarte elements(starting from the first position) after sorting in ascending order.
Given, a list of unsorted elements, write an algorithm to find the alternate sort of the given list.

E.g.:
Input: [3, 5, 1, 5, 9, 10, 2, 6]
Output: [1, 3, 5, 9]

P.S.: You don't need to return anything. Just log on the standard output.
********
*/

import java.util.Arrays;

class AlternateSort {

	public static void main(String[] args) {
		int[][] test_cases = new int[][] {
			new int[] {3, 5, 1, 5, 9, 10, 2, 6},
			new int[] { 4, 7, 1, 2, 5, 9, 10, 34, 5, 6, 3}
		};

		int[][] answers = new int[][] {
			new int[] {1, 3, 5, 9},
			new int[] {1, 3, 5, 6, 9, 34}
		};
		
		for(int i = 0; i < test_cases.length; i++) {
			System.out.println("Given input: ");	
			printArray(test_cases[i]);
			System.out.println("Expected Output: ");
			printArray(answers[i]);
			System.out.println("Actual output: ");
			alternateSort(test_cases[i]);
		}
		
	}

	static void alternateSort(int[] array) {

		Arrays.sort(array);

		for (int i = 0; i < array.length; i+=2) {
			System.out.print(array[i] + "\t");
		}

		System.out.println();
	}

	static void printArray(int[] array) {
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + "\t");
		}
		System.out.println();
	}
}