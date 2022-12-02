const fs = require("fs");
const puzzleData = fs.readFileSync("./input.txt").toString();
const depths = puzzleData.split("\n").map((string) => parseInt(string));

// =============== PART 1 ===============

let previous = Infinity;
let increaseCount = 0;

depths.forEach((depth) => {
    if (depth > previous) {
        increaseCount++;
    }

    previous = depth;
});

console.log(`increase count: ${increaseCount}`);

// =============== PART 2 ===============

let previousGroup = Infinity;
let increaseCountGroup = 0;
let group = [];

depths.forEach((depth, i) => {
    let groupTotal = 0;
    group.unshift(depth);

    if (group.length > 3) {
        group.pop();
        groupTotal = group.reduce((p, c) => {
            return p + c;
        });
    }

    if (group.length > 0) {
        if (groupTotal > previousGroup) {
            increaseCountGroup++;
        }
    }

    previousGroup = groupTotal;
});
console.log(increaseCountGroup);
