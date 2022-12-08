const fs = require('fs')

function processInput() {
    return fs.readFileSync('./day6/input.txt', 'utf8')
}

const input = processInput()

function allUnique(chars) {
    return chars.every(c => chars.lastIndexOf(c) === chars.indexOf(c))
}

function solve(size) {
    for (let i = 0; i < input.length - size; i++) {
        const chunk = input.slice(i, i + size).split('')
        if (allUnique(chunk)) {
            return i + size
        }
    }
}

function solvePart1() {
    return solve(4)
}

function solvePart2() {
    return solve(14)
}

console.log(solvePart1() == 1356)
console.log(solvePart2() == 2564)
