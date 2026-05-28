class ItemToPurchase:
    # Set up a default item so every object starts with known values.
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    # Print the cost for one item.
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ "
            f"${self.item_price:g} = ${total_cost:g}"
        )

    # Print the description for one item.
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    # Set up a shopping cart with customer details and an empty item list.
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add one item object to the cart.
    def add_item(self, item):
        self.cart_items.append(item)

    # Remove an item from the cart by matching the item name.
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    # Update only the item details that are not still set to default values.
    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    # Add all item quantities together.
    def get_num_items_in_cart(self):
        total_quantity = 0

        for item in self.cart_items:
            total_quantity = total_quantity + item.item_quantity

        return total_quantity

    # Add all item costs together.
    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)

        return total_cost

    # Print the shopping cart total.
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

            print(f"Total: ${self.get_cost_of_cart():g}")

    # Print all item descriptions in the cart.
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


def get_required_text(prompt):
    # Keep asking until the user enters text.
    user_input = input(prompt)

    while user_input.strip() == "":
        print("Invalid input. Please enter a value.")
        user_input = input(prompt)

    return user_input.strip()


def get_positive_number(prompt):
    # Keep asking until the user enters a positive number.
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_whole_number(prompt):
    # Keep asking until the user enters a positive whole number.
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Invalid input. Please enter a positive whole number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def print_menu(cart):
    option = ""

    # Keep showing the menu until the customer chooses to quit.
    while option != "q":
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        option = input("Choose an option:\n")

        while option not in ("a", "r", "c", "i", "o", "q"):
            print("Invalid input. Please enter a valid menu option.")
            option = input("Choose an option:\n")

        if option == "a":
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = get_required_text("Enter the item name:\n")
            item.item_description = get_required_text("Enter the item description:\n")
            item.item_price = get_positive_number("Enter the item price:\n")
            item.item_quantity = get_positive_whole_number("Enter the item quantity:\n")
            cart.add_item(item)

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            item_name = get_required_text("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = get_required_text("Enter the item name:\n")
            item.item_quantity = get_positive_whole_number("Enter the new quantity:\n")
            cart.modify_item(item)

        elif option == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif option == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()


def main():
    # Get the customer information before starting the shopping cart menu.
    customer_name = get_required_text("Enter customer's name:\n")
    current_date = get_required_text("Enter today's date:\n")

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
