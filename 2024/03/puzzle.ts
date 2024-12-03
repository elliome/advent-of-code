import * as fs from 'fs';
const puzzleData = fs.readFileSync("./input.txt").toString();
const time = performance.now();

const MUL_MATCH_STRING = "mul(";
const DO_MATCH_STRING = "do()";
const DONT_MATCH_STRING = "don't()";
const MATCH_STRINGS = [MUL_MATCH_STRING, DO_MATCH_STRING, DONT_MATCH_STRING];
let isDo = true;
let currentString = "";
let inputNumbers = "";
let totalPartOne = 0;
let totalPartTwo = 0;

function mul(a: number, b: number) {
  return a * b;
}

for (let i = 0; i < puzzleData.length; i += 1) {
  if (puzzleData[i] === ")" && currentString === MUL_MATCH_STRING && inputNumbers.length > 2) {
    const numbers = inputNumbers.split(",").map(Number);

    if (numbers.length === 2 ){
      totalPartOne += mul(numbers[0], numbers[1]);
      if (isDo) {
        totalPartTwo += mul(numbers[0], numbers[1]);
      }
    }

    inputNumbers = "";
    currentString = "";
    continue;
  }

  if (currentString === MUL_MATCH_STRING) {
    if (!isNaN(parseInt(puzzleData[i])) || puzzleData[i] === ",") {
      inputNumbers += puzzleData[i];
    } else {
      inputNumbers = "";
      currentString = "";
    }
    continue;
  }

  if (currentString === DO_MATCH_STRING) {
    isDo = true;
    currentString = "";
  }

  if (currentString === DONT_MATCH_STRING) {
    isDo = false;
    currentString = "";
  }

  currentString += puzzleData[i];

  let isInMatchStrings = false;

  MATCH_STRINGS.forEach((matchString) => {
    if (matchString.substring(0, currentString.length) === currentString) {
      isInMatchStrings = true;
    }
  });

  if (!isInMatchStrings) {
    currentString = "";
  }

}

console.log(`[PART 1] ${totalPartOne}`);
console.log(`[PART 2] ${totalPartTwo}`);
console.log(`Completed in ${(performance.now() - time).toFixed(2)}ms`)