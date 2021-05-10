// Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical
// characters.
// Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

// Ex: Given the following strings...

// "level", return true
// "algorithm", return false
// "A man, a plan, a canal: Panama.", return true

const palindromeString = (inputStr) => {
  let punctuations = `[!"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~ ]`;
  inputStr = inputStr.toLowerCase();
  let i = 0,
    j = inputStr.length - 1;
  while (i < j) {
    if (punctuations.includes(inputStr[i])) i += 1;
    else if (punctuations.includes(inputStr[j])) j -= 1;
    else if (inputStr[i] !== inputStr[j]) return false;
    else {
      i += 1;
      j -= 1;
    }
  }
  return true;
};

const test = () => {
  testCases = [
    "level",
    "algorithm",
    "A man, a plan, a canal: Panama.",
    "Race Car",
    "",
    "John Snow",
  ];
  expecteds = [true, false, true, true, true, false];

  for (let i = 0; i < testCases.length; i++) {
    const actual = palindromeString(testCases[i]);
    console.log(`For '${testCases[i]}' output obtained '${actual}'`);
    console.assert(
      actual === expecteds[i],
      `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
    );
  }
  console.log("Test completed.");
};

test();
