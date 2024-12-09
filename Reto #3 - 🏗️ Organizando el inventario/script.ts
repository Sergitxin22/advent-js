type Inventory = Array<
    { name: string, quantity: number, category: string }
>

function organizeInventory(inventory: Inventory): object {
    let organizedInventory = {}

    inventory.forEach(item => {
        let currentCategory: string = item['category']
        let currentName: string = item['name']
        let currentQuantity: number = item['quantity']

        if (!organizedInventory[currentCategory])
            organizedInventory[currentCategory] = {}

        if (!organizedInventory[currentCategory][currentName])
            organizedInventory[currentCategory][currentName] = 0

        organizedInventory[currentCategory][currentName] += currentQuantity
    });

    return organizedInventory
}

const inventory = [
    { name: 'doll', quantity: 5, category: 'toys' },
    { name: 'car', quantity: 3, category: 'toys' },
    { name: 'ball', quantity: 2, category: 'sports' },
    { name: 'car', quantity: 2, category: 'toys' },
    { name: 'racket', quantity: 4, category: 'sports' }
]

console.log(organizeInventory(inventory))

// Resultado esperado:
// {
//   toys: {
//     doll: 5,
//     car: 5
//   },
//   sports: {
//     ball: 2,
//     racket: 4
//   }