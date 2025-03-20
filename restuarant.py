# Define the restaurant menu with items and their prices
menu = {
    'Burger': 100,
    'Pizza': 150,
    'Pasta': 120,
    'Salad': 80,
    'Soda': 50,
    'Coffee': 40
}

# Function to display the menu
def display_menu():
    print("\n--- Vignan's Restaurant Menu ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

# Function to calculate the total bill
def generate_bill(order_items):
    total = 0
    print("\n--- Receipt ---")
    for item, quantity in order_items.items():
        price = menu.get(item, 0)
        item_total = price * quantity
        total += item_total
        print(f"{item} x {quantity} = ₹{item_total}")
    print(f"\nTotal Bill: ₹{total}")
    return total

# Main function to take customer orders
def take_order():
    order_items = {}
    while True:
        display_menu()
        item = input("\nEnter the item you want to order (or 'done' to finish): ").capitalize()
        
        if item.lower() == 'done':
            break
        
        if item not in menu:
            print("Sorry, this item is not available in the menu.")
            continue
        
        quantity = int(input(f"Enter the quantity for {item}: "))
        
        if item in order_items:
            order_items[item] += quantity  # Update quantity if item is already selected
        else:
            order_items[item] = quantity  # Add new item to the order

    total_amount = generate_bill(order_items)

    # Ask for payment method and print a receipt
    payment_method = input("\nEnter payment method (Cash/Card): ").capitalize()
    print(f"\nPayment Method: {payment_method}")
    print(f"Amount Paid: ₹{total_amount}")
    print("\nThank you for visiting Vignan's Restaurant! Have a great day!")

# Call the take_order function to start the program
if __name__ == "__main__":
    take_order()
