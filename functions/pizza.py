# Module containing function make_pizza()

def make_pizza(size, *toppings):
    """Summarize pizza to make"""
    print(f"\nMaking a {size}-inch pizza with toppings:")
    for topping in toppings:
        print(f" - {topping}")