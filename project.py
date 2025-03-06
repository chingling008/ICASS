"""
Name : Cizario Gum
Project: ICASS PAT1
DESCRIPTION: INVENTORY LOGING
"""

totalcost = 0.00
inventory = {}  # Dictionary to store inventory data (product: quantity)
low_stock_threshold = 10 #set the low stock threshold

def addingStock(product, quantity, supplier, cost_per_unit):
    """Adds stock to the inventory and updates the log file."""
    global totalcost
    totalcost = quantity * cost_per_unit
    large_order = " (Large Order)" if quantity > 100 else ""  # Example: Large order if quantity > 100

    with open("inventory_log.txt", "a") as file:
        file.write(f"Product: {product}, Quantity: {quantity}, Supplier: {supplier}, Total Cost: R{totalcost:.2f}{large_order}\n")

    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    print(f"Added {quantity} units of {product} to inventory.")

def low_stock():
    """Checks and prints products with low stock."""
    low_stock_products = []
    for product, quantity in inventory.items():
        if quantity <= low_stock_threshold:
            low_stock_products.append(product)

    if low_stock_products:
        print("\nLow Stock Products:")
        for product in low_stock_products:
            print(f"- {product} (Quantity: {inventory[product]})")
    else:
        print("\nNo products are currently low in stock.")

def processOrders(product, quantity_ordered):
    """Processes customer orders and updates inventory."""
    if product in inventory:
        if inventory[product] >= quantity_ordered:
            inventory[product] -= quantity_ordered
            print(f"Processed order for {quantity_ordered} units of {product}.")
            if inventory[product] <= 0:
                del inventory[product] #removes product from inventory if the quantity is 0.
        else:
            print(f"Insufficient stock for {product}. Available: {inventory[product]}")
    else:
        print(f"{product} not found in inventory.")


# Example usage (you can add more input prompts or a menu):
productName = input("Enter the product name: ")
quanRec = int(input("Enter quantity received as integer: "))
supplierName = input("Enter the supplier name: ")
costUnit = float(input("The cost per unit in rands: "))

addingStock(productName, quanRec, supplierName, costUnit)
low_stock()

order_product = input("Enter product to order (or leave blank): ")
if order_product:
    order_quantity = int(input("Enter quantity to order: "))
    processOrders(order_product, order_quantity)

low_stock() #checks low stock again after order is processed.
totalCost = quanRec * costUnit

large_order = " (Large Order)" if quanRec > 100 else ""  # Example: Large order if quantity > 100

with open("inventory_log.txt", "a") as file:
    file.write(f"Product: {productName}, Quantity: {quanRec}, Supplier: {supplierName}, Total Cost: R{totalCost:.2f}{large_order}\n")

print(f"Inventory log updated in 'inventory_log.txt'")
