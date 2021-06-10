// Given two integer arrays, return their intersection.
// Note: the intersection is the set of elements that are common to both arrays.

// Ex: Given the following arrays...

// nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
// nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
// nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []


const intersectionOfArray = (arr1, arr2) => {
    const setB = new Set(arr2);
    return [...new Set((arr1.filter(x => setB.has(x))))];
};


const test = () => {
    testCases = [
      { arr1: [2, 4, 4, 2], arr2: [2, 4] },
      { arr1: [1, 2, 3, 3], arr2: [3, 3] },
      { arr1: [2, 4, 6, 8], arr2: [1, 3, 5, 7] }
    ];
    expecteds = [[2, 4], [3], []];
  
    for (let i = 0; i < testCases.length; i++) {
      const actual = intersectionOfArray(testCases[i].arr1, testCases[i].arr2);
      console.log(`For '${testCases[i]}' output obtained '${actual}'`);
      console.assert(
        actual === expecteds[i],
        `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
      );
    }
    console.log("Test completed.");
  };
  
  test();
  