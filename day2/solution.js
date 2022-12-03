const fs = require('fs')

Array.prototype.sum = function () {
    return this.reduce((a, b) => a + b)
}

function processInput() {
    const rawData = fs.readFileSync('./day2/input.txt', 'utf8')
    return rawData.split('\n').map(l => l.split(' '))
}

const draw = {
    A: 'X',
    B: 'Y',
    C: 'Z'
}

const winning = {
    C: 'X',
    B: 'Z',
    A: 'Y'
}

const losing = {
    C: 'Y',
    B: 'X',
    A: 'Z'
}

const pointsForOutcome = {
    X: 0,
    Y: 3,
    Z: 6
}

const pointsForChoice = {
    X: 1,
    Y: 2,
    Z: 3
}

const games = processInput()

function pointsForGamePart1([hisChoice, myChoice]) {
    let points = pointsForChoice[myChoice]

    if (winning[hisChoice] === myChoice) points += 6
    if (draw[hisChoice] === myChoice) points += 3

    return points
}

function solvePart1() {
    return games.map(pointsForGamePart1).sum()
}

function resolveMyChoice(hisChoice, outcome) {
    const mapping = {
        X: losing[hisChoice],
        Y: draw[hisChoice],
        Z: winning[hisChoice],
    }

    return mapping[outcome]
}


function pointsForGamePart2([hisChoice, outcome]) {
    const points = pointsForOutcome[outcome]
    const myChoice = resolveMyChoice(hisChoice, outcome)
    return points + pointsForChoice[myChoice]
}

function solvePart2() {
    return games.map(pointsForGamePart2).sum()
}

console.log(solvePart1() == 15523)
console.log(solvePart2() == 15702)
