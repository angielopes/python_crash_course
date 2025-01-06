"""Do the following to create a program that simulates how websites ensure
that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users.
Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used.
If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive.
If 'John' has been used, 'JOHN' should not be accepted.
(To do this, you'll need to make a copy of current_users containing the lowercase
versions of all existing users.)"""

current_users = ["secondstokill", "Admin", "JOSE123", "totoro", "minion", "sweetcake"]
new_users = ["admin", "Jose123", "coldbeer", "Sweetcake", "sleepycat"]
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry {user} it's already been used. Try another one.")
    else:
        print(f"The username {user} is available!")
