const fs = require('fs')
const {splitIntoChunks} = require("../helpers");

function processInput() {
    const rawData = fs.readFileSync('./day3/input.txt', 'utf8')
    return rawData.split('\n').map(line => line.split(''))
}

const lines = processInput()
const lower = 'abcdefghijklmnopqrstuvwxyz'
const allLetters = ' ' + lower + lower.toUpperCase()

function findCommonChar(line) {
    const firstHalf = line.slice(0, line.length / 2)
    const secondHalf = line.slice(line.length / 2)

    return firstHalf.find(char => secondHalf.includes(char))
}

function solvePart1() {
    return lines.reduce((acc, line) => {
        const commonChar = findCommonChar(line)
        return acc + allLetters.indexOf(commonChar)
    }, 0)
}

function findCommonCharPart2([line1, line2, line3]) {
    return line1.find(char => line2.includes(char) && line3.includes(char))
}

function solvePart2() {
    const chunks = splitIntoChunks(lines,3)

    return chunks.reduce((acc, chunk) => {
        const commonChar = findCommonCharPart2(chunk)
        return allLetters.indexOf(commonChar) + acc
    }, 0)
}

console.log(solvePart1() == 7875)
console.log(solvePart2() == 2479)