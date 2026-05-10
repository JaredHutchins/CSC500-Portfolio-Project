class ItemToPurchase:
    # Set up a default item so every object starts with known values.
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Print the cost for one item.
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ "
            f"${self.item_price:g} = ${total_cost:g}"
        )


if __name__ == "__main__":
    # Create two item objects for the shopping cart.
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Store each item object as an element in the shopping cart list.
    cart = [item1, item2]

    # Collect item details for each object in the cart.
    for item_number, item in enumerate(cart, 1):
        print(f"Item {item_number}")
        print("Enter the item name:")
        item.item_name = input()

        # Keep asking for the price until we get a valid non-negative number.
        while True:
            print("Enter the item price:")
            try:
                item.item_price = float(input())
                if item.item_price < 0:
                    print("Invalid input. Price cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Keep asking for the quantity until we get a valid non-negative whole number.
        while True:
            print("Enter the item quantity:")
            try:
                item.item_quantity = int(input())
                if item.item_quantity < 0:
                    print("Invalid input. Quantity cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        print()

    # Go through each element in the cart list and print its item cost.
    print("TOTAL COST")
    for item in cart:
        item.print_item_cost()

    # Go through the cart again and add all item totals together.
    total_cost = 0
    for item in cart:
        total_cost = total_cost + (item.item_price * item.item_quantity)
    print(f"Total: ${total_cost:g}")
