stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for object,amount in inventory.items() : 
        print(amount, object)
        total = total + amount
    print("Total number of items:", total)



if __name__ == "__main__":
    displayInventory(stuff)
