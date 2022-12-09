const fs = require('fs')

function readInput() {
    return fs.readFileSync('./day9/input.txt', 'utf8')
        .split('\n')
        .map(line => {
            const [direction, steps] = line.split(' ')
            return [direction, Number(steps)]
        })
}

const input = readInput()

function updateTailCoordinate(headPos, tailPos) {
    const diff = headPos - tailPos
    const sign = diff < 0 ? -1 : 1
    const step = Math.min(Math.abs(diff), 1)
    return tailPos + step * sign
}

function updateTailPosition(headPos, tailPos) {
    let [tailRow, tailCol] = tailPos
    if (!areTouching(headPos, tailPos)) {
        let [headRow, headCol] = headPos
        tailRow = updateTailCoordinate(headRow, tailRow)
        tailCol = updateTailCoordinate(headCol, tailCol)
    }
    return [tailRow, tailCol]
}

function areTouching([headRow, headCol], [tailRow, tailCol]) {
    return Math.abs(headRow - tailRow) < 2 && Math.abs(headCol - tailCol) < 2
}

function updateHeadPosition(head, direction) {
    let [headRow, headCol] = head
    if (direction === 'L') headCol--
    if (direction === 'R') headCol++
    if (direction === 'U') headRow--
    if (direction === 'D') headRow++
    return [headRow, headCol]
}

function updatePositions(remaining, updated) {
    if (!remaining.length) return updated
    const [lastUpdated] = updated
    const newUpdated = updateTailPosition(lastUpdated, remaining.pop())
    return updatePositions(remaining, [newUpdated, ...updated])
}

function solve(numOfKnots) {
    const tailPositions = {'0#0': true}
    let knots = Array(numOfKnots).fill([0, 0])

    for (let [direction, steps] of input) {
        while (steps) {
            const updatedHead = updateHeadPosition(knots[numOfKnots - 1], direction)
            knots = updatePositions(knots.slice(0, -1), [updatedHead])
            const [updatedTailRow, updatedTailCol] = knots[0]
            tailPositions[`${updatedTailRow}#${updatedTailCol}`] = true
            steps--
        }
    }

    return Object.keys(tailPositions).length
}

function solvePart1() {
    return solve(2)
}

function solvePart2() {
    return solve(10)
}

console.log(solvePart1() === 5907)
console.log(solvePart2() === 2303)

module.exports = {
    updateTailPosition
}