"""Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll.
If they have already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take the poll."""

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
poll = ["angela", "sarah", "julia", "phil"]

for name in poll:
    if name in favorite_languages:
        print(f"Thanks, {name.capitalize()}, for responding to the poll!")
    else:
        print(f"{name.capitalize()}, you have been invited to respond to the poll.")
