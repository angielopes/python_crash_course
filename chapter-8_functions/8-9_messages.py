"""Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message."""


def show_messages(short_messages):
    print("SHORT MESSAGES FOR YOU (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    while short_messages:
        message = short_messages.pop()
        print(f"\n{message}")


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
show_messages(short_messages)
