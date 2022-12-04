const fs = require('fs')

function processInput() {
    const rawData = fs.readFileSync('./day4/input.txt', 'utf8')
    return rawData.split('\n').map(line =>
        line.split(',').map(range => range.split('-').map(Number))
    )
}

const lines = processInput()

function sortLine(pair1, pair2) {
    if (pair1[0] !== pair2[0]) return pair1[0] - pair2[0]
    else return pair2[1] - pair1[1]
}

for (const line of lines) line.sort(sortLine)

function solvePart1() {
    return lines.reduce((count, line) => {
        const [[a, b], [c, d]] = line
        return a <= c && b >= d ? count + 1 : count
    }, 0)
}

function solvePart2() {
    return lines.reduce((count, line) => {
        const [[a, b], [c, d]] = line
        return c <= b ? count + 1 : count
    }, 0)
}

console.log(solvePart1() == 582)
console.log(solvePart2() == 893)
