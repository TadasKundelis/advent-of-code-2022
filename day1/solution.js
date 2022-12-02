const fs = require('fs')

Array.prototype.sum = function () {
  return this.reduce((a, b) => a + b)
}

function processInput() {
  const raw_data = fs.readFileSync('./day1/input.txt', 'utf8');
  return raw_data
    .split('\n\n')
    .map(line => line.split('\n').map(Number))
}

const caloryListsPerElf = processInput()
const totalCaloriesPerElf = caloryListsPerElf.map(calories => calories.sum())

function solvePart1() {
  return Math.max(...totalCaloriesPerElf)
}

function solvePart2() {
  totalCaloriesPerElf.sort((a, b) => b - a)
  return totalCaloriesPerElf.slice(0, 3).sum()
}

console.log(solvePart1() == 68787)
console.log(solvePart2() == 198041)

