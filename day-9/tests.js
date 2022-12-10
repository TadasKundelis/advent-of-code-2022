const updateTailPosition = require('./solution').updateTailPosition

function areEqual(pos1, pos2) {
    return pos1.join('') === pos2.join('')
}

function test(headPos, tailPos, expectedTailPos) {
    return areEqual(updateTailPosition(headPos, tailPos), expectedTailPos)
}

console.log(test([0, 0], [0, 0], [0, 0])) // overlap
console.log(test([0, 0], [0, 1], [0, 1])) // touching horizontally
console.log(test([0, 0], [1, 0], [1, 0])) // touching vertically
console.log(test([0, 0], [1, 1], [1, 1])) // touching diagonally
console.log(test([0, 0], [0, 2], [0, 1])) // move to the left
console.log(test([0, 2], [0, 0], [0, 1])) // move to the right
console.log(test([0, 0], [2, 0], [1, 0])) // move up
console.log(test([2, 0], [0, 0], [1, 0])) // move down
console.log(test([2, 2], [0, 0], [1, 1])) // move diagonally
console.log(test([1, 2], [0, 0], [1, 1])) // move diagonally
console.log(test([1, 2], [2, 0], [1, 1])) // move diagonally
console.log(test([1, 2], [0, 4], [1, 3])) // move diagonally
console.log(test([1, 2], [2, 4], [1, 3])) // move diagonally