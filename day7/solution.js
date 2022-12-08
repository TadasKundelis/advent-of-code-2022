const fs = require('fs')

function readInput() {
    return fs.readFileSync('./day7/input.txt', 'utf8').split('\n')
}

class File {
    constructor(name, size) {
        this.name = name
        this.size = size
    }
}

class Directory {
    constructor(parentDir) {
        this.parentDir = parentDir
        this.files = []
        this.childDirs = {}
    }

    addChildDirIfNotExists(dirName) {
        this.childDirs[dirName] = this.childDirs[dirName] || new Directory(this)
    }

    addFile(file) {
        this.files.push(file)
    }

    computeDirSize() {
        const fileSizes = this.files.map(file => file.size)
        const childDirSizes = Object.values(this.childDirs).map(dir => dir.computeDirSize())
        return fileSizes.reduce((a, b) => a + b, 0) + childDirSizes.reduce((a, b) => a + b, 0)
    }
}

class FileSystem {
    constructor() {
        this.root = new Directory(null)
        this.currentDir = this.root
    }

    addDir(dirName) {
        this.currentDir.addChildDirIfNotExists(dirName)
    }

    addFile(file) {
        this.currentDir.addFile(file)
    }

    goToDir(dir) {
        if (dir === '/') {
            this.currentDir = this.root
        } else if (dir === '..') {
            this.currentDir = this.currentDir.parentDir
        } else {
            this.currentDir = this.currentDir.childDirs[dir]
        }
    }
}

function processCommands() {
    let i = 0

    while (i < input.length) {
        const line = input[i]
        const [_, command, dir] = line.split(' ')

        switch (command) {
            case 'cd':
                fileSystem.goToDir(dir)
                break
            case 'ls':
                while (i + 1 < input.length && input[i + 1][0] !== '$') {
                    addDirOrFile(input[++i])
                }
                break
        }
        i++
    }
}

function addDirOrFile(line) {
    const [a, b] = line.split(' ')
    if (a === 'dir') {
        const dirName = b
        fileSystem.addDir(dirName)
    } else {
        const [size, name] = [a, b]
        fileSystem.addFile(new File(name, Number(size)))
    }
}

function traverseAndSum(dir) {
    const size = dir.computeDirSize()
    const total = size <= 100000 ? size : 0
    return Object.values(dir.childDirs).reduce((acc, curr) => acc + traverseAndSum(curr), total)
}

const input = readInput()
const fileSystem = new FileSystem()

function solvePart1() {
    processCommands()
    return traverseAndSum(fileSystem.root)
}

const TOTAL_AVAILABLE_SPACE = 70000000
const NEEDED_FREE_SPACE = 30000000

function findSmallestDir(dir, missing) {
    const currentSize = dir.computeDirSize()
    const childDirSizes = Object.values(dir.childDirs).map(childDir => findSmallestDir(childDir, missing))
    return Math.min(...[currentSize].concat(childDirSizes).filter(size => size >= missing))
}

function solvePart2() {
    const totalUsedSpace = fileSystem.root.computeDirSize()
    const currentFreeSpace = TOTAL_AVAILABLE_SPACE - totalUsedSpace
    const missingSpace = NEEDED_FREE_SPACE - currentFreeSpace
    return findSmallestDir(fileSystem.root, missingSpace)
}

console.log(solvePart1() == 1583951)
console.log(solvePart2() == 214171)


