// Given a string, reverse all of its characters and return the resulting string.

// Ex: Given the following strings...

// “Cat”, return “taC”
// “The Daily Byte”, return "etyB yliaD ehT”
// “civic”, return “civic”

const reverseString = (inputStr) => {
    stack = [];
    for (let i = 0; i < inputStr.length; i++) {
        stack.push(inputStr[i]);
    }

    let returnString = "";

    while (stack.length > 0) {
        returnString += stack.pop();
    }

    return returnString;
}


const test = () => {
    testCases = ["Cat", "The Daily Byte", "civic"];
    expecteds = ["taC", "etyB yliaD ehT", "civic"];

    for (let i = 0; i < testCases.length; i++) {
        const actual = reverseString(testCases[i]);
        console.log(`For '${testCases[i]}' output obtained '${actual}'`);
        console.assert(actual == expecteds[i], `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`);
    }
    console.log("Test completed.");
}

test();