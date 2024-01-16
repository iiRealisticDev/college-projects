// import readline/promises (async way of reading stdin)
import readline from "readline/promises";

// create an interface to read from stdin
// stdin is the standard input (keyboard)
// stdout is the standard output (console)
const pipe = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// to use async-await we need to create a function
// and call it
async function main() {
  const number1 = await pipe.question("Enter a number: ");
  const number2 = await pipe.question("Enter another number: ");
  const op = await pipe.question("Enter an operator (+ - / *): ");

  pipe.close();

  // convert string to number
  const num1 = Number(number1);
  const num2 = Number(number2);

  // switch statement
  switch (op) {
    case "+":
      console.log(num1 + num2);
      break;
    case "-":
      console.log(num1 - num2);
      break;
    case "*":
      console.log(num1 * num2);
      break;
    case "/":
      console.log(num1 / num2);
      break;
    default:
      console.log("Invalid operator");
      break;
  }
}

main();