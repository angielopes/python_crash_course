"""We're now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter, and extend it by adding new keys and values,
changing the context of the program, or improving the formatting of the output."""

pets = {
    "totoro": {
        "age": 1000,
        "especie": "spirit of nature",
        "owner": "nobody",
        "characteristic": "mystical",
    },
    "pikachu": {
        "age": 6,
        "especie": "electric mouse",
        "owner": "ash ketchum",
        "characteristic": "energetic",
    },
    "toothless": {
        "age": 20,
        "especie": "night fury dragon",
        "owner": "hiccup horrendous haddock iii",
        "characteristic": "brave",
    },
    "scooby_doo": {
        "age": 7,
        "especie": "great dane",
        "owner": "shaggy rogers",
        "characteristic": "funny",
    },
    "gizmo": {
        "age": 2,
        "especie": "mogwai",
        "owner": "billy peltzer",
        "characteristic": "mystical",
    },
    "chewbacca": {
        "age": 200,
        "especie": "wookiee",
        "owner": "han solo",
        "characteristic": "strong",
    },
    "slinky_dog": {
        "age": 5,
        "especie": "dog",
        "owner": "andy",
        "characteristic": "loyal",
    },
    "dobby": {
        "age": 50,
        "especie": "house elf",
        "owner": "nobody",
        "characteristic": "brave",
    },
}

emojis = {
    "mystical": "\U0001F333",
    "energetic": "\U000026A1",
    "brave": "\U0001F981",
    "funny": "\U0001F602",
    "strong": "\U0001F4AA",
    "loyal": "\U0001F91D",
}

corrected_names = {
    "nobody": "nodoby",
    "hiccup horrendous haddock iii": "Hiccup Horrendous Haddock III",
}

vogals = ["a", "e", "i", "o", "u"]

for pet, pet_info in pets.items():
    emoji = emojis.get(pet_info["characteristic"], "")
    name = pet.replace("_", " ")
    owner = pet_info["owner"].lower()
    owner = corrected_names.get(owner, owner.title())
    article = (
        "an"
        if pet_info["characteristic"][0] in vogals or pet_info["especie"][0] in vogals
        else "a"
    ) # Modify the article of the sentence according to the noun
    print(f"\n{name.title()} {emoji}")
    print(
        f"{name.title()} is {article} {pet_info['characteristic']} creature and {article} {pet_info['especie']}. It is {pet_info['age']} years old and belongs to {owner}."
    )
