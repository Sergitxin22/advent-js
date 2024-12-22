def in_box(box):
  encontrado = False
  height = len(box)
  width = len(box[0])
  # print(f"{height}, {width}")
  for index, linea in enumerate(box):
    try:
      posicion_encontrado = linea.index("*")
      # Intentamos encontrar el índice de '*' en la línea
      if index > 0 and index < height -1:
        return
      
      if posicion_encontrado > 0 and posicion_encontrado < width-1:
        # Si encuentra el asterisco, imprime en qué línea está
        # print(f"Está el *, en la línea: {index}, {posicion_encontrado}")
        encontrado = True
    except ValueError:
      # Si no se encuentra el asterisco, capturamos el ValueError y mostramos que no está
      None
  
  print(f"Encontrado: {encontrado}")


in_box([
  "###",
  "#*#",
  "###"
]) # ➞ true

in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) # ➞ true

in_box([
  "#####",
  "#   #",
  "#  #*",
  "#####"
]) # ➞ false

in_box([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) # ➞ false