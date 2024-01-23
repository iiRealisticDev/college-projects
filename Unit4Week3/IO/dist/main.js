"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
if (!fs_1.default.existsSync("test.txt")) {
    fs_1.default.writeFileSync("test.txt", "");
}
// 2d array
const grades = [
    ["Student", "Grade"],
    ["Ali", "A*"],
    ["Javad", "A"],
];
// format the array so that it looks like a table
// make it so that the text will appear as
/**
 * Student  Grade
 * Ali      A*
 * Javad    A
 */
// in both the file and the console
// \t in .txt files will be 2 spaces and will not properly align the text
// \t in the console will be 4 spaces and will properly align the text
// \t\t will be 8 spaces in the file and 4 spaces in the console
// so we will use \t\t to align the text in the file and \t to align the text in the console
// write the file
fs_1.default.writeFileSync("test.txt", grades.map((row) => row.join("\t\t")).join("\n"));
// read the file
const fileContent = fs_1.default.readFileSync("test.txt", "utf-8");
// print the file
console.log(fileContent);
