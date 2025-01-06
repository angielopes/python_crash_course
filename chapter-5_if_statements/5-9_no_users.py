"""Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed."""

usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello, {user.title()}. Would you like to see a status report?")
        else:
            print(f"Hello, {user.title()}. Thank you for logging in again!")
else:
    print("We need to find some users!")
