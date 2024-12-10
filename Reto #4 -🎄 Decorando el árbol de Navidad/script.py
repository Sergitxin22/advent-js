def create_xmas_tree(height, ornament):
    xmas_tree = ""
    for index in range(height):
        if height - index > 0:
            xmas_tree += (height - index - 1)*"_"
            xmas_tree += index*ornament
            xmas_tree += ornament
            xmas_tree += index*ornament
            xmas_tree += (height - index - 1)*"_" + "\n"

    xmas_tree += (height - 1)*"_" + "#" + (height - 1)*"_" + "\n"
    xmas_tree += (height - 1)*"_" + "#" + (height - 1)*"_"
    return xmas_tree

tree = create_xmas_tree(5, '*')
print(tree)
print()
"""
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
"""

tree2 = create_xmas_tree(3, '+')
print(tree2)
print()
"""
__+__
_+++_
+++++
__#__
__#__
"""

tree3 = create_xmas_tree(6, '@')
print(tree3)
"""
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
"""