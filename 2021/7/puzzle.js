const fs = require("fs");
let puzzleData = fs
    .readFileSync("./input.txt")
    .toString()
    .split(",")
    .map((string) => parseInt(string));

let options = Array(puzzleData.reduce((p, c) => (c > p ? c : p))).fill(0);

options = options.map((option, index) => {
    console.log(Math.round((index / options.length) * 100));
    let totalFuel = 0;

    puzzleData.forEach((num) => {
        let dist = index - num;
        if (dist < 0) {
            dist = dist * -1;
        }

        let counter = 0;
        for (let i = 0; i <= dist; i++) {
            counter += i;
        }

        totalFuel += counter;
    });

    return totalFuel;
});

console.log(options);
console.log(`Answer: ${options.reduce((p, c) => (c < p ? c : p))}`);
