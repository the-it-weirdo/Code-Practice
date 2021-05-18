// Given two strings s and t return whether or not s is an anagram of t.
// Note: An anagram is a word formed by reordering the letters of another word.

// Ex: Given the following strings...

// s = "cat", t = "tac", return true
// s = "listen", t = "silent", return true
// s = "program", t = "function", return false

const validAnagram = (s, t) => {
  let charMapS = {};
  s.split("").forEach((element) => {
    charMapS[element] = charMapS[element] ? charMapS[element] + 1 : 1;
  });
  let charMapT = {};
  t.split("").forEach((element) => {
    charMapT[element] = charMapT[element] ? charMapT[element] + 1 : 1;
  });
  return Object.entries(charMapS).sort().toString() === Object.entries(charMapT).sort().toString();
};


const test = () => {
    testCases = [
      { s: "cat", t: "tac" },
      { s: "silent", t: "listen" },
      { s: "program", t: "function" },
    ];
    expecteds = [true, true, false];
  
    for (let i = 0; i < testCases.length; i++) {
      const actual = validAnagram(testCases[i].s, testCases[i].t);
      console.log(`For '${testCases[i]}' output obtained '${actual}'`);
      console.assert(
        actual == expecteds[i],
        `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
      );
    }
    console.log("Test completed.");
  };
  
  test();
  