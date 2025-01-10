"""Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets.
Next, loop through your list and as you do, print everything you know about each pet."""

totoro = {
    "name": "totoro",
    "age": 1000,
    "especie": "spirit of nature",
    "owner": "nobody",
}

pikachu = {
    "name": "pikachu",
    "age": 6,
    "especie": "electric mouse",
    "owner": "ash ketchum",
}

toothless = {
    "name": "toothless",
    "age": 20,
    "especie": "night fury dragon",
    "owner": "hiccup horrendous haddock iii",
}

scooby_doo = {
    "name": "scooby-doo",
    "age": 7,
    "especie": "great dane",
    "owner": "shaggy rogers",
}

gizmo = {
    "name": "gizmo",
    "age": 2,
    "especie": "mogwai",
    "owner": "billy peltzer",
}

pets = [totoro, pikachu, toothless, scooby_doo, gizmo]
correcterd_names = {"hiccup horrendous haddock iii": "Hiccup Horrendous Haddock III"}

print("\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ WONDERFUL PETS")
for pet in pets:
    print(f"\n{pet['name'].upper()} (●ˇ∀ˇ●)")
    print(f"{pet['name'].title()} is {pet['age']} years old.")
    print(f"It belongs to the species of {pet['especie'].title()}.")
    # Correct owner's name, if necessary
    owner = pet["owner"].lower()
    owner = correcterd_names.get(owner, owner.title())
    print(f"{owner} owns it.")
