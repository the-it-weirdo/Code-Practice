// Given a string representing the sequence of moves a robot vacuum makes,
// return whether or not it will return to its original position.
// The string will only contain L, R, U, and D characters, representing left,
// right, up, and down respectively.

// Ex: Given the following strings...

// "LR", return true
// "URURD", return false
// "RUULLDRD", return true

const vaccumCleanerPath = (inputPath) => {
    let position = 0;
    for (let i = 0; i < inputPath.length; i++) {
        if (inputPath[i] === "L" || inputPath[i] === "l") position += 1;
        else if (inputPath[i] === "R" || inputPath[i] === "r") position -= 1;
        else if (inputPath[i] === "D" || inputPath[i] === "d") position += 2;
        else if (inputPath[i] === "U" || inputPath[i] === "u") position -= 2;
        else throw `Illegal Character ${inputPath[i]}`;
    }
    return position === 0 ? true : false;
};

const vaccumCleanerPathUsingStack = (inputPath) => {
    horizontalStack = [];
    verticalStack = [];
    for (let i = 0; i < inputPath.length; i++) {
        if (inputPath[i] === "L" || inputPath[i] === "l") {
            if (horizontalStack.length === 0) horizontalStack.push(inputPath[i]);
            else horizontalStack.pop();
        } else if (inputPath[i] === "R" || inputPath[i] === "r") {
            if (horizontalStack.length === 0) horizontalStack.push(inputPath[i]);
            else horizontalStack.pop();
        } else if (inputPath[i] === "D" || inputPath[i] === "d") {
            if (verticalStack.length === 0) verticalStack.push(inputPath[i]);
            else verticalStack.pop();
        } else if (inputPath[i] === "U" || inputPath[i] === "u") {
            if (verticalStack.length === 0) verticalStack.push(inputPath[i]);
            else verticalStack.pop();
        } else throw `Illegal Character ${inputPath[i]}`;
    }
    return horizontalStack.length === 0 && verticalStack.length === 0 ?
        true :
        false;
};

const test = () => {
    testCases = ["LR", "URURD", "RUULLDRD"];
    expecteds = [true, false, true];

    for (let i = 0; i < testCases.length; i++) {
        const actual = vaccumCleanerPath(testCases[i]);
        console.log(`For '${testCases[i]}' output obtained '${actual}'`);
        console.assert(
            actual === expecteds[i],
            `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
        );
    }
    console.log("Test completed for vaccumCleanerPath.");

    for (let i = 0; i < testCases.length; i++) {
        const actual = vaccumCleanerPathUsingStack(testCases[i]);
        console.log(`For '${testCases[i]}' output obtained '${actual}'`);
        console.assert(
            actual === expecteds[i],
            `Wrong answer. Expected: '${expecteds[i]}'. Found: '${actual}'`
        );
    }
    console.log("Test completed for vaccumCleanerPathUsingStack.");
};

test();