import { readFileSync } from 'fs';

const input = readFileSync('input.txt', 'utf8').split('\n');
const elfs: number[] = []
let elfCounter = 0;
let currentBiggestElf = 0;
let tempElf = 0;

input.forEach((line) => {
    if(line === ''){
        elfs[elfCounter] = tempElf;
        if (tempElf > currentBiggestElf) {
            currentBiggestElf = tempElf;
        }

        elfCounter++;
        tempElf = 0;
    }else{
        tempElf += parseInt(line);
  }

});

console.log(currentBiggestElf, elfs.sort((a, b) => b - a).slice(0, 3).reduce((a, b) => a + b, 0));