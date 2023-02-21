# Modify t_shirt.py w/ defaults size large & message "I Love Python"
# Make a large and a medium shirt with the default message
# Make a shirt of any size with any message

def make_shirt(size='Large', message="I Love Python"):
    """Confirms shirt size and message to print on shirt"""
    print(f"You have ordered a {size} shirt with message : \n{message}")

make_shirt()

make_shirt(size='Medium')

make_shirt(message="I'm learning Python!", size="small")