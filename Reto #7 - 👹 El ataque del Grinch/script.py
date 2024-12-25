def fix_packages(packages):
  stack = []
    
  for char in packages:
    if char == ')':
      temp = []
      # Extraemos los caracteres hasta encontrar '('
      while stack and stack[-1] != '(':
        temp.append(stack.pop())
      # Quitamos el '('
      stack.pop()
      # Añadimos los caracteres invertidos
      stack.extend(temp)
    else:
        # Añadimos el carácter al stack
        stack.append(char)
            
  return ''.join(stack)


print(fix_packages('a(cb)de'))
# ➞ "abcde"
# Volteamos "cb" dentro de los paréntesis

print(fix_packages('a(bc(def)g)h'))
# ➞ "agdefcbh"
# 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

print(fix_packages('abc(def(gh)i)jk'))
# ➞ "abcighfedjk"
# 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

print(fix_packages('a(b(c))e'))
# ➞ "acbe"
# 1º volteamos "c" → "c", luego "bc" → "cb"