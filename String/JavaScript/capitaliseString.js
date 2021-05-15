// Given a string, return whether or not it uses capitalization correctly.
// A string correctly uses capitalization if all letters are capitalized,
// no letters are capitalized, or only the first letter is capitalized.

// Ex: Given the following strings...

// "USA", return true
// "Calvin", return true
// "compUter", return false
// "coding", return true

const capitaliseString = (inputstr) => {
  let allCaps = false,
    noneCap = false,
    firstCap = true;

  for (let i = 0; i < inputstr.length; i++) {
    if (i === 0 && !inputstr[i].toUpperCase() === inputstr[i]) {
      firstCap = false;
      noneCap = true;
    }
    if (i === 1 && inputstr[i].toUpperCase() === inputstr[i]) allCaps = true;
    if (allCaps && inputstr[i].toLowerCase() === inputstr[i]) return false;
    if (noneCap && inputstr[i].toUpperCase() === inputstr[i]) return false;
    if (!i == 0 && !allCaps && inputstr[i].toUpperCase() === inputstr[i])
      return false;
  }
  return true;
};

const test = () => {
  testCases = [
    "USA",
    "Calvin",
    "compUter",
    "coding",
    "CCd",
    "CdC",
    "CCdE",
    "eeC",
    "eCe",
    "eeCe",
  ];
  expecteds = [true, true, false, true, false, false, false, false, false, false];

  for (let i = 0; i < testCases.length; i++) {
    const actual = capitaliseString(testCases[i]);
    console.log(`For '${testCases[i]}' output obtained '${actual}'`);
    console.assert(
      actual === expecteds[i],
      `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
    );
  }
  console.log("Test completed.");
};

test();
