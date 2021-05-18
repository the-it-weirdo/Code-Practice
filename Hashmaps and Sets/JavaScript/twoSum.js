// Given an array of integers, return whether or not two numbers sum to a given target, k.
// Note: you may not sum a number with itself.

// Ex: Given the following...

// [1, 3, 8, 2], k = 10, return true (8 + 2)
// [3, 9, 13, 7], k = 8, return false
// [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

const twoSum = (arr, k) => {
  let seen = new Set();
  for (let i = 0; i <= arr.length; i++) {
    if (seen.has(k - arr[i])) return true;
    else seen.add(arr[i]);
  }
  return false;
};



const test = () => {
  testCases = [
    { arr: [1, 3, 8, 2], k: 10 },
    { arr: [3, 9, 13, 7], k: 8 },
    { arr: [4, 2, 6, 5, 2], k: 4 },
  ];
  expecteds = [true, false, true];

  for (let i = 0; i < testCases.length; i++) {
    const actual = twoSum(testCases[i].arr, testCases[i].k);
    console.log(`For '${testCases[i]}' output obtained '${actual}'`);
    console.assert(
      actual == expecteds[i],
      `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
    );
  }
  console.log("Test completed.");
};

test();
