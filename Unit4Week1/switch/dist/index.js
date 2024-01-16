"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// import readline promises
const promises_1 = __importDefault(require("readline/promises"));
const pipe = promises_1.default.createInterface({
    input: process.stdin,
    output: process.stdout
});
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const number1 = yield pipe.question("Enter a number: ");
        const number2 = yield pipe.question("Enter another number: ");
        const op = yield pipe.question("Enter an operator (+ - / *): ");
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
    });
}
main();
