# Restaurant Billing System
# Developed by: Viswa

MENU = {
    "biriyani": 200,
    "naan with curry": 300,
    "starters": 200,
    "desserts": 200,
    "spl.biriyani": 700,
    "soft drink": 50
}


def calculate_discount(quantity):
    """Return discount percentage based on quantity."""

    if 1 <= quantity <= 5:
        return 0.05
    elif 6 <= quantity <= 10:
        return 0.10
    elif 11 <= quantity <= 15:
        return 0.15
    else:
        return 0


def display_menu():
    """Display restaurant menu."""

    print("\n" + "*" * 50)
    print("          WELCOME TO YOUR'S KITCHEN")
    print("*" * 50)

    print("\nMENU")
    print("-" * 50)

    for item, price in MENU.items():
        print(f"{item.title():20} - ₹{price}")

    print("-" * 50)
    print("Maximum quantity allowed per item: 15")
    print("*" * 50)


def take_order():
    """Take customer orders and calculate the bill."""

    orders = {}

    print("\nPlace your order.")
    print("Enter 1 to order an item.")
    print("Enter 0 to skip an item.")

    for item, price in MENU.items():

        choice = int(input(f"\nEnter 1 to place {item}: "))

        if choice == 1:

            quantity = int(input("Enter number of plates: "))

            if quantity < 1 or quantity > 15:
                print("Invalid quantity! Please order between 1 and 15.")
                continue

            subtotal = price * quantity

            discount_rate = calculate_discount(quantity)
            discount_amount = subtotal * discount_rate
            final_amount = subtotal - discount_amount

            orders[item] = {
                "quantity": quantity,
                "price": price,
                "subtotal": subtotal,
                "discount": discount_amount,
                "final_amount": final_amount
            }

            print(f"{item.title()} selected.")
            print(f"Subtotal: ₹{subtotal}")
            print(f"Discount: {discount_rate * 100:.0f}%")
            print(f"Final amount: ₹{final_amount:.2f}")

        elif choice == 0:
            print(f"{item.title()} skipped.")

        else:
            print("Invalid choice. Item skipped.")

    return orders


def display_bill(orders):
    """Display the final restaurant bill."""

    print("\n" + "=" * 60)
    print("                     FINAL BILL")
    print("=" * 60)

    if not orders:
        print("No items were ordered.")
        return

    total_bill = 0
    total_discount = 0

    for item, details in orders.items():

        print(f"\n{item.title()}")
        print(f"Quantity       : {details['quantity']}")
        print(f"Price/plate    : ₹{details['price']}")
        print(f"Subtotal       : ₹{details['subtotal']}")
        print(f"Discount       : ₹{details['discount']:.2f}")
        print(f"Final amount   : ₹{details['final_amount']:.2f}")

        total_bill += details["subtotal"]
        total_discount += details["discount"]

    final_bill = total_bill - total_discount

    print("\n" + "-" * 60)
    print(f"Total Bill       : ₹{total_bill:.2f}")
    print(f"Total Discount   : ₹{total_discount:.2f}")
    print(f"Amount Payable   : ₹{final_bill:.2f}")
    print("-" * 60)

    print("\nThank you for visiting Your's Kitchen!")
    print("Please visit again.")
    print("\nDone by: VISWA")


# Main program

display_menu()

orders = take_order()

display_bill(orders)