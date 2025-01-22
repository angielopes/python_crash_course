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
