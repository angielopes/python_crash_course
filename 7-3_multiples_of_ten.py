"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

prompt = "Type a number so I can tell if it is multiple of 10 or not."
prompt += "\nNumber: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of 10!")
else:
    print(f"{number} is not multiple of 10!")
