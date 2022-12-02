const fs = require("fs");
const colors = require("colors");

let puzzleData = fs.readFileSync("./input.txt").toString().split("\n");
let totalRisk = 0;

for (let y = 0; y < puzzleData.length; y++) {
    const row = puzzleData[y].split("");
    for (let x = 0; x < row.length; x++) {
        const depth = parseInt(row[x]);
        let up = 10;
        let down = 10;
        let right = 10;
        let left = 10;

        if (y > 0) {
            up = parseInt(puzzleData[y - 1].split("")[x]);
        }

        if (y < puzzleData.length - 1) {
            down = parseInt(puzzleData[y + 1].split("")[x]);
        }

        if (x > 0) {
            left = parseInt(row[x - 1]);
        }

        if (x < row.length - 1) {
            right = parseInt(row[x + 1]);
        }

        if (
            [up, down, right, left].reduce((p, c) => {
                if (p) {
                    if (depth < c) {
                        return p;
                    } else {
                        return false;
                    }
                } else {
                    return p;
                }
            }, true)
        ) {
            totalRisk += 1 + depth;
        }
    }
}
console.log(totalRisk);
const colorsArr = ["green", "red"];
let basins = [];
let visited = [];

let queue = [];

const grid = puzzleData.map((row) => row.split(""));

const printGrid = (grid) => {
    let output = "";

    grid.forEach((row, y) => {
        row.forEach((num, x) => {
            let color = "white";

            basins.forEach((basin, i) => {
                basin.forEach((cell) => {
                    if (cell == `${x},${y}`) {
                        color = colorsArr[i % colorsArr.length];
                    }
                });
            });

            output += `${num}`[color];
        });
        output += "\n";
    });
    console.log(output);
};

const getCell = (x, y) => {
    return grid[y][x];
};

printGrid(grid);

for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[y].length; x++) {
        if (getCell(x, y) >= 9) {
            continue;
        }

        if (visited.findIndex((a) => a == `${x},${y}`) != -1) {
            continue;
        }

        queue.push([x, y]);

        if (queue.length) {
            basins.push([]);
        }

        const currentBasin = basins[basins.length - 1];

        while (queue.length) {
            const current = queue.shift();

            if (
                visited.findIndex((a) => a == `${current[0]},${current[1]}`) !=
                -1
            ) {
                continue;
            }

            visited.push(current);

            const x = current[0];
            const y = current[1];

            const depth = getCell(current[0], current[1]);

            if (depth >= 9) {
                continue;
            }

            if (x > 0) {
                queue.push([current[0] - 1, current[1]]);
            }

            if (x < grid[0].length - 1) {
                queue.push([current[0] + 1, current[1]]);
            }

            if (y > 0) {
                queue.push([current[0], current[1] - 1]);
            }

            if (y < grid.length - 1) {
                queue.push([current[0], current[1] + 1]);
            }

            currentBasin.push(`${current[0]},${current[1]}`);
        }
        // console.log(currentBasin);
    }
    // printGrid(grid);
    console.log(y);
}

basins = basins.sort((a, b) => b.length - a.length);
console.log(basins.map((basin) => basin.length));

console.log(basins[0].length * basins[1].length * basins[2].length);
