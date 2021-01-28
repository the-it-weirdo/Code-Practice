const checkArmstrong = (number) => {
	let temp = number;
	const numberOfDigits = number.toString().length;
	let sum = 0;
	while (temp > 0) {
		let remainder = temp % 10;
        sum += remainder ** numberOfDigits;
        temp = parseInt(temp / 10);
	}

	if (sum === number) {
		return true;
	} else {
		return false;
	}
}


let number = 121;
answer = checkArmstrong(number);
console.log(`The number ${number} is armstrong: ${answer}.`);

number = 153;
answer = checkArmstrong(number);
console.log(`The number ${number} is armstrong: ${answer}.`);