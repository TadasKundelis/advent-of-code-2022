function splitIntoChunks(items, size) {
    const chunks = []
    let curr = []
    for (const i in items) {
        const line = items[i]
        curr.push(line)
        if (curr.length === size) {
            chunks.push(curr)
            curr = []
        }
    }
    return chunks
}

module.exports = {
    splitIntoChunks
}