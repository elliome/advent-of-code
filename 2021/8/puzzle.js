const fs = require("fs");
let puzzleData = fs.readFileSync("./input.txt").toString().split("\n");

//   0:      1:      2:      3:      4:
//  aaaa    ....    aaaa    aaaa    ....
// b    c  .    c  .    c  .    c  b    c
// b    c  .    c  .    c  .    c  b    c
//  ....    ....    dddd    dddd    dddd
// e    f  .    f  e    .  .    f  .    f
// e    f  .    f  e    .  .    f  .    f
//  gggg    ....    gggg    gggg    ....

//   5:      6:      7:      8:      9:
//  aaaa    aaaa    aaaa    aaaa    aaaa
// b    .  b    .  .    c  b    c  b    c
// b    .  b    .  .    c  b    c  b    c
//  dddd    dddd    ....    dddd    dddd
// .    f  e    f  .    f  e    f  .    f
// .    f  e    f  .    f  e    f  .    f
//  gggg    gggg    ....    gggg    gggg

const numbers = [
    "abcefg", //0
    "cf", //1
    "acdeg", //2
    "acdfg", //3
    "bcdf", //4
    "abdfg", //5
    "abdefg", //6
    "acf", //7
    "abcdefg", //8
    "abcdfg", //9
];

const findMatch = (length) => {
    let matchCount = 0;
    let ret;
    numbers.forEach((str) => {
        if (str.length == length) {
            matchCount++;
            ret = str;
        }
    });

    if (matchCount === 1) {
        return ret;
    }

    return null;
};

let pt1Count = 0;
let pt2Sum = 0;

puzzleData.forEach((str) => {
    const [unique, output] = str.split(" | ");
    const outputArray = output.split(" ");
    outputArray.forEach((num) => {
        if ([2, 3, 4, 7].includes(num.length)) {
            console.log(num);
            pt1Count++;
        }
    });
});
console.log(pt1Count);

puzzleData.forEach((line) => {
    const [unique, output] = line.split(" | ");
    const uniqueArray = unique.split(" ");

    const lookup = {
        a: null,
        b: null,
        c: null,
        d: null,
        e: null,
        f: null,
        g: null,
    };

    const one = uniqueArray.find((str) => str.length === 2);
    const seven = uniqueArray.find((str) => str.length === 3);

    seven.split("").forEach((char) => {
        if (!one.includes(char)) {
            lookup.a = char;
        }
    });

    const count = [0, 0];

    uniqueArray.forEach((str) => {
        one.split("").forEach((char, i) => {
            if (str.includes(char)) {
                count[i]++;
            }
        });
    });

    count.forEach((c, i) => {
        if (c == 9) {
            lookup.f = one.split("")[i];
        } else {
            lookup.c = one.split("")[i];
        }
    });

    const numberCount = {};

    uniqueArray.forEach((str) => {
        str.split("").forEach((char) => {
            numberCount[char] = (numberCount[char] ?? 0) + 1;
        });
    });

    Object.entries(numberCount).forEach(([key, value]) => {
        console.log(value);
        if (value == 4) {
            lookup.e = key;
        }

        if (value == 6) {
            lookup.b = key;
        }
    });

    // TODO FIND D AND G by counting the times A & D appear (6) vs A & G appear (7)

    const findDG = {};

    const alphabet = ["a", "b", "c", "d", "e", "f", "g"];
    let found = [];

    Object.entries(lookup).forEach(([key, value]) => {
        if (value) {
            found.push(value);
        }
    });

    alphabet.forEach((char) => {
        if (!found.includes(char)) {
            findDG[char] = 0;
        }
    });

    let counter = 0;

    uniqueArray.forEach((str) => {
        // console.log();
        if (str.includes(lookup.a)) {
            // console.log(str);
            Object.entries(findDG).forEach(([key, value]) => {
                if (str.includes(key)) {
                    findDG[key]++;
                }
            });
            counter++;
        }
    });

    Object.entries(findDG).forEach(([key, value]) => {
        if (value == 7) {
            lookup.g = key;
        } else {
            lookup.d = key;
        }
    });

    const translateOBJ = {};

    Object.entries(lookup).forEach(([key, value]) => {
        translateOBJ[value] = key;
    });

    let translatedOutput = output.split(" ").map((str) => {
        return numbers.findIndex(
            (num) =>
                num ==
                str
                    .split("")
                    .map((char) => translateOBJ[char])
                    .sort()
                    .reduce((p, c) => p + c, "")
        );
    });

    pt2Sum += parseInt(translatedOutput.reduce((p, c) => p + c, "0"));
});

console.log(pt2Sum);
