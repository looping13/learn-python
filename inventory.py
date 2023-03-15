# D&D inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'bow': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    totalObject = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalObject = totalObject + v
    print('Total number of items: ' + str(totalObject))


def addToInventory(inventory, addeditems):
    for items in addeditems:
        if items in inventory:
            inventory[items] = inventory[items] + 1
        else:
            inventory[items] = 1
    displayInventory(inventory)


displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(stuff, dragonLoot)
