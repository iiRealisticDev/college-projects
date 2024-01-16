import readline from "readline/promises";

const pin = "1234";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function main() {
  let tries = 0;

  do {
    const input = await rl.question("Enter your PIN: ");
    tries++;

    if (input === pin) {
      console.log("PIN ACCEPTED");
      break;
    } else {
      console.log("PIN FAILED");
    }
  } while (tries < 4);

  if (tries >= 3) {
    console.log("Card blocked");
  }
  
  rl.close();
}

main();