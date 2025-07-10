item_inventory = {'arrow': 12, 
                  'gold coin': 42, 
                  'rope': 1,
                  'torch': 6,
                  'dagger': 1}


def displayInventory(inventory, item):
    print(f"Inventory:")
    for i, j in inventory.items(): # Loop through `item_inventory` dictionary that was passed through the `displayInventory` function
        print(f"{j} {i}")
   

displayInventory(item_inventory, 0)

# Output
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger




