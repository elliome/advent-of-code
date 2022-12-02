const fs = require("fs");
const puzzleData = fs.readFileSync("./input.txt").toString().split("\n");

// =============== PART 1 ===============

const counts = Array(12).fill(0, 0, 12);

puzzleData.forEach((string) => {
    string.split("").forEach((char, i) => {
        if (char == "1") {
            counts[i]++;
        }
    });
});

let gamma = parseInt(
    counts.reduce((p, c) => `${p}${c > 500 ? 1 : 0}`, ""),
    2
);
let epsilon = parseInt(
    counts.reduce((p, c) => `${p}${c < 500 ? 1 : 0}`, ""),
    2
);

console.log(gamma * epsilon);

// =============== PART 2 ===============

const bits = ["0", "1"];
let readings = [];

bits.forEach((bit) => {
    let ones = [];
    let zeros = [];
    let interator = 0;

    let data = puzzleData;

    while (data.length > 1) {
        ones = [];
        zeros = [];

        data.forEach((string) => {
            if (string.substring(interator, interator + 1) == "1") {
                ones.push(string);
            } else {
                zeros.push(string);
            }
        });

        if (bit == "1") {
            if (zeros.length > ones.length) {
                data = zeros;
            } else {
                data = ones;
            }
        } else {
            if (zeros.length <= ones.length) {
                data = zeros;
            } else {
                data = ones;
            }
        }

        interator++;
    }
    readings.push(parseInt(data[0], 2));
});

console.log(
    readings,
    readings.reduce((p, c) => p * c, 1)
);
