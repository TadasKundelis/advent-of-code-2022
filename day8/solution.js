const fs = require('fs')

function readInput() {
    return fs.readFileSync('./day8/input.txt', 'utf8')
        .split('\n').map(line => line.split('').map(Number))
}

const matrix = readInput()

function seenFromLeft(matrix, row, col) {
    let pos = 0
    while (pos < col) {
        if (matrix[row][pos] >= matrix[row][col]) return false
        pos++
    }
    return true
}

function seenFromRight(matrix, row, col) {
    let pos = matrix[0].length - 1
    while (pos > col) {
        if (matrix[row][pos] >= matrix[row][col]) return false
        pos--
    }
    return true
}

function seenFromTop(matrix, row, col) {
    let pos = 0
    while (pos < row) {
        if (matrix[pos][col] >= matrix[row][col]) return false
        pos++
    }
    return true
}

function seenFromBottom(matrix, row, col) {
    let pos = matrix.length - 1
    while (pos > row) {
        if (matrix[pos][col] >= matrix[row][col]) return false
        pos--
    }
    return true
}

let count = 0

for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
        if (seenFromLeft(matrix, i, j) || seenFromRight(matrix, i, j) || seenFromTop(matrix, i, j) || seenFromBottom(matrix, i, j)) {
            count++
        }
    }
}

// part 2

function seeOnTheLeft(matrix, row, col) {
    let count = 0
    let pos = col
    while (--pos >= 0) {
        count++
        if (matrix[row][pos] >= matrix[row][col]) break
    }
    return count
}

function seeOnTheRight(matrix, row, col) {
    let count = 0
    let pos = col
    while (++pos < matrix[0].length) {
        count++
        if (matrix[row][pos] >= matrix[row][col]) break
    }
    return count
}

function seeOnTheTop(matrix, row, col) {
    let count = 0
    let pos = row
    while (--pos >= 0) {
        count++
        if (matrix[pos][col] >= matrix[row][col]) break
    }
    return count
}

function seeOnTheBottom(matrix, row, col) {
    let count = 0
    let pos = row
    while (++pos < matrix.length) {
        count++
        if (matrix[pos][col] >= matrix[row][col]) break
    }
    return count
}

let best = 0

for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
        let total = seeOnTheLeft(matrix, i, j) * seeOnTheRight(matrix, i, j) * seeOnTheTop(matrix, i, j) * seeOnTheBottom(matrix, i, j)
        best = Math.max(best, total)
    }
}

console.log(best == 422059)
