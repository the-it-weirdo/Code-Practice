// Given a string representing your stones and another string representing a list of jewels,
// return the number of stones that you have that are also jewels.

// Ex: Given the following jewels and stones...

// jewels = "abc", stones = "ac", return 2
// jewels = "Af", stones = "AaaddfFf", return 3
// jewels = "AYOPD", stones = "ayopd", return 0

const jewelsAndStones = (jewels, stones) => {
  const jewelSet = new Set(jewels.split(""));
  let count = 0;
  stones.split("").forEach((element) => {
    if (jewelSet.has(element)) count += 1;
  });
  return count;
};

const test = () => {
  testCases = [
    { jewels: "abc", stones: "ac" },
    { jewels: "Af", stones: "AaaddfFf" },
    { jewels: "AYOPD", stones: "ayopd" },
  ];
  expecteds = [2, 3, 0];

  for (let i = 0; i < testCases.length; i++) {
    const actual = jewelsAndStones(testCases[i].jewels, testCases[i].stones);
    console.log(`For '${testCases[i]}' output obtained '${actual}'`);
    console.assert(
      actual == expecteds[i],
      `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
    );
  }
  console.log("Test completed.");
};

test();
