def organize_shoes(shoes):
    # Crear un diccionario para contar las botas de tipo I y R por tamaño
    shoe_counts = {}

    # Contamos las botas de tipo I y R por tamaño
    for shoe in shoes:
        size = shoe['size']
        shoe_type = shoe['type']
        
        if size not in shoe_counts:
            shoe_counts[size] = {'I': 0, 'R': 0}
        
        shoe_counts[size][shoe_type] += 1

    # Crear una lista con los tamaños que tienen pares disponibles
    pairs = []
    for size, counts in shoe_counts.items():
        countI = counts['I']
        countR = counts['R']
        min_pairs = min(countI, countR)  # Número de pares posibles
        pairs.extend([size] * min_pairs)  # Añadir los pares al resultado

    return pairs

# Ejemplos de uso
shoes1 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38},
    {'type': 'R', 'size': 42},
    {'type': 'I', 'size': 41},
    {'type': 'I', 'size': 42}
]

shoes2 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38},
    {'type': 'I', 'size': 38},
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38}
]

shoes3 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 36},
    {'type': 'R', 'size': 42},
    {'type': 'I', 'size': 41},
    {'type': 'I', 'size': 43}
]

print(organize_shoes(shoes1))  # [38, 42]
print(organize_shoes(shoes2))  # [38, 38]
print(organize_shoes(shoes3))  # []