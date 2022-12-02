const fs = require("fs");
const puzzleData = fs.readFileSync("./input.txt").toString().split("\n");

const input = puzzleData.shift().split(",");
let players = [];

puzzleData.forEach((line) => {
    if (line === "") {
        players.push({
            board: [],
            hits: [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        });
        return;
    }

    players[players.length - 1].board.push(
        line.split(" ").filter((number) => {
            if (number !== " ") {
                return number;
            }
        })
    );
});

let end = false;
let pt1solution = 0;
let pt2solution = 0;

top: for (let i = 0; i < input.length; i++) {
    const numberInput = input[i];

    players = players.filter((player, playerIndex) => {
        if (end) return player;

        let bingo = false;

        player.board.filter((line, lineIndex) => {
            line.forEach((number, numberIndex) => {
                if (number === numberInput) {
                    player.hits[lineIndex][numberIndex] = 1;
                    // check row
                    if (
                        player.hits[lineIndex].reduce(
                            (p, c) => p + parseInt(c),
                            0
                        ) == 5
                    ) {
                        bingo = true;
                    }

                    // check column
                    let colHits = player.hits.map((row) => row[numberIndex]);
                    if (colHits.reduce((p, c) => p + parseInt(c), 0) == 5) {
                        bingo = true;
                    }

                    if (bingo) {
                        let sum = 0;
                        player.hits.forEach((hitRow, hitRowIndex) => {
                            hitRow.forEach((hit, hitColIndex) => {
                                if (hit === 0) {
                                    sum += parseInt(
                                        player.board[hitRowIndex][hitColIndex]
                                    );
                                }
                            });
                        });

                        if (!pt1solution) {
                            pt1solution = sum * number;
                        }

                        if (players.length == 1) {
                            pt2solution = sum * number;
                        }
                    }
                }
            });
        });

        if (bingo) {
            player = null;
        }

        return player;
    });

    if (players.length === 0) {
        break;
    }
}

console.log(pt1solution, pt2solution);
