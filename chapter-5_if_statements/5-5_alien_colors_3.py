"""Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien."""

alien_color = "green"

print("GREEN ALIEN")
if alien_color == "green":
    print("Congrats! You earned 5 points.")
elif alien_color == "yellow":
    print("Wow! 10 points for you.")
else:
    print("15 points :)))))")

alien_color = "yellow"

print("\nYELLOW ALIEN")
if alien_color == "green":
    print("Congrats! You earned 5 points.")
elif alien_color == "yellow":
    print("Wow! 10 points for you.")
else:
    print("15 points :)))))")

alien_color = "red"

print("\nRED ALIEN")
if alien_color == "green":
    print("Congrats! You earned 5 points.")
elif alien_color == "yellow":
    print("Wow! 10 points for you.")
else:
    print("15 points :)))))")
