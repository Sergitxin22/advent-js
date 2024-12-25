/** @param {string} packages with parentheses
 *  @returns {string} Fixed and sorted packages
 */
function fixPackages(packages) {
    const stack = [];

    for (const char of packages) {
        if (char === ')') {
            let reversed = '';
            while (stack.at(-1) !== '(') {
                reversed += stack.pop();
            }

            stack.pop(); // Elimina '('
            stack.push(...reversed);
        } else {
            stack.push(char);
        }
    }

    return stack.join('');
}

console.log(fixPackages('a(cb)de'))
// ➞ "abcde"
// Volteamos "cb" dentro de los paréntesis

console.log(fixPackages('a(bc(def)g)h'))
// ➞ "agdefcbh"
// 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

console.log(fixPackages('abc(def(gh)i)jk'))
// ➞ "abcighfedjk"
// 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

console.log(fixPackages('a(b(c))e'))
// ➞ "acbe"
// 1º volteamos "c" → "c", luego "bc" → "cb"