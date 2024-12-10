/**
 * @param {number} height - Height of the tree
 * @param {string} ornament - Symbol to draw
 * @returns {string} Drawn tree
 */
function createXmasTree(height, ornament) {
    let xmasTree = ""
    for (let index = 0; height - index > 0; index++) {
        xmasTree += "_".repeat(height - index - 1)
        xmasTree += ornament.repeat(index)
        xmasTree += ornament
        xmasTree += ornament.repeat(index)
        xmasTree += "_".repeat(height - index - 1) + "\n"
    }
    xmasTree += "_".repeat(height - 1) + "#" + "_".repeat(height - 1) + "\n"
    xmasTree += "_".repeat(height - 1) + "#" + "_".repeat(height - 1)
    return xmasTree
}

const tree = createXmasTree(5, '*')
console.log(tree)
console.log()
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/

const tree2 = createXmasTree(3, '+')
console.log(tree2)
console.log()
/*
__+__
_+++_
+++++
__#__
__#__
*/

const tree3 = createXmasTree(6, '@')
console.log(tree3)
/*
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
*/