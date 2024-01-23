import fs from "fs"; // import fs module

// if file does not exist, create it
if (!fs.existsSync("test.txt")) {
  fs.writeFileSync("test.txt", "");
}

// 2d array
const grades = [
  ["Student", "Grade"],
  ["Ali", "A*"],
  ["Javad", "A"],
];

// space between columns
fs.writeFileSync("test.txt", grades.map((row) => row.join("\t\t")).join("\n"));

// read the file
const fileContent = fs.readFileSync("test.txt", "utf-8");

// print the file
console.log(fileContent);