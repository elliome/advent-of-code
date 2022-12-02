import { readFileSync } from 'fs';

const input = readFileSync('input.txt', 'utf8')
    .split('\n')
    .map(line => {
        const [playerA, playerB] = line.split(' ') as ['A' | 'B' | 'C', 'X' | 'Y' | 'Z'];
        return { playerA, playerB };
    });

let score = 0;

const A_ROCK = 'A';
const A_PAPER = 'B';
const A_SCISSORS = 'C';

const B_ROCK = 'X';
const B_PAPER = 'Y';
const B_SCISSORS = 'Z';

const B_LOSE = 'X';
const B_DRAW = 'Y';
const B_WIN = 'Z';

const pt2Input = input.map(({ playerA, playerB }) => {
    if(playerB === B_LOSE) {
        if(playerA === A_ROCK){
            playerB = B_SCISSORS;
        }else if (playerA === A_PAPER){
            playerB = B_ROCK;
        }else {
            playerB = B_PAPER;
        }
    }else if (playerB === B_DRAW) {
        if(playerA === A_ROCK){
            playerB = B_ROCK;
        }else if (playerA === A_PAPER){
            playerB = B_PAPER;
        }else {
            playerB = B_SCISSORS;
        }
    }else {
        if(playerA === A_ROCK){
            playerB = B_PAPER;
        }else if (playerA === A_PAPER){
            playerB = B_SCISSORS;
        }else {
            playerB = B_ROCK;
        }
    }

    return { playerA, playerB };
});

const playerBActionScore = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

const calculateScore = (input:{playerA:'A' | 'B' | 'C', playerB: 'X' | 'Y' | 'Z'}[]):number => {
    score = 0;

    input.forEach(({ playerA, playerB }) => {
        if(playerA === A_ROCK){
            if(playerB === B_PAPER){
                score += 6;
            }else if(playerB === B_ROCK){
                score += 3;
            }
        }else if (playerA === A_PAPER){
            if(playerB === B_SCISSORS){
                score += 6;
            }else if(playerB === B_PAPER){
                score += 3;
            }
        }else if (playerA === A_SCISSORS){
            if(playerB === B_ROCK){
                score += 6;
            }else if(playerB === B_SCISSORS){
                score += 3;
            }
        }

        score += playerBActionScore[playerB];
    });

    return score
}

console.log(calculateScore(input));

console.log(calculateScore(pt2Input));