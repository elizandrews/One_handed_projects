# Make a list containing a series of short text messages
# Pass the list to a function show_messsages, which prints each text message

text_messages = ["I will be out of the office between March 12 - 15.",
"Please contact Mark Walhberg at markiemark@gmail.com with questions.",
"I will return any messages as soon as possible after I am back in the office."]

def show_messages(messages):
    """Prints text messages in a list"""
    for message in messages:
        print(message)

show_messages(text_messages)