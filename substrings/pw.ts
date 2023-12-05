import readline from "readline/promises";

const rl = readline.createInterface(process.stdin, process.stdout);

const numReg = new RegExp("[0-9]");

function containsNum(phrase: string) {
  return numReg.test(phrase);
}

async function main() {
  let isValid = false;

  while (!isValid) {
    const pw = await rl.question("Please enter a password: ");

    if (!pw || pw.length < 8) {
      console.log("Your password's length must be at least 8 characters.");
      continue;
    } else if (!containsNum(pw)) {
      console.log("Your password must include at least one number.");
      continue;
    }

    isValid = true;

    console.log("This password is valid.");
    rl.close();

    process.exit(1);
  }

}

main();