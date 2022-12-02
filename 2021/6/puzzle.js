const fs = require("fs");
let puzzleData = fs
    .readFileSync("./input.txt")
    .toString()
    .split(",")
    .map((string) => parseInt(string));

let fishes = new Array(9).fill(0);

puzzleData.forEach((num) => {
    fishes[num] += 1;
});

for (let i = 0; i < 256; i++) {
    let newFish = new Array(9).fill(0);

    fishes.forEach((fish, i) => {
        if (i == 0) {
            newFish[6] = fish;
            newFish[8] = fish;
            return;
        }

        newFish[i - 1] += fish;
    });

    fishes = newFish;
}
console.log(fishes.reduce((p, c) => p + c, 0));
