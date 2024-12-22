/** @param {string[]} box
 *  @returns {boolean} True if the gift is inside the box
 */
function inBox(box) {
    const height = box.length
    const width = box[0].length
    for (let i = 1; i < height - 1; i++) {
        const linea = box[i]
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