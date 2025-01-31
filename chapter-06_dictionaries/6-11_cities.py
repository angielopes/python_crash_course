"""Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in,
its approximate population, and one fact about that city.
The keys for each city's dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it."""

cities = {
    "gotham city": {
        "country": "united states",
        "population": 10_000_000,
        "fact": "Gotham City is known for its high crime rate and is the home of Batman, the vigilante who fights to protect the city from criminal organizations.",
    },
    "hogsmeade": {
        "country": "united kingdom",
        "population": 1_000,
        "fact": "Hogsmeade is the only all-wizarding village in Britain and is located near Hogwarts School of Witchcraft and Wizardry. It’s famous for its magical shops, such as Honeydukes and Zonko’s Joke Shop.",
    },
    "zion": {
        "country": "zion",
        "population": 500_000,
        "fact": "Zion is a technologically advanced city known for its sustainable energy and futuristic architecture. It’s a symbol of environmental and technological harmony.",
    },
}

for city, city_info in cities.items():
    print(f"\n{city.upper()}")
    print(f"Country: {city_info['country'].title()}")
    print(f"Approximate Population: {city_info['population']}")
    print(f"Nice fact about: {city_info['fact']}")
