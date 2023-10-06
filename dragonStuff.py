stuff  = {"rope": 1,"gold coin": 42}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        if loot in inventory:
            inventory[loot] += 1
        else:
            inventory.setdefault(loot, 1)

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in stuff.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
