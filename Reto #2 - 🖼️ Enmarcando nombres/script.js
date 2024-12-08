function createFrame(names) {
    let frame = ""
    let longestName = names[0]

    names.forEach(name => {
        if (name.length > longestName.length) {
            longestName = name
        }
    });

    frame += ("*".repeat(2)) + "*".repeat(longestName.length) + "*".repeat(2) + "\n"
    names.forEach(name => {
        frame += "* " + name + " ".repeat(longestName.length - name.length) + " *\n"
    });

    frame += ("*".repeat(2)) + "*".repeat(longestName.length) + "*".repeat(2)

    return frame
}

console.log(createFrame(['midu', 'madeval', 'educalvolpz']))

// Resultado esperado:
//   ***************
//   * midu        *
//   * madeval     *
//   * educalvolpz *
//   ***************

console.log(createFrame(['midu']))

// Resultado esperado:
//   ********
//   * midu *
//   ********

console.log(createFrame(['a', 'bb', 'ccc']))

// Resultado esperado:
//   *******
//   * a   *
//   * bb  *
//   * ccc *
//   *******

console.log(createFrame(['a', 'bb', 'ccc', 'dddd']))