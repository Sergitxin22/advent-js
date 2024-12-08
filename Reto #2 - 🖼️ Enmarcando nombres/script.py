def createFrame(names):
    frame = ''
    longest_name = names[0]

    for name in names:
        if len(name) > len(longest_name):
            longest_name = name

    frame += (2*"*" + (len(longest_name)*"*") + 2*"*")
    frame += "\n"
    for name in names:
        frame += ("* " + name + ((len(longest_name) - len(name))*" ") + " *\n")
    frame += (2*"*" + (len(longest_name)*"*") + 2*"*")

    return frame

print(createFrame(['midu', 'madeval', 'educalvolpz']))

# Resultado esperado:
# ***************
# * midu        *
# * madeval     *
# * educalvolpz *
# ***************

print(createFrame(['midu']))

# Resultado esperado:
# ********
# * midu *
# ********

print(createFrame(['a', 'bb', 'ccc']))

# Resultado esperado:
# *******
# * a   *
# * bb  *
# * ccc *
# *******

print(createFrame(['a', 'bb', 'ccc', 'dddd']))