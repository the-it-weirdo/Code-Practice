// Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
// Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

// Ex: Given the following strings...

// "abcba", return true
// "foobof", return true (remove the first 'o', the second 'o', or 'b')
// "abccab", return false

const isValidPalindrome = (inputstr) => {
  return inputstr === inputstr.split("").reverse().join("");
};

const isValidPalindromeWithRemoval = (inputstr) => {
    for(let i = 0; i < inputstr.length; i++) {
        const first = inputstr.split("").splice(0, i).join("");
        const second = inputstr.split("").splice(i+1).join("");
        if (isValidPalindrome(first+second)) return true;
    }
    return false;
};

const test = () => {
    testCases = ["abcba", "foobof", "abccab", "poope", "teye", "oolaaaaloo", "abba", "aba"];
    expecteds = [true, true, false, true, true, true, true, true];

    for (let i = 0; i < testCases.length; i++) {
        const actual = isValidPalindromeWithRemoval(testCases[i]);
        console.log(`For '${testCases[i]}' output obtained '${actual}'`);
        console.assert(actual == expecteds[i], `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`);
    }
    console.log("Test completed.");
}

test();