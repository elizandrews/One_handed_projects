# Beginning with messages.py, write a function called send_messages()
# Function should print each message and moves to new list sent_messages
# After calling the function, print both lists to make sure messages moved

text_messages = ["I will be out of the office between March 12 - 15.",
"Please contact Mark Walhberg at markiemark@gmail.com with questions.",
"I will return any messages as soon as possible after I am back in the office."]

sent_messages = []

def send_messages(messages, sent_list):
    """Prints text messages in a list & moves to sent list"""
    messages.reverse()
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_list.append(current_message)

send_messages(text_messages, sent_messages)

print(text_messages)
print(sent_messages)