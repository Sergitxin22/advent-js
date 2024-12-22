function inBox(box: string[]): boolean {
    const height: number = box.length
    const width: number = box[0].length

    for (let i = 1; i < height - 1; i++) {
        const linea: string = box[i]
        if (linea.slice(1, width - 1)?.indexOf("*") != -1) {
            return true
        }
    }

    return false
}

console.log(inBox([
    "###",
    "#*#",
    "###"
])) // ➞ true

console.log(inBox([
    "####",
    "#* #",
    "#  #",
    "####"
])) // ➞ true

console.log(inBox([
    "#####",
    "#   #",
    "#  #*",
    "#####"
])) // ➞ false

console.log(inBox([
    "#####",
    "#   #",
    "#   #",
    "#   #",
    "#####"
])) // ➞ false