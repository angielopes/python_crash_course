"""Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each
text message and moves each message to a new list called
sent_messages as it's printed. After calling the function,
print both of your lists to make sure the messages were moved correctly."""


def show_messages(short_messages, sent_messages):
    """Prints each text message and moves each message to a new list called sent_messages as it's printed."""
    while short_messages:
        current_message = short_messages.pop()
        print(f"Message to be sent: {current_message}")
        sent_messages.append(current_message)


def send_messages(sent_messages):
    """Shows messages that have been printed and moved to sent_messages"""
    print("\nSHORT MESSAGES FOR YOU (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    for message in sent_messages:
        print(f"{message}")


short_messages = [
    "Keep it simple.",
    "Never give up.",
    "Dream big.",
    "Stay positive.",
    "Work hard.",
    "Be kind.",
    "Think different.",
    "Believe in yourself.",
    "Take a chance.",
    "Make it happen.",
]

sent_messages = []

show_messages(short_messages, sent_messages)
send_messages(sent_messages)
