const fs = require('fs')
const {splitIntoChunks} = require("../helpers");

function readInput() {
    return fs.readFileSync('./day-10/input.txt', 'utf8')
        .split('\n')
        .map(line => {
            const [command, num] = line.split(' ')
            return command === 'addx' ? Number(num) : 0 // would not work with "addx 0" but oh well
        })
}

const input = readInput()

function resolveValuesForCycles(inputNums, numsByCycle, nextValue) {
    if (!inputNums.length) return numsByCycle
    const nextInputNum = inputNums.shift()
    const updatedNums = nextInputNum ? numsByCycle.concat([nextValue, nextValue]) : numsByCycle.concat(nextValue)
    return resolveValuesForCycles(inputNums, updatedNums, nextValue + nextInputNum)
}

function signalStrengthSum(cycleToValue) {
    let total = 0
    for (let i = 20; i < cycleToValue.length; i += 40) {
        total += cycleToValue[i] * i
    }
    return total
}

function solvePart1() {
    const cycleToValue = resolveValuesForCycles(input.slice(), [null], 1)
    return signalStrengthSum(cycleToValue)
}

function solvePart2() {
    const cycleToValue = resolveValuesForCycles(input.slice(), [null], 1)
    const pixels = Array(240).fill('.')
    for (let i = 0; i < cycleToValue.length; i++) {
        const spritePositions = getSpritePositions(cycleToValue[i + 1])
        if (spritePositions.includes(i % 40)) pixels[i] = '#'
    }
    return printResponse(pixels)
}

function getSpritePositions(middle) {
    return [middle - 1, middle, middle + 1]
}

function printResponse(pixels) {
    return splitIntoChunks(pixels, 40).map(chunk => chunk.join('')).join('\n')
}

console.log(solvePart1() === 14780)
console.log(solvePart2())
