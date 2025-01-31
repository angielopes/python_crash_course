"""You can use a loop to see how hard it might be to win the kind of lottery
you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins.
Print a message reporting how many times the loop had to run to give you a winning ticket."""

from module_lottery import Lottery

my_ticket = [14, 2, 3, 12]

lottery = Lottery()

attempts = 0
while True:
    attempts += 1
    draw_result = lottery.draw()
    if sorted(my_ticket) == draw_result:
        print(f"\nYou won after {attempts} attempts")
        lottery.show_results()
        break
    else:
        print("Maybe next time!")
