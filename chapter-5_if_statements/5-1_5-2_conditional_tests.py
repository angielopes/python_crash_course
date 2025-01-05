"""Write a series of conditional tests. Print a statement describing each
test and your prediction for the results of each test. Your code should
look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and
another 5 tests evaluate to False."""

# 1
desert = "cake"
print("DESERT")
print("Is my favorite desert == 'cake'? I predict True.")
print(desert == "cake")
# 2
print("Is my favorite desert == 'ice cream'? I predict False.")
print(desert == "ice cream")

# 3
my_age = 27
print("\nAGE")
print("Is my age < 30? I predict True.")
print(my_age < 30)
# 4
print("Is my age > 30? I predict False.")
print(my_age > 30)

# 5
print("\nARTISTS")
my_fav_artits = ["linkin park", "rammstein", "lady gaga", "jisoo"]
print("Is my favorite singer 'lady gaga' in the list? I predict True.")
print("lady gaga" in my_fav_artits)
# 6
print("Is the horrible singer 'lisa' in the list? I predict False.")
print("lisa" in my_fav_artits)

# 7
print("\nMOVIES")
movies_december_2024 = ["lake mungo", "speak no evil", "oddity", "heretic"]
print("Did I not watched 'bridget jones diary' in december of 2024? I predict True.")
print("bridget jones diary" not in movies_december_2024)
# 8
print("Did I not watched 'lake mungo' in december of 2024? I predict False.")
print("lake mungo" not in movies_december_2024)
