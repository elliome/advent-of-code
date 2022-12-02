const fs = require("fs");
const puzzleData = fs.readFileSync("./input.txt").toString();

const instructions = puzzleData.split("\n").map((string) => ({
    direction: string.split(" ")[0],
    amount: parseInt(string.split(" ")[1]),
}));

// =============== PART 1 ===============

const position = {
    depth: 0,
    horizontal: 0,
};

instructions.forEach((instruction) => {
    switch (instruction.direction) {
        case "up":
            position.depth -= instruction.amount;
            break;
        case "down":
            position.depth += instruction.amount;
            break;
        case "forward":
            position.horizontal += instruction.amount;
            break;
    }
});

console.log(position.depth * position.horizontal);

// =============== PART 2 ===============

const submarine = {
    depth: 0,
    aim: 0,
    position: 0,
};

instructions.forEach((instruction) => {
    switch (instruction.direction) {
        case "up":
            submarine.aim -= instruction.amount;
            break;
        case "down":
            submarine.aim += instruction.amount;
            break;
        case "forward":
            submarine.position += instruction.amount;
            submarine.depth += instruction.amount * submarine.aim;
            break;
    }
});

console.log(submarine.depth * submarine.position);
