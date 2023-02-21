# Write a function called make_shirt() that accepts a size & message for shirt
# Should summarize size and message in print
# Call function using positional arguments to make shirt
# Call function using keyword arguments to make shirt

def make_shirt(size, message):
    """Confirms shirt size and message to print on shirt"""
    print(f"You have ordered a {size} shirt with message : \n{message}")

make_shirt('medium', 'Python n00b')

make_shirt(message="Python person", size='small')