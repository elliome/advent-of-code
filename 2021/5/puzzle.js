const fs = require("fs");
let puzzleData = fs.readFileSync("./input.txt").toString().split("\n");

puzzleData = puzzleData.map((line) => {
    const xy = line.split(" -> ");
    const points = [];

    xy.forEach((point) => {
        const vector = point.split(",");
        points.push({
            x: parseInt(vector[0]),
            y: parseInt(vector[1]),
        });
    });

    return points;
});

const grid = [];

for (let i = 0; i < 1000; i++) {
    let temp = [];

    for (let j = 0; j < 1000; j++) {
        temp.push(0);
    }

    grid.push(temp);
}

puzzleData.forEach((line) => {
    const [start, end] = line;

    // ============ pt 2, diagonal lines ============

    if (start.x != end.x && start.y != end.y) {
        let positionX = start.x;
        let positionY = start.y;

        console.log(`${start.x},${start.y} -> ${end.x},${end.y}`);

        while (positionX != end.x && positionY != end.y) {
            console.log(positionX, positionY);
            grid[positionX][positionY] += 1;

            positionX += start.x < end.x ? 1 : -1;
            positionY += start.y < end.y ? 1 : -1;
        }
        grid[positionX][positionY] += 1;

        return;
    }

    // ================== pt 1 ==================

    for (
        let x = start.x;
        x != end.x + (start.x == end.x ? 1 : 0);
        x += start.x > end.x ? -1 : 1
    ) {
        for (
            let y = start.y;
            y != end.y + (start.y == end.y ? 1 : 0);
            y += start.y > end.y ? -1 : 1
        ) {
            grid[x][y] += 1;
        }
    }

    grid[end.x][end.y] += 1;
});

let output = "";
let intersections = 0;

grid.forEach((row) => {
    row.forEach((number) => {
        output += number;

        if (number > 1) {
            intersections++;
            // console.log(number);
        }
    });
    output += "\n";
});

console.log(intersections);
fs.writeFileSync("./grid.txt", output);
