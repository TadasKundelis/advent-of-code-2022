const fs = require('fs')

function processInput() {
    const rawData = fs.readFileSync('./day-5/input.txt', 'utf8')
    return rawData.split('\n')
        .map(line => line.match(/\d+/g).map(Number))
        .map(([count, from, to]) => [count, from - 1, to - 1])
}

const commands = processInput()

const stacks = [
    ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    ['M', 'F', 'V'],
    ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    ['D', 'Q', 'R', 'T', 'F'],
    ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    ['W', 'F', 'R', 'L', 'C', 'T'],
    ['T', 'Z', 'N', 'S'],
    ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N'],
]

function getResponse(stacks) {
    return stacks.map(s => s.pop()).join('')
}

function solvePart1() {
    const _stacks = stacks.map(s => s.slice())
    for (const [count, from, to] of commands) {
        for (let i = count; i > 0; i--) {
            _stacks[to].push(_stacks[from].pop())
        }
    }
    return getResponse(_stacks)
}

function solvePart2() {
    const _stacks = stacks.map(s => s.slice())
    for (const [count, from, to] of commands) {
        const fromStack = _stacks[from]
        const toStack = _stacks[to]
        _stacks[to] = toStack.concat(fromStack.slice(-count))
        _stacks[from] = fromStack.slice(0, fromStack.length - count)
    }
    return getResponse(_stacks)
}

console.log(solvePart1() == 'FRDSQRRCD')
console.log(solvePart2() == 'HRFTQVWNN')
