"use strict";
let i = 1;
function isPrime(n) {
    // check if n is a prime number
    let isPrime = true;
    for (let j = 2; j < n; j++) {
        if (n % j === 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

do {
    // check if i is a prime number
    if (isPrime(i)) {
        console.log(`${i} is a prime number`);
    }
    // add 1 to a prime number
    i++;
} while (i < 20);
