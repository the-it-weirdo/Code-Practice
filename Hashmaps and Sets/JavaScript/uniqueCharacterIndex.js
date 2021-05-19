// Given a string, return the index of its first unique character.
// If a unique character does not exist, return -1.

// Ex: Given the following strings...

// "abcabd", return 2
// "thedailybyte", return 1
// "developer", return 0

const charCount = (ch, inputstr) => {
  //   return [...inputstr].reduce((acc, c) => (c === ch ? ++acc : acc), 0);
  return inputstr.split(ch).length - 1;
};

const uniqueCharIndex = (inputstr) => {
  const charMap = {};
  for (let index in inputstr) {
    let key = charCount(inputstr[index], inputstr);
    charMap[key] = Math.min(
      isFinite(charMap[key]) ? charMap[key] : index,
      index
    );
  }
  return isFinite(charMap["1"]) ? charMap["1"] : -1;
};

const test = () => {
  testCases = ["abcabd", "thedailybyte", "developer", "aa"];
  expecteds = [2, 1, 0, -1];

  for (let i = 0; i < testCases.length; i++) {
    const actual = uniqueCharIndex(testCases[i]);
    console.log(`For '${testCases[i]}' output obtained '${actual}'`);
    console.assert(
      actual == expecteds[i],
      `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
    );
  }
  console.log("Test completed.");
};

test();
