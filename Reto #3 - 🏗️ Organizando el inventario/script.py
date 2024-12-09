def organize_inventory(inventory):
    organized_inventory = {}

    for item in inventory:
        current_category = item['category']
        current_name = item['name']
        current_quantity = item['quantity']

        if current_category not in organized_inventory:
            organized_inventory[current_category] = {}

        if current_name not in organized_inventory[current_category]:
            organized_inventory[current_category][current_name] = 0
        
        organized_inventory[current_category][current_name] += current_quantity

    return organized_inventory

inventory = [
    { 'name': 'doll', 'quantity': 5, 'category': 'toys' },
    { 'name': 'car', 'quantity': 3, 'category': 'toys' },
    { 'name': 'ball', 'quantity': 2, 'category': 'sports' },
    { 'name': 'car', 'quantity': 2, 'category': 'toys' },
    { 'name': 'racket', 'quantity': 4, 'category': 'sports' }
]

print(organize_inventory(inventory))

# Resultado esperado:
# {
#   toys: {
#     doll: 5,
#     car: 5
#   },
#   sports: {
#     ball: 2,
#     racket: 4
#   }
# }